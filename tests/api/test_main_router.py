import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from router.main_router import router
from fastapi import FastAPI


app = FastAPI()
app.include_router(router)

client = TestClient(app)

# load mock data from json files
import os

mock_request_body = {
    "statistic": "average",
    "date": "29-04-2025",
    "metrics": "temperature",
    "sensors": ["sensor1", "sensor2"]
}

mock_invalid_body = {
    "statistic": "invalid_statistic",
    "date": "invalid_date",
    "metrics": "invalid_metric",
    "sensors": ["invalid_sensor"]
}

mock_response_body = {
    "statistic": "average",
    "sensors": ["sensor1", "sensor2"],
    "date": "29-04-2025",
    "metrics": "temperature",
    "response": "{'sensor1_temperature_average': 25.5, 'sensor2_temperature_average': 30.0}",
    "msg": "success"
}

@patch("util.input_validation.validate_sensor_ids", return_value=True)
@patch("util.input_validation.validate_date")
@patch("util.input_validation.validate_metrics", return_value=["temperature"])
@patch("util.input_validation.validate_statistics", return_value=True)
@patch("router.database_router.get_sensor_data", side_effect=[{"temperature": 20}, {"temperature": 30}])
@patch("util.statistics_calculator.calculate_average", return_value=25.5)
@patch("util.parser.build_response_for_service", return_value=mock_response_body)
def test_get_sensor_statistics_success(
    mock_parser,
    mock_calculate_average,
    mock_get_sensor_data,
    mock_validate_statistics,
    mock_validate_metrics,
    mock_validate_date,
    mock_validate_sensor_ids,
):
    response = client.post("/sensor/stats", json=mock_request_body)
    assert response.status_code == 200
    assert response.json() == mock_response_body
    
    
def test_get_sensor_statistics_invalid_body():
    """
    Test that the API returns a 500 status code when provided with an invalid request body.
    """
    response = client.post("/sensor/stats", json=mock_invalid_body)
    assert response.status_code == 500  # Unprocessable Entity for invalid request body


@patch("util.input_validation.validate_sensor_ids", side_effect=Exception("Invalid sensor ID"))
def test_get_sensor_statistics_invalid_sensor(mock_validate_sensor_ids):
    response = client.post("/sensor/stats", json=mock_request_body)
    assert response.status_code == 500
    assert "Invalid sensor ID" in response.json()["detail"]
    

@patch("router.database_router.get_sensor_data", side_effect=Exception("Database error"))
def test_get_sensor_statistics_database_error(mock_get_sensor_data):
    response = client.post("/sensor/stats", json=mock_request_body)
    assert response.status_code == 500
    assert "Database error" in response.json()["detail"]
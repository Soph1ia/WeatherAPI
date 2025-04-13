import pytest
from datetime import datetime, timedelta
from fastapi import HTTPException
from util import input_validation

def test_validate_sensor_ids_valid():
    valid_sensors = ["sensor1", "sensor2"]
    assert input_validation.validate_sensor_ids(valid_sensors) is True

def test_validate_sensor_ids_invalid():
    invalid_sensors = ["sensor5", "sensor6"]
    with pytest.raises(HTTPException) as excinfo:
        input_validation.validate_sensor_ids(invalid_sensors)
    assert excinfo.value.status_code == 400
    assert "Invalid sensor ID" in str(excinfo.value.detail)

def test_validate_date_valid():
    valid_date = (datetime.now() - timedelta(days=5)).strftime("%d-%m-%Y")
    parsed_date = input_validation.validate_date(valid_date)
    assert parsed_date.strftime("%d-%m-%Y") == valid_date

def test_validate_date_invalid_format():
    invalid_date = "2025-04-29"
    with pytest.raises(HTTPException) as excinfo:
        input_validation.validate_date(invalid_date)
    assert excinfo.value.status_code == 400
    assert "Invalid date format" in str(excinfo.value.detail)

def test_validate_date_out_of_range():
    out_of_range_date = (datetime.now() - timedelta(days=31)).strftime("%d-%m-%Y")
    with pytest.raises(HTTPException) as excinfo:
        input_validation.validate_date(out_of_range_date)
    assert excinfo.value.status_code == 400
    assert "Date out of range" in str(excinfo.value.detail)

def test_validate_metrics_valid():
    valid_metrics = "temperature,humidity"
    parsed_metrics = input_validation.validate_metrics(valid_metrics)
    assert parsed_metrics == ["temperature", "humidity"]

def test_validate_metrics_invalid():
    invalid_metrics = "invalid_metric"
    with pytest.raises(HTTPException) as excinfo:
        input_validation.validate_metrics(invalid_metrics)
    assert excinfo.value.status_code == 400
    assert "Invalid metric" in str(excinfo.value.detail)

def test_validate_statistics_valid():
    valid_statistic = "average"
    assert input_validation.validate_statistics(valid_statistic) is True

def test_validate_statistics_invalid():
    invalid_statistic = "median"
    with pytest.raises(HTTPException) as excinfo:
        input_validation.validate_statistics(invalid_statistic)
    assert excinfo.value.status_code == 400
    assert "Invalid statistic" in str(excinfo.value.detail)
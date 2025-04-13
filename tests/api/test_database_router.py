""" Test to validate that the database router is working as expected. """

import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from fastapi import HTTPException
from router.database_router import get_sensor_data



def test_get_sensor_data_success():
    # Mock inputs
    sensor_id = 1
    date = "2023-01-01"
    mock_rows_db = [{"id": 1, "value": 25.5, "date": "03-04-2025"}]
    mock_parsed_data = {"sensor_id": 1, "data": [{"value": 25.5, "date": "03-04-2025"}]}

    # Mock dependencies
    with patch("router.database_router.sensor_db_api.query_database", return_value=mock_rows_db) as mock_query_db, \
         patch("router.database_router.parser.parse_response_from_database", return_value=mock_parsed_data) as mock_parser:
        
        # Call the function
        result = get_sensor_data(sensor_id, date)

        # Assertions
        mock_query_db.assert_called_once_with(sensor_id, date)
        mock_parser.assert_called_once_with(mock_rows_db, sensor_id, date)
        assert result == mock_parsed_data

def test_get_sensor_data_failure():
    # Mock inputs
    sensor_id = 1
    date = "08-04-2025"

    # Mock dependencies
    with patch("router.database_router.sensor_db_api.query_database", side_effect=Exception("Database error")):
        try:
            # Call the function
            get_sensor_data(sensor_id, date)
        except HTTPException as e:
            # Assertions
            assert e.status_code == 500
            assert "Error in get_sensor_data: Database error" in e.detail
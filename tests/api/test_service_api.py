# import methods for testing 
import pytest
from fastapi.testclient import TestClient
from main import app
from schemas import request_schema, response_schema
from api import service_api
from router import main_router
from unittest.mock import patch, MagicMock

# Create a test client for the FastAPI app
client = TestClient(app)

# Mock the database connection and methods
def mock_get_sensor_details_from_database():
    return [
        (1, 25.0, 60.0, 10.0, "2023-10-01 12:00:00"),
        (2, 30.0, 55.0, 15.0, "2023-10-02 12:00:00"),
        (3, 20.0, 70.0, 5.0, "2023-10-03 12:00:00"),
    ]
    
def mock_get_average_sensor_data(sensor_id, metric, date_range):
    return 25.0
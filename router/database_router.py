from fastapi import Body, HTTPException, APIRouter
from typing import Annotated
from schemas import request_schema, response_schema
from database import sensor_db_api
from util import parser

router = APIRouter()

@router.get("/init_db", tags=["Database"])
def init_database():
    """
    Initialize the database connection and create tables if they do not exist.
    """
    print("Initializing database...")
    try: 
        sensor_db_api.init_database()
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail="Internal server error: Unable to initialize the database.")


def get_sensor_data(sensor_id: int, date: str):
    """
    Query the database for sensor data.
    
    Args:
        sensor_id (int): The ID of the sensor to query.
        
    Returns:
        dict: A dictionary containing the sensor data.
    """
    try:
        # Call the database API to get the sensor data
        rows_db = sensor_db_api.query_database(sensor_id, date)
        # Construct the data response into the response_schema
        sensor_data  = parser.parse_response_from_database(rows_db, sensor_id, date)
        # print("Sensor data:", sensor_data)
        return sensor_data
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Error in get_sensor_data: {str(e)}")

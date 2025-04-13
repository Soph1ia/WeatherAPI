"""
This file is used for gathering latest data from 
weather APIs 
"""
import random 
import datetime
import logging

logger  = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def fetch_latest_data():
    """
    This function fetches the latest data from the weather API.
    It is a placeholder function and should be replaced with actual API calls.
    """
    # Simulate fetching data from an API
    print("Fetching latest data from the weather API...")
    
    # Simulate some data processing
    data = {
        "sensor_id": random.randint(1, 6),
        "temperature": random.uniform(-10, 40),
        "humidity": random.uniform(0, 100),
        "wind_speed": random.uniform(0, 20),
        "date": datetime.datetime.now().strftime("%d-%m-%Y")
    }
    
    logger.info(f"Fetched data: {data}")
    return data
    
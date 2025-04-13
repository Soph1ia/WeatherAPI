"""
This file contains utility functions for input validation in the WeatherAPI project.
It includes functions to validate sensor IDs, dates, and statistics requests.
"""

from datetime import datetime
from typing import List, Optional, Union
from fastapi import HTTPException
from pydantic import BaseModel, Field, conlist, constr, conint
from enum import Enum

def validate_sensor_ids(sensor_list) -> bool:
    """
    This method validates list of sensorIDs
    Only sensor ids in the valid range (sensor1, sensor2, sensor3 and sensor4) are accepted.

    Args:
        sensor_list (list): List of sensor IDs to validate.
        
    Returns:
        bool: True if all sensor IDs are valid, False otherwise.
    """
    valid_sensor_ids = ["sensor1", "sensor2", "sensor3", "sensor4"]
    
    # Check if all sensor IDs are valid
    for sensor_id in sensor_list:
        if sensor_id not in valid_sensor_ids:
            raise HTTPException(status_code=400, detail=f"Invalid sensor ID '{sensor_id}'. Valid IDs are {', '.join(valid_sensor_ids)}.")
    
    return True

def validate_date(date_string: str) -> datetime:
    """
    Parse a date string into a datetime object.
    In this application we can only accept dates in the format DD-MM-YYYY
    We can only go back 30 days from today.
    If there is an error parsing the date string, default to today's date.
    
    Args:
        date_string (str): The date string to parse.
        
    Returns:
        datetime: A datetime object representing the parsed date.
    """
    try:
        date = datetime.strptime(date_string, "%d-%m-%Y")
    except ValueError:
        date = datetime.now()
        raise HTTPException(status_code=400, detail="Invalid date format. Use 'DD-MM-YYYY'. Defaulting to today's date.")
    
    # Check if the date is within the last 30 days
    if (datetime.now() - date).days > 30:
        date = datetime.now() 
        raise HTTPException(status_code=400, detail="Date out of range. Only dates within the last 30 days are allowed. Defaulting to today's date.")
    
    return date

def validate_metrics(metrics_string: str) -> List[str]:
    """
    Parse a metrics string into a list of metrics.
    In this application we can only accept the following metrics:
    temperature, humidity, wind_speed, and date.
    
    Args:
        metrics_string (str): The metrics string to parse.
        
    Returns:
        List[str]: A list of metrics.
        
    Raises:
        HTTPException: If the metrics string is invalid.
    """
    
    valid_metrics = ["temperature", "humidity", "wind_speed", "date"]
    metrics = metrics_string.split(",")
    metrics = [m.strip() for m in metrics]
    
    # Check if the metrics are valid
    for metric in metrics:
        if metric not in valid_metrics:
            raise HTTPException(status_code=400, detail=f"Invalid metric '{metric}'. Valid metrics are {', '.join(valid_metrics)}.")
    
    return metrics

def validate_statistics(statistics: str) -> bool:
    """
    Validate the statistics request.
    In this application we can only accept the following statistics:
    average, sum, min, max.
    
    Args:
        statistics (str): The statistics string to validate.
        
    Returns:
        bool: True if the statistics string is valid, False otherwise.
        
    Raises:
        HTTPException: If the statistics string is invalid.
    """
    
    valid_statistics = ["average", "sum", "min", "max"]
    
    # Check if the statistics are valid
    if statistics not in valid_statistics:
        raise HTTPException(status_code=400, detail=f"Invalid statistic '{statistics}'. Valid statistics are {', '.join(valid_statistics)}.")
    
    return True
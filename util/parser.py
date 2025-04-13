"""
This module contains utility functions for parsing and validating data in the WeatherAPI project.
"""
from schemas import response_schema


def parse_response_from_database(data:list,sensor_id:int, date:str ):
    """
    Parse the response from the database and construct a response schema.
    The data comes to us in the format (id, sensorid, temp, humidity, wind_speed, date)
    
    Args:
        data (list): The data retrieved from the database.
        sensor_id (int): The ID of the sensor.
        date (str): The date for which the data is requested.
        
    Return: 
        SensorDataResponse: A Pydantic model representing the sensor data response.  
    """
    processed_data = []
    for row in data:
        print("The row is:", row)
        sensor_data = {
                "sensor_id": row[1],
                "date": row[5],
                "temperature": row[2],
                "humidity": row[3],
                "wind_speed": row[4]
            }
        processed_data.append(sensor_data)
    print("The processed data is:", processed_data)
    return processed_data
        
def build_response_for_service(
        statistic:str, 
        sensor_ids:list, 
        date:str, 
        metrics:str, 
        response:dict, 
        msg:str) -> response_schema.StatisticsResponseSchema:
    """
    Build a response for the service API.
    
    Args:
        statistic (str): The type of statistic (e.g., "average", "min", "max").
        sensor_id (int): The ID of the sensor.
        date (str): The date for which the statistics are requested.
        metrics (list): A list of metrics to include in the statistics.
        response (float): The calculated statistic value.
        msg (str): A message indicating success or failure.
        
    Returns:
        StatisticsResponse: A Pydantic model representing the response.
    """
    return response_schema.StatisticsResponseSchema(
        statistic=statistic,
        sensors=sensor_ids,
        date=date,
        metrics=metrics,
        response=response,
        msg=msg
    )
    
def parse_sensor_id(sensor_id:str) -> int:
    """
    Parse the sensor ID from a string format (e.g., "sensor1" to 1).
    
    Args:
        sensor_id (str): The sensor ID in string format.
        
    Returns:
        int: The parsed sensor ID as an integer.
        
    Raises:
        ValueError: If the sensor ID is not in the expected format.
    """
    try:
        # Extract the numeric part of the sensor ID
        return int(sensor_id.replace("sensor", ""))
    except ValueError:
        raise ValueError(f"Invalid sensor ID format: {sensor_id}")
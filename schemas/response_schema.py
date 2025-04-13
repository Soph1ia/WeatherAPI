from pydantic import BaseModel
class StatisticsResponseSchema(BaseModel):
    """
    Response schema for sensor statistics endpoint.
    
    Attributes:
        statistic (str): The type of statistic calculated.
        sensors (list): A list of sensors included in the statistics . 
        date (str): The date for which the statistics were requested.
        metrics (list): A list of metrics included in the statistics. 
        response (dict): The response containing the calculated statistics.
        msg (str): A message indicating the status of the request.
    """
    
    statistic: str
    sensors: list
    date: str
    metrics: str
    response: str  # Assuming response is a dictionary with metric names as keys and their values as floats
    msg: str 
    
class SensorDataResponse(BaseModel):
    """
    Response schema for sensor data endpoint.
    
    Attributes:
        sensor_id (str): The ID of the sensor.
        date (str): The date for which the data is requested.
        metrics (dict): A dictionary containing the sensor data metrics.
    """
    
    sensor_id: str
    date: str
    metrics: dict[str, float]  # Assuming metrics are key-value pairs where key is metric name and value is its value
    
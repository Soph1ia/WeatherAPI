from pydantic import BaseModel
class StatisticsResponseSchema(BaseModel):
    """
    Response schema for sensor statistics endpoint.
    
    Attributes:
        statistic (str): The type of statistic calculated (e.g., "average", "min", "max").
        sensor (list): A list of sensors included in the statistics (e.g., ["sensor1", "sensor2"]). 
        date (str): The date for which the statistics were requested.
        metrics (list): A list of metrics included in the statistics (e.g., ["temperature", "humidity"]). 
        response (int): The response code indicating success or failure.
        msg (str): A message indicating the status of the request.
    """
    
    statistic: str
    sensor: list[str]
    date: str
    metrics: list[str]
    response: int
    msg: str 
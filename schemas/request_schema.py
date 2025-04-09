from pydantic import BaseModel
from typing import Union

# Data Model
class StatisticsRequestBody(BaseModel):
    """
    Request body for sensor statistics endpoint.
    
    Attributes:
        statistic (str): The type of statistic to calculate (e.g., "average", "min", "max").
        date (str): The date for which the statistics are requested.
        metrics (list): A list of metrics to include in the statistics (e.g., ["temperature", "humidity"]). 
        sensors (list): A list of sensors to include in the statistics (e.g., ["sensor1", "sensor2"]).
    """
    
    statistic: str
    date: Union[str, None] = 1
    metrics: list[str]
    sensors: list [str]

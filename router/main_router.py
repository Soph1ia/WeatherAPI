from fastapi import Body, HTTPException, APIRouter
from typing import Annotated
from schemas import request_schema, response_schema

router = APIRouter()


@router.post("/sensor/stats", response_model=response_schema.StatisticsResponseSchema)
async def get_sensor_statistics(
    item: Annotated[
        request_schema.StatisticsRequestBody,
        Body(
            examples=[
                {
                    "statistic": "average",
                    "date": "1",
                    "metrics": ["temperature", "humidity"],
                    "sensors": ["sensor1", "sensor2"],
                }
            ],
        ),
    ],
):
    """
    This method is used to get the statistics of the sensors.
    It takes the request body as input and returns the statistics response.
    
    Args:
        item (StatisticsRequestBody): The request body containing the statistics request.
        
    """
    # Here you would typically process the request and return a response.
    # For demonstration purposes, we'll just return the input data as the response.
    try : 
        variable_to_return = {
        "statistic": "aver",
        "sensor": ["sensor1", "sensor2"],
        "date": "1",
        "metrics": ["temperature", "humidity"],
        "response": 1,
        "msg": "success",
    }
        
        # do input validation 
        
        # call the
    except Exception as e:
        # Handle any exceptions that may occur during processing
        raise HTTPException(status_code=500, detail=str(e))
        
    return variable_to_return
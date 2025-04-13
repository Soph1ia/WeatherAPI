from fastapi import Body, HTTPException, APIRouter
from typing import Annotated
from schemas import request_schema, response_schema
from util import input_validation, statistics_calculator,parser
from router import database_router
import logging
import json

router = APIRouter()
logger = logging.getLogger(__name__)

def validation(request_body) -> bool:
        return input_validation.validate_sensor_ids(request_body['sensors']) and input_validation.validate_date(request_body['date'])and input_validation.validate_metrics(request_body['metrics']) and input_validation.validate_statistics(request_body['statistic'])


@router.post("/sensor/stats")
async def get_sensor_statistics(
    item: Annotated[
        request_schema.StatisticsRequestBody,
        Body(
            examples=[
                {
                    "statistic": "average",
                    "date": "29-04-2025",
                    "metrics": "temperature",
                    "sensors": ["sensor1", "sensor2"],
                }
            ],
        ),
    ],
) -> response_schema.StatisticsResponseSchema:
    """
    This method is used to get the statistics of the sensors.
    It takes the request body as input and returns the statistics response.
    
    Args:
        item (StatisticsRequestBody): The request body containing the statistics request.
        
    """
    try :         
        # Access the request body using model_dump (if needed for debugging or processing)
        request_body = item.model_dump()
        logger.info(f"Request body: {request_body}")
        print("Request body:", request_body)
        print("Sensors:", request_body['sensors'])
        print("Date:", request_body['date'])
        print("Metrics:", request_body['metrics'])
        print("Statistic:", request_body['statistic'])
        
        # Validate inputs using utility functions
        valid_input = validation(request_body)
        list_of_sensor_data = []    
        
        # Only proceed if all are valid
        if valid_input:
            logger.info("All inputs are valid.")

            try: # For this example we update the database everytime we call the API
                database_router.update_database()
            except Exception as e:
                raise HTTPException(
                    status_code=500, 
                    detail=f"Error in update_db: {str(e)}")
            
            for sensor in request_body['sensors']:
                # Call the database API to get the sensor data
                sensor_data = database_router.get_sensor_data(sensor_id=sensor, date=request_body['date'])
                list_of_sensor_data.append(sensor_data)
            
            statistics_from_data = []
            # Call the statistics calculator to get the statistics from the data    
            # process the data to get the relevant statistics. 
            if request_body['statistic'] == "average":
                # get the average of the metrics specified. 
                statistics_from_data = statistics_calculator.calculate_average(list_of_sensor_data, request_body['metrics'],request_body['sensors'])
            elif request_body['statistic'] == "max":
                # get the max of the metrics specified. 
                statistics_from_data = statistics_calculator.calculate_max(list_of_sensor_data, request_body['metrics'],request_body['sensors'])
            elif request_body['statistic'] == "min":
                # get the min of the metrics specified. 
                statistics_from_data = statistics_calculator.calculate_min(list_of_sensor_data, request_body['metrics'],request_body['sensors'])
            elif request_body['statistic'] == "sum":
                # get the sum of the metrics specified. 
                statistics_from_data = statistics_calculator.calculate_sum(list_of_sensor_data, request_body['metrics'],request_body['sensors'])
                
            # parse the response to fit the response schema.
            statistics_from_data = parser.build_response_for_service(
                request_body['statistic'],
                request_body['sensors'],
                request_body['date'],
                request_body['metrics'],
                str(statistics_from_data),
                "success"
            )
            return statistics_from_data

    except Exception as e:
        # Handle any exceptions that may occur during processing
        raise HTTPException(
            status_code=500, 
            detail=f"Error in get_sensor_statistics: {str(e)}")
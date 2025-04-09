import sqlite3


def get_sensor_details(metric, sensor_number, statistic, date_range=1):
    """
    This method is used to get the details of the sensors.
    It takes the request body as input and returns the details response.
    
    Args:
        metric (str): The metric to be used for the sensor.
        sensor_number (str): The number of the sensor.
        statistic (str): The statistic to be used for the sensor.
        date_range (int, optional): The date range for the sensor. Defaults to 1.
        
    Returns:
        dict: A dictionary containing the sensor details.
    """
    # Here you would typically process the request and return a response.
    # For demonstration purposes, we'll just return the input data as the response.
    
    # validate the inputs received
    
    # given the metric and the statistic call the metho
    
    
    variable_to_return = {
        "statistic": statistic,
        "sensor": [sensor_number],
        "date": date_range,
        "metrics": [metric],
        "response": 1,
        "msg": "success",
    }
    return variable_to_return

def verify_request_input():
    return True

def get_average_sensor_data(sensor_id, metric, date_range):
    """
    This method is used to get the average sensor data.
    """

def get_maximum_sensor_data(sensor_id, metric, date_range):
    """
    This method is used to get the maximum sensor data.
    """
    
def get_minimum_sensor_data(sensor_id, metric, date_range):
    """
    This method is used to get the minimum sensor data.
    """

def get_sensor_details_from_database():
    """
    This method is used to get the details of the sensors from the database.
    It connects to the SQLite database and fetches all sensor data.
    
    Returns:
        list: A list of tuples containing the sensor data.
    """
    # Connect to the SQLite database
    conn = sqlite3.connect('sensor_data.db')
    
    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()
    
    # Execute a query to fetch all sensor data
    cursor.execute('SELECT * FROM sensor_data')
    
    # Fetch all rows from the executed query
    rows = cursor.fetchall()
    
    # Close the database connection
    conn.close()
    
    return rows
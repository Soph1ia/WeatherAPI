import sqlite3
import random
from datetime import datetime, timedelta
from util import parser
import time
import requests
import sqlite3
from datetime import datetime
from database import weather_data_api
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def init_database():
    """
    Initialize the database connection and create tables if they do not exist.
    """
    # Connect to (or create) a local database file
    conn = sqlite3.connect('sensor_data.db')

    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    # Create a table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sensor_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sensorid INTEGER NOT NULL,
            temp FLOAT UNIQUE NOT NULL,
            humidity FLOAT UNIQUE NOT NULL,
            wind_speed FLOAT UNIQUE NOT NULL,
            date TEXT NOT NULL
        );
    ''')

    # iterate through and insert data into the table for each sensor insert 5 records and insert random dates
    for sensor_id in range(1, 6):
        for _ in range(10):
            # Generate random sensor data
            temp = random.uniform(-10.0, 35.0)  # Random temperature between -10 and 35 degrees Celsius
            humidity = random.uniform(0.0, 100.0)  # Random humidity between 0 and 100 percent
            wind_speed = random.uniform(0.0, 20.0)  # Random wind speed between 0 and 20 m/s
            date = (datetime.now() - timedelta(days=random.randint(0, 10))).strftime('%d-%m-%Y')  # Random date within the last 10 days

            # Insert the data into the table    
            cursor.execute('''
                INSERT INTO sensor_data (sensorid, temp, humidity, wind_speed, date)
                VALUES (?, ?, ?, ?, ?)
            ''', (sensor_id, temp, humidity, wind_speed, date))

    # Query the data
    cursor.execute('SELECT * FROM sensor_data')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Commit changes and close the connection
    conn.commit()
    conn.close()
    pass

def query_database(sensor_id, date):
    """
    Query the database for sensor data.
    
    Args:
        sensor_id (int): The ID of the sensor to query.
        date (str): The date to filter the data.
        
    Returns:
        list: A list of tuples containing sensor data.
        
    Raises:
        sqlite3.Error: If there is an error querying the database.
    """
    
    # Connect to the database
    conn = sqlite3.connect('sensor_data.db')
    cursor = conn.cursor()
    
    print("The sensor id is:", sensor_id)
    
    # parse the sensor_id and get the number from structure sensor1 to 1 
    sensor_id = parser.parse_sensor_id(sensor_id)

    # Query the database for the specified sensor ID and get until the specified date
    cursor.execute('''
        SELECT * FROM sensor_data WHERE sensorid = ? AND date <= ?
    ''', (sensor_id, date))
    rows = cursor.fetchall()
    
    print("The rows are:", rows)

    # Close the connection
    conn.close()

    return rows


def update_database():
    """
    TODO: This method updates the database with new entries.
    It polls the API for new entries and updates the database.
    """
    
    # Call the weather_data API to get the latest sensor data
    latest_data = weather_data_api.fetch_latest_data()
    logger.info(f"Latest data from weather API: {latest_data}")
    
    # Call the database API to update the database
    try: 
        # Connect to (or create) a local database file
        conn = sqlite3.connect('sensor_data.db')

        # Create a cursor object to execute SQL commands
        cursor = conn.cursor()
        # Add new entried from the weather_data API to the database
        cursor.execute('''
            INSERT INTO sensor_data (sensorid, temp, humidity, wind_speed, date)
            VALUES (?, ?, ?, ?, ?)
        ''', (latest_data['sensor_id'], latest_data['temperature'], latest_data['humidity'], latest_data['wind_speed'], latest_data['date']))
        # Commit changes and close the connection
        conn.commit()
        conn.close()
    except Exception as e:
        raise Exception(f"Error in update_db: {str(e)}")
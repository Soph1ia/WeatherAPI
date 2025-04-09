import sqlite3
import random
from datetime import datetime, timedelta

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
    for _ in range(5):
        # Generate random sensor data
        temp = random.uniform(-10.0, 35.0)  # Random temperature between -10 and 35 degrees Celsius
        humidity = random.uniform(0.0, 100.0)  # Random humidity between 0 and 100 percent
        wind_speed = random.uniform(0.0, 20.0)  # Random wind speed between 0 and 20 m/s
        date = (datetime.now() - timedelta(days=random.randint(1, 30))).strftime('%Y-%m-%d %H:%M:%S')  # Random date within the last month

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

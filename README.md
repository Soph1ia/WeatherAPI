# WeatherAPI
This application is using FastAPI to deploy an API endpoint that will allow users to query and get the latest statistics of different sensors. 

## Architecture Overview
![WeatherAPI-Planning](https://github.com/user-attachments/assets/dc3c168c-37f1-4034-8355-fcd2a91bd53f)

## How To Run This Project

### Environment setup 
1. Python version: `3.9.12`
2. Install `pip install -r requirements.txt`
3. Navigate to main.py 
4. In a bash terminal run the following command:  `fastapi dev main.py `
5. From a browser go to `localhost:8000/docs`

### Run The query 
When the application is running locally and you have opened a browser on `localhost:8000/docs` you will see a document page that will let you test out the endpoint. 
You should be able to see this if you have everything set up correctly. 
![image](https://github.com/user-attachments/assets/a96248f1-1589-45df-9f92-e3b10d02d905)

### How to run the tests
From the main folder run the following code in the terminal

`python -m pytest`
![image](https://github.com/user-attachments/assets/5e4e479a-9ea1-41e8-99ee-a18a4f0e3384)


# Planning

## Basic Commitment 
- Fast API
- Users can query sensor, statistic, date range, max/min
- Application returns this statistic.
- Store sensor data in a persisted database.

### Testing 
- Pytesting methods
- Test database
- input validation

## Stretch Goal 
- Use a hugging face model link the methods to the LLM
- Allowing users to state a sentence and retrieve results through an LLM
- Polling to get the latest data into the database

# Thoughts on Improving the Solution 
- CI/CD pipeline
- performance testing
- cloud deployment potentially
- Caching?

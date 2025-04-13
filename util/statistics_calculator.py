"""
This module contains utility functions to calculate statistics for sensor data.
It includes functions to calculate average, minimum, and maximum values for given metrics.
"""
from util import parser

def calculate_average(data_list:list, metric:str, sensor_ids:list) -> list:
    """
    Calculate the average of a list of numbers.
    
    Args:
        data (list): rows returns from a database
        metrics(list): A list of metrics to calculate the average for.
        
    Returns:
        float: The average value.
    """
    dictionary_of_averages = {}

    for data in data_list:
        metric_values = [] 
        for row in data:
            sensor_id_in_current_list = row.get("sensor_id")
            metric_values.append(row.get(metric))
        
        if metric_values:
            dictionary_of_averages[str(sensor_id_in_current_list) +"_"+ metric + "_average"] = sum(metric_values) / len(metric_values)
        else :
            dictionary_of_averages[str(sensor_id_in_current_list) +"_"+ metric + "_average"] = 0.0
            
        print("The results are : ", dictionary_of_averages)
    
    return dictionary_of_averages

def calculate_min(data_list:list, metric:str, sensor_ids:list) -> list:
    """
    Calculate the minimum of a list of numbers.
    
    Args:
        data (list): rows returns from a database
        metrics(list): A list of metrics to calculate the average for.
        
    Returns:
        float: The average value.
    """
    dictionary_of_minimum = {}

    for data in data_list:
        metric_values = [] 
        for row in data:
            sensor_id_in_current_list = row.get("sensor_id")
            metric_values.append(row.get(metric))
        
        if metric_values:
            dictionary_of_minimum[str(sensor_id_in_current_list) +"_"+ metric + "_average"] = min(metric_values)
        else :
            dictionary_of_minimum[str(sensor_id_in_current_list) +"_"+ metric + "_average"] = 0.0
            
    
    return dictionary_of_minimum

def calculate_max(data_list:list, metric:str, sensor_ids:list) -> list:
    """
    Calculate the maximum of a list of numbers.
    
    Args:
        data (list): rows returns from a database
        metrics(list): A list of metrics to calculate the average for.
        
    Returns:
        float: The average value.
    """
    dictionary_of_maximum = {}

    for data in data_list:
        metric_values = [] 
        for row in data:
            sensor_id_in_current_list = row.get("sensor_id")
            metric_values.append(row.get(metric))
        
        if metric_values:
            dictionary_of_maximum[str(sensor_id_in_current_list) +"_"+ metric + "_average"] = max(metric_values)
        else :
            dictionary_of_maximum[str(sensor_id_in_current_list) +"_"+ metric + "_average"] = 0.0
            
    
    return dictionary_of_maximum

def calculate_sum(data_list:list, metric:str, sensor_ids:list) -> list:
    """
    Calculate the sum of a list of numbers.
    
    Args:
        data (list): rows returns from a database
        metrics(list): A list of metrics to calculate the average for.
        
    Returns:
        float: The average value.
    """
    dictionary_of_sum = {}

    for data in data_list:
        metric_values = [] 
        for row in data:
            sensor_id_in_current_list = row.get("sensor_id")
            metric_values.append(row.get(metric))
        
        if metric_values:
            dictionary_of_sum[str(sensor_id_in_current_list) +"_"+ metric + "_average"] = sum(metric_values)
        else :
            dictionary_of_sum[str(sensor_id_in_current_list) +"_"+ metric + "_average"] = 0.0
            
    
    return dictionary_of_sum
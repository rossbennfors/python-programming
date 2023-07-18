# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification
import numpy as np 
from utils import *
import pandas as pd

data = {
    "Harlington" : pd.read_csv('data/Pollution-London Harlington.csv'),
    "Marylebone" : pd.read_csv('data/Pollution-London Marylebone Road.csv'),
    "Kensington" : pd.read_csv('data/Pollution-London N Kensington.csv')
    }

def daily_average(data, monitoring_station, pollutant):
    """Calculates the average for each day across the whole year for the monitoring station and pollutant requested.
    
    Args:
        data is the dictionary with monitoring stations as keys and a pandas dataframe as values.
        monitoring _station is the station chosen, options: Harlington, Marylebone, Kensington. 
        pollutant is the type of pollution chosen, options: no, pm10, pm25.
    Returns:
        The calculated average for each day from the chosen monitoring station and pollutant for each day in a list.
    """

    data_list = data[monitoring_station][pollutant].to_list()
    averages = []
    current_average = []
    hour_counter = 0

    for i in data_list:                    
        if hour_counter < 23: 
            if i == 'No data': #skips over No data values so not to affect average
                hour_counter += 1
                continue              
            current_average.append(float(i))
            hour_counter += 1

        else:
            if len(current_average) == 0:
                averages.append('No data')
            else:
                average = sumvalues(current_average)/len(current_average) #calculates average
                averages.append(average) 
            current_average.clear() #clears the current_average list so it is empty for the next day of data points
            hour_counter = 0 #rests counter

    return averages

def daily_median(data, monitoring_station, pollutant):
    """Calculates the median value for each day for the monitoring station and pollutant requested.
    
    Args:
        data is the dictionary with monitoring stations as keys and a pandas dataframe as values.
        monitoring _station is the station chosen, options: Harlington, Marylebone, Kensington. 
        pollutant is the type of pollution chosen, options: no, pm10, pm25.
    Returns:
        The calculated median from the chosen monitoring station and pollutant for each day in a list.
    """
    
    data_list = data[monitoring_station][pollutant].to_list()
    medians = []
    current_values = []
    hour_counter = 0
    
    for i in data_list:
        if hour_counter < 23:
            if i == 'No data': #skips over No data values so not to affect average
                hour_counter += 1
                continue
            current_values.append(float(i))
            hour_counter += 1
        
        else:
            if len(current_values) == 0:
                medians.append('No data')
            else:
                median = np.median(current_values)
                medians.append(median)
            current_values.clear()
            hour_counter = 0
    
    return medians

def hourly_average(data, monitoring_station, pollutant):
    """Calculates the average for each hour of the day across the whole year for the monitoring station and pollutant requested.
    
    Args:
        data is the dictionary with monitoring stations as keys and a pandas dataframe as values.
        monitoring _station is the station chosen, options: Harlington, Marylebone, Kensington. 
        pollutant is the type of pollution chosen, options: no, pm10, pm25.
    Returns:
        The calculated average for each hour of the day from the chosen monitoring station and pollutant for each day in a list.
    """

    grouped = data[monitoring_station].groupby('time')[pollutant]
    data_by_time = {time: list(group) for time, group in grouped}
    current_average = []
    averages = []

    for x in data_by_time.values():
        for value in x:
            if value == 'No data':
                continue
            current_average.append(float(value))
        average = sumvalues(current_average)/len(current_average)
        averages.append(average)
        current_average.clear()

    return averages
    
def monthly_average(data, monitoring_station, pollutant):
    """Calculates the average for each month for the monitoring station and pollutant requested.
    
    Args:
        data is the dictionary with monitoring stations as keys and a pandas dataframe as values.
        monitoring _station is the station chosen, options: Harlington, Marylebone, Kensington. 
        pollutant is the type of pollution chosen, options: no, pm10, pm25.
    Returns:
        The calculated average for each month from the chosen monitoring station and pollutant for each day in a list.
    """
    
    current_average = []
    averages = []
    data[monitoring_station]['date'] = pd.to_datetime(data[monitoring_station]['date'])
    grouped = data[monitoring_station].groupby(data[monitoring_station]['date'].dt.month)[pollutant]
    data_by_date = {date: list(group) for date, group in grouped}

    for x in data_by_date.values():
        for value in x:
            if value == 'No data':
                continue
            current_average.append(float(value))
        average = meanvalue(current_average)
        averages.append(average)
        current_average.clear()

    return averages   

def peak_hour_date(data, date, monitoring_station, pollutant):
    """Finds the peak (highest) data value on the day chosen for the monitoring station and pollutant requested.
    
    Args:
        data is the dictionary with monitoring stations as keys and a pandas dataframe as values.
        date is the day in format 'YYYY/MM/DD' chosen.
        monitoring _station is the station chosen, options: Harlington, Marylebone, Kensington. 
        pollutant is the type of pollution chosen, options: no, pm10, pm25.
    Returns:
        The hour and value of the peak data value 
    """
    
    data_list = data[monitoring_station].values.tolist()
    current_values = []
    for i in data_list:
        if i[0] == date:
            if pollutant == 'no':
                if i[2] == 'No data':
                    continue
                current_values.append(float(i[2]))        
            elif pollutant == 'pm10':
                if i[3] == 'No data':
                    continue
                current_values.append(float(i[3]))
            elif pollutant == 'pm25':
                if i[4] == 'No data':
                    continue
                current_values.append(float(i[4]))        

    max_no = current_values[maxvalue(current_values)]

    for i in data_list:
        if i[2] == str(max_no):
            return i[1], i[2]
        else:
            text = 'No data for this day'
        return text

def count_missing_data(data, monitoring_station, pollutant):
    """Counts how many 'No data' values there are for the monitoring station and pollutant requested.
    
    Args:
        data is the dictionary with monitoring stations as keys and a pandas dataframe as values.
        monitoring _station is the station chosen, options: Harlington, Marylebone, Kensington. 
        pollutant is the type of pollution chosen, options: no, pm10, pm25.
    Returns:
        
    """
    
    data_list = data[monitoring_station][pollutant].to_list()
    counter = countvalue(data_list, 'No data')

    return counter

def fill_missing_data(data, new_value, monitoring_station, pollutant):
    """This function outputs a list of data from a chosen monitoring station and pollutant with all 'No data' values replaced with the chosen new value (new_value)"""

    data_list = data[monitoring_station].values.tolist() 
    replace_value = lambda x: [new_value if i == 'No data' else i for i in x]
    new_list = list(map(replace_value, data_list))
    if pollutant == 'no':
        extract = [[row[0], row[1], row[2]]for row in new_list]
        return extract
    elif pollutant == 'pm10':
        extract = [[row[0], row[1], row[3]]for row in new_list]
        return extract
    elif pollutant == 'pm25':
        extract = [[row[0], row[1], row[4]]for row in new_list]
        return extract


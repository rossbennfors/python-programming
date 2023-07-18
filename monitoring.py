# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification.
# 
# This module will access data from the LondonAir Application Programming Interface (API)
# The API provides access to data to monitoring stations. 
# 
# You can access the API documentation here http://api.erg.ic.ac.uk/AirQuality/help
#

import requests
import datetime
from pprint import pprint as pp
from utils import *

def get_live_data_from_api(site_code='BG2',species_code='NO',start_date=None,end_date=None):
    """
    Return data from the LondonAir API using its AirQuality API. 
    
    *** This function is provided as an example of how to retrieve data from the API. ***
    It requires the `requests` library which needs to be installed. 
    In order to use this function you first have to install the `requests` library.
    This code is provided as-is. 
    """
    import requests
    import datetime
    start_date = datetime.date.today() if start_date is None else start_date
    end_date = start_date + datetime.timedelta(days=1) if end_date is None else end_date
    
    
    endpoint = "http://api.erg.ic.ac.uk/AirQuality/Data/Site/SiteCode={site_code}/StartDate={start_date}/EndDate={end_date}/Json"
    
    url = endpoint.format(
        site_code = site_code,
        #species_code = species_code,
        start_date = start_date,
        end_date = end_date
    )
    
    res = requests.get(url)
    return pp(res.json())

def most_recent_value(site_code,species_code,start_date=None,end_date=None):
    """Your documentation goes here"""

    start_date = datetime.date.today() if start_date is None else start_date
    end_date = start_date + datetime.timedelta(days=1) if end_date is None else end_date
    # Set the API endpoint and any necessary parameters
    endpoint = 'http://api.erg.ic.ac.uk/AirQuality/Data/SiteSpecies/SiteCode={site_code}/SpeciesCode={species_code}/StartDate={start_date}/EndDate={end_date}/Json'
    url = endpoint.format(
        site_code = site_code,
        species_code = species_code,
        start_date = start_date,
        end_date = end_date
    )
    response = requests.get(url)
    data = response.json()['RawAQData']['Data']
    newest_val = 0
    for x in data:
        if x['@Value'] != '':
            newest_val = float(x['@Value'])
    if newest_val == 0:
        text = 'Sorry there is no data for this site/pollutant. Please try another one.'
        return text 
    return newest_val

def current_daily_average(site_code,species_code,start_date=None,end_date=None):
    """Your documentation goes here"""

    start_date = datetime.date.today() if start_date is None else start_date
    end_date = start_date + datetime.timedelta(days=1) if end_date is None else end_date
    # Set the API endpoint and any necessary parameters
    endpoint = 'http://api.erg.ic.ac.uk/AirQuality/Data/SiteSpecies/SiteCode={site_code}/SpeciesCode={species_code}/StartDate={start_date}/EndDate={end_date}/Json'
    url = endpoint.format(
        site_code = site_code,
        species_code = species_code,
        start_date = start_date,
        end_date = end_date
    )
    response = requests.get(url)
    data = response.json()['RawAQData']['Data']
    values = []
    for x in data:
        if x['@Value'] != '':
            values.append(float(x['@Value']))
    
    if len(values) == 0:
        text = 'Sorry there is no data for this site/pollutant. Please try another one.'
        return text

    return meanvalue(values)

def peak_data(site_code,species_code,start_date=None,end_date=None):
    """Your documentation goes here"""

    start_date = datetime.date.today() if start_date is None else start_date
    end_date = start_date + datetime.timedelta(days=1) if end_date is None else end_date
    # Set the API endpoint and any necessary parameters
    endpoint = 'http://api.erg.ic.ac.uk/AirQuality/Data/SiteSpecies/SiteCode={site_code}/SpeciesCode={species_code}/StartDate={start_date}/EndDate={end_date}/Json'
    url = endpoint.format(
        site_code = site_code,
        species_code = species_code,
        start_date = start_date,
        end_date = end_date
    )
    response = requests.get(url)
    data = response.json()['RawAQData']['Data']
    values = []
    for x in data:
        if x['@Value'] != '':
            values.append(float(x['@Value']))        
    
    max_no = values[maxvalue(values)]
    for i in data:
        if i['@Value'] == str(max_no):
            return i['@MeasurementDateGMT'][11:], i['@Value']
        else:
            text = 'Sorry there is no data for this site/pollutant. Please try another one.'
            return text

def rm_function_4(*args,**kwargs):
    """Your documentation goes here"""
    # Your code goes here


if __name__ == '__main__':
    GROUPNAME='London'
    pols = "http://api.erg.ic.ac.uk/AirQuality/Information/Species/Json"    
    info = pols.format(
    
    )
    species = []
    res = requests.get(info)
    group_info = res.json()['AirQualitySpecies']['Species']
    
    for x in group_info:
        species.append(x['@SpeciesCode'])
    print(pp(peak_data('BG2', 'NO2')))
    #print(get_live_data_from_api())
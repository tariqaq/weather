import requests
from prettytable import PrettyTable
from utils import *

API_KEY = "5c443b217be241e6b75175940230507"  # trq main acc

def searchCity(city):  # Returns closely matched names
    url = f"http://api.weatherapi.com/v1/search.json?key={API_KEY}&q={city}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    
    else:
        print(f"Could not find city data for '{city}'.")
        print(response.status_code)
        input('error.')
        return None
    
def formatSearch(rawSearchData):
    if len(rawSearchData) > 1:

        print("Did u mean:")
        for i, dict in enumerate(rawSearchData, start=1):
            print(f"{i} . {dict['name']} ({dict['country']})")

        choice = int(input("Enter choice: "))  # Get user input
        city = rawSearchData[choice-1]['name']  # Subtract 1 because list indices start at 0
        return city
    
    elif len(rawSearchData) == 1:
        city = rawSearchData[0]['name']
        return city
    
    else:
        print('Error: Search failed.')
        input('error.')
        return

def getCityData(city):  # Getting API response
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    
    else:
        print(f"Could not find weather data for '{city}'.")
        print(response.status_code)
        input('error.')
        return None
    
def weatherMain():
    weatherData = None
    usrCity = None
    rawSearchData = None
    
    usrCity = input('Enter the city : ')
    
    rawSearchData = searchCity(usrCity)
    searchedCity = formatSearch(rawSearchData)
    weatherData = getCityData(searchedCity)
    
    cls()
    
    print(f'---Weather Forecast---'.center(globalCenter))
    print(f'--{searchedCity}--'.center(globalCenter))
    
    # print(f"Condition: {weatherData['current']['condition']['text']}\n"
    #       f"Temperature: {weatherData['current']['temp_c']}°C\n"
    #       f"UV Index: {weatherData['current']['uv']}")
    
    table = PrettyTable()
    table.add_column('Condition', [weatherData['current']['condition']['text']])
    table.add_column('Temperature (°C)', [weatherData['current']['temp_c']])
    table.add_column('UV Index', [weatherData['current']['uv']])
    print(table)
import requests

API_KEY = "5c443b217be241e6b75175940230507"  # trq main acc

def search_city(city):  # Returns closely matched names
    url = f"http://api.weatherapi.com/v1/search.json?key={API_KEY}&q={city}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    
    else:
        print(f"Could not find city data for '{city}'.")
        print(response.status_code)
        return None

def get_weather_data(city):  # Getting API response
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    
    else:
        print(f"Could not find weather data for '{city}'.")
        print(response.status_code)
        return None
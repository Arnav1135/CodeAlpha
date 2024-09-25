import requests
import json

def get_weather(latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        'latitude': latitude,
        'longitude': longitude,
        'hourly': 'temperature_2m,precipitation',
        'current_weather': True, 
        'timezone': 'auto'  
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        weather_data = response.json()
        return weather_data
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")


latitude = 26.8467
longitude = 80.9462
weather = get_weather(latitude, longitude)
if weather:
    #print(weather) #uncomment to print JSON response object
    parsed_json = json.loads(json.dumps(weather))
    print("Current temperature " + str(parsed_json['current_weather']['temperature']) + "°C")
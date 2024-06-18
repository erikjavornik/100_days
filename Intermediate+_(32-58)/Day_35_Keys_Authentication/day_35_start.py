import requests
import os

#Sign-up and enter API key from OpenWeather
#Hides API keys in the environment for uploading code to public
# Windows command to see environment: 'dir Env:'
# Create environment variable: In terminal type 'export VAR_NAME=VALUE'
API_KEY = os.environ.get("OWM_API_KEY")
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
MY_LAT = 40.679597 # Your latitude
MY_LONG = -73.907776 # Your longitude

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["hourly"][0]["weather"][0]["id"])
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    # Get weather condition ID
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:   
    print("Bring an umbrella.")

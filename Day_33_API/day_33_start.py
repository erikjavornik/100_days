#Make request to API
import requests
from datetime import datetime

# #Only will give a response code and not the actual data
# #1XX Hold on, something is happening
# #2XX Here you go, everything was successful
# #3XX Go away, you don't have permission
# #4XX You screwed up, thing you are looking for doesn't exist
# #5XX I screwed up, sever messed up and is maybe down
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# #Will raise HTTPError if the HTTP request returned an unsuccessful status code.
# response.raise_for_status()

# longitude = response.json()["iss_position"]["longitude"]
# latitude = response.json()["iss_position"]["latitude"]

#API that requires inputs
MY_LAT = 40.679597
MY_LONG = -73.907776

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunrise.split("T")[1].split(":")[0])


time_now = datetime.now()

print(time_now.hour)
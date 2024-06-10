# App uses the Pixela API: Documentation- "https://docs.pixe.la/"
# Import modules
import requests
from datetime import datetime

# Constants for Pixela API
USERNAME = "YOUR USERNAME"
TOKEN = "YOUR SELF GENERATED TOKEN"
GRAPH_ID = "YOUR GRAPH ID"

# Set-up parameters to create a user for Pixela
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

## POST
## Creates a user, will fail if ran again with same username
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Set-up parameters to create the graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Reading Graph",
    "unit": "Pages",
    "type": "int",
    "color": "kuro"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

## Creates graph, not needed to run again
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Set up to create a pixel to be added to the graph
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# Get value for today's date
today = datetime.now()
# print(today.strftime("%Y%m%d"))

# Pixel parameters
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many pages did you read today? "),
}

# Post piece of data to the graph, if data already exists for today, then will fail
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "5"
}

## PUT
## Update data already in the graph
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)


delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"


## DELETE
## Remove data point from the graph
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
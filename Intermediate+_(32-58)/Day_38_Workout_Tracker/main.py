# Import Statements
import requests
import datetime

# Constants from Nutritionix API. Documentation: https://www.nutritionix.com/business/api 
# API Guide: https://docx.syndigo.com/developers/docs/nutritionix-api-guide
APP_ID = "App Id from Nutritionix"
API_KEY = "API key"

# Sheety API for adding to a Google Sheet. Documentation: https://sheety.co/docs
# Constants for Sheety API
USERNAME = "Username"
PROJECTNAME = "projectName"
SHEETNAME = "sheetName"

# Prompt user to write the exercises they did
user_input = input("Tell me which exercises you did: ")

# Nutritionix endpoint for Exercise 
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
# API requires verification
header = {
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY
}
# Required parameter by the API
body = {
    "query" : user_input
}

# Request.post using the header and body
response = requests.post(url=exercise_endpoint, json=body, headers=header)
result = response.json()
# print(result)

# Adding to Spreadsheet
sheet_endpoint = f"https://api.sheety.co/{USERNAME}/{PROJECTNAME}/{SHEETNAME}"
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# #Basic Authentication
# sheet_response = requests.post(
#     sheet_endpoint, 
#     json=sheet_inputs, 
#     auth=(
#         YOUR USERNAME, 
#         YOUR PASSWORD,
#     )
#     )

# #Bearer Token Authentication
# bearer_headers = {
# "Authorization": f"Bearer {YOUR_TOKEN}"
# }
# sheet_response = requests.post(
#     sheet_endpoint, 
#     json=sheet_inputs, 
#     headers=bearer_headers
# )

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    # No Authorization
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    print(sheet_response.text)
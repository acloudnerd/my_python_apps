import requests
from datetime import datetime 
import os
from dotenv import load_dotenv

ENDPOINT = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/901906ea70c3a57fdbeee98a6e24dbe9/tshepoMyWorkouts/workouts"
GENDER = "male"
WEIGHT = 64
HEIGHT = 1.86
AGE = 27


load_dotenv()

APP_ID  = os.environ["NUTRITIONIX_APP_ID"]
API_KEY = os.environ["NUTRITIONIX_API_KEY"]
USERNAME = os.environ["SHEETY_USERNAME"]
PSWD = os.environ["SHEETY_PASSWORD"]
 

input_text = input("What exercise(s) did you do? ")

headers = {
    "x-app-key": API_KEY,
    "x-app-id": APP_ID,
}

params = {
    "query": "indoor run for 10 mins",
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(url=ENDPOINT, json=params, headers=headers)
result = response.json()
print(result)

current_date = datetime.now().strftime("%d/%m/%Y")
now = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheety_inputs = {
        "workout":{
            "date": current_date,
            "time" : now,
            "exercise": exercise["name"].title(),
            "durations": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }


    # basic auth
    
    sheety_response = requests.post(SHEETY_ENDPOINT, json=sheety_inputs,
                                    auth=(USERNAME, PSWD))
    sheety_results = sheety_response.json()
    print(sheety_results)






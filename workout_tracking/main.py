import requests

APP_ID = "app_6cd52af399ef4d85886b3c6c"
API_KEY = "nix_live_ppY1AWVdoHzqQQzSKHGSntg1NBR1uiTW"
ENDPOINT = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
# SHEET_ENDPOINT = 
GENDER = "male"
WEIGHT = 64
HEIGHT = 1.86
AGE = 27


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

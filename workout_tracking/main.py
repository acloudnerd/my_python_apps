import requests

APP_ID = "app_6cd52af399ef4d85886b3c6c"
API_KEY = "nix_live_ppY1AWVdoHzqQQzSKHGSntg1NBR1uiTW"
ENDPOINT = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

headers = {
    "x-app-key": API_KEY,
    "x-app-id": APP_ID,
}

params = {
    "query": "indoor run for 10 mins",
    "gender": "male"
}

response = requests.post(url=ENDPOINT, headers=headers)

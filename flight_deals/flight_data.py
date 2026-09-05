import requests
from dotenv import load_dotenv
import os
from datetime import date, timedelta

load_dotenv()

class FlightData:
    #This class is responsible for structuring the flight data.
    FLIGHT_API = "https://serpapi.com/search"

    def __init__(self):
        self.api_key = os.environ["API_KEY"]

    def get_flight_data(self):
        outbound_date = (date.today() + timedelta(days=30)).isoformat()
        return_date = (date.today() + timedelta(days=37)).isoformat()

        params = {
            "engine": "google_flights",
            "departure_id": "CDG",
            "arrival_id": "AUS",
            "outbound_date": outbound_date,
            "return_date": return_date,
            "api_key": self.api_key,
        }

        response = requests.get(self.FLIGHT_API, params=params)
        response.raise_for_status()

        return response.json()
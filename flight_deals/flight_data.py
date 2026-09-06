import requests
from dotenv import load_dotenv
import os
from datetime import date, timedelta

load_dotenv()

class FlightData:
    #This class is responsible for structuring the flight data.
    FLIGHT_API = "https://serpapi.com/search"

    def __init__(self):
        self.api_key = os.environ["SERP_API_KEY"]

    def get_flight_data(self, origin_city_cd, destination_city_cd, out_date, return_date):

        params = {
            "engine": "google_flights",
            "departure_id": origin_city_cd,
            "arrival_id": destination_city_cd,
            "outbound_date": out_date,
            "return_date": return_date,
            "api_key": self.api_key,
        }

        response = requests.get(self.FLIGHT_API, params=params)
        response.raise_for_status()

        return response.json()
    
def find_cheapest_flight(data, return_date):
        all_flights = data.get("best_flights", []) + data.get("other_flights", [])
        if not all_flights:
            print("No flight data available")
            return None
        else:
            cheapest_flight = min(all_flights, key=lambda flight: flight["price"])
            return cheapest_flight
            
        
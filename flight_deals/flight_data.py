import requests
from dotenv import load_dotenv
import os
from datetime import date, timedelta

load_dotenv()

class FlightData:
    #This class is responsible for structuring the flight data.
    FLIGHT_API = "https://serpapi.com/search"

    def __init__(self, price=None, origin_airport=None, destination_airport=None, out_date=None, return_date=None):
        self.api_key = os.environ["SERP_API_KEY"]
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date

    def get_flight_data(self):

        params = {
            "engine": "google_flights",
            "departure_id": self.origin_airport,
            "arrival_id": self.destination_airport,
            "outbound_date": self.out_date,
            "return_date": self.return_date,
            "api_key": self.api_key,
        }

        response = requests.get(self.FLIGHT_API, params=params)
        response.raise_for_status()

        return response.json()
    
def find_cheapest_flight(data, return_date):
    all_flights = data.get("best_flights", []) + data.get("other_flights", [])

    cheapest = None
    for flight in all_flights:
        try:
            price = flight["price"]
        except KeyError:
            # Some flights come back without a price. Skip them.
            continue
        if cheapest is None or price < cheapest["price"]:
            cheapest = flight

    if cheapest is None:
        print("No flight data available")
        return FlightData(
            price="N/A",
            origin_airport="N/A",
            destination_airport="N/A",
            out_date="N/A",
            return_date="N/A",
        )

    origin_airport = cheapest["flights"][0]["departure_airport"]["id"]
    destination_airport = cheapest["flights"][-1]["arrival_airport"]["id"]
    out_date = cheapest["flights"][0]["departure_airport"]["time"].split(" ")[0]

    return FlightData(
        price=cheapest["price"],
        origin_airport=origin_airport,
        destination_airport=destination_airport,
        out_date=out_date,
        return_date=return_date,
    )

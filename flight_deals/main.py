#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests_cache
from data_manager import DataManager
from flight_data import FlightData, find_cheapest_flight
from datetime import date, timedelta


# set the dates
tdy = date.today()
tomorrow = (tdy + timedelta(days=1)).isoformat()
six_months_from_today = (tdy + timedelta(weeks=24)).isoformat()



data_manager = DataManager()
sheet_data = data_manager.get_data()["prices"]
destination = sheet_data[0]  # CDG / Paris is the first row in the spreadsheet

flight_data = FlightData(origin_airport="LHR", destination_airport=destination["iataCode"], out_date=tomorrow, return_date=six_months_from_today)
data = flight_data.get_flight_data()

cheapest_flight = find_cheapest_flight(data, return_date=six_months_from_today)

print(f"{destination['city']}: GBP {cheapest_flight.price}")

if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
    print(f"Lower price flight found to {destination['city']}!")
    data_manager.update_lowest_price(row_id=destination["id"], new_price=cheapest_flight.price)
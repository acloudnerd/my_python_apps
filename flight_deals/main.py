#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import json
import requests_cache
from data_manager import DataManager
from flight_data import FlightData, find_cheapest_flight
from datetime import date, timedelta


# set the dates
tdy = date.today()
tomorrow = (tdy + timedelta(days=1)).isoformat()
six_months_from_today = (tdy + timedelta(weeks=24)).isoformat()
# print(six_months_from_today)

flight_data = FlightData()
data = flight_data.get_flight_data(origin_city_cd="LHR", destination_city_cd="CDG", out_date=tdy, return_date=six_months_from_today)

# data_manager = DataManager()
# data = data_manager.get_data()

# print(json.dumps(data, indent=2))

print(find_cheapest_flight(data, return_date=six_months_from_today))
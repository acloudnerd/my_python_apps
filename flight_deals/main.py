#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_data import FlightData

flight_data = FlightData()
data = flight_data.get_flight_data()

# data_manager = DataManager()
# data = data_manager.get_data()

print(data)
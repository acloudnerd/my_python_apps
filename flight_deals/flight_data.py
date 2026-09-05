import requests

class FlightData:
    #This class is responsible for structuring the flight data.
    FLIGHT_API = "https://serpapi.com/search?engine=google_flights"
    
    
    def get_flight_data():
    
        params = {"departure_id": "CDG", "arrival_id": "AUS"}
        
        response = requests.get(self.FLIGHT_API, params=params)
        
        return response.json()
import requests
import os
from dotenv import load_dotenv

load_dotenv()

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    SHEETY_ENDPOINT = ("https://api.sheety.co/901906ea70c3a57fdbeee98a6e24dbe9/"
                       "tshepoFlightDeals/prices"
    )
 
    
    def __init__(self):
        self.username = os.environ["SHEETY_USERNAME"]
        self.password = os.environ["SHEETY_PASSWORD"]
    
    def get_data(self):
        response = requests.get(
            self.SHEETY_ENDPOINT, 
            auth=(self.username, self.password)
            )
            
        response.raise_for_status()
        
        return response.json()
    
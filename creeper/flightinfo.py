#-*- coding: utf-8 -*-
# python 3.7.2

import requests
import time, random
import re

class FlightInfo():
    def __init__(self):
        self.session = requests.session() # download mechine
        # https://flights.ctrip.com/itinerary/roundtrip/sha-syx?date=2020-03-23%2C2020-03-26
        # https://flights.ctrip.com/itinerary/oneway/sha-syx?date=2020-03-23
        self.url = ''
    
    def get_price(self, fromcode, tocode, date):
        pass


if __name__ == '__main__':
    flightinfo = FlightInfo()
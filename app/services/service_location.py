from decouple import config
from fastapi.responses import JSONResponse
import json

class LocationService:
    def __init__(self):
        self.api_province = config("API_PROVINCE")
        self.api_country = config("API_COUNTRY")

    def province(self):
        data = json.load(open(self.api_province, encoding='utf-8'))
        return data

    def country(self):
        data = json.load(open(self.api_country, encoding='utf-8'))
        obj = {'name': 'sonny','age': 28}
        return data
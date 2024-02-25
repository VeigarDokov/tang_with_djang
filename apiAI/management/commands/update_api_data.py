# """API"""
# from django.core.management.base import BaseCommand
# import json
# import requests
# 
# 
# class Command(BaseCommand):
#     """fatch api for crypto prices"""
# 
#     help = "Fatch data from API and update api_data.json"
# 
#     def handle(self, *args, **kwargs):
#         headers = {
#             "X-CMC_PRO_API_KEY": "2239c60e-d1bf-4be8-8158-882ac87d5c9f",
#             "Accepts": "application/json",
#         }
#         params = {
#             "start": "1",
#             "limit": "60",
#             "convert": "USD",
#         }
#         url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
#         response = requests.get(url, params=params, headers=headers)
#         data = response.json()
# 
#         with open("api_data.json", "w") as f:
#             json.dump(data["data"], f)
# 
#         self.stdout.write(self.style.SUCCESS("API data updated successfully"))


# update_api_data.py
import os
from django.core.management.base import BaseCommand
import json
import requests


class Command(BaseCommand):
    help = "Fetch data from API and update api_data.json"

    def handle(self, *args, **kwargs):
        headers = {
            "X-CMC_PRO_API_KEY": "2239c60e-d1bf-4be8-8158-882ac87d5c9f",
            "Accepts": "application/json",
        }
        params = {
            "start": "1",
            "limit": "60",
            "convert": "USD",
        }
        url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
        response = requests.get(url, params=params, headers=headers)
        data = response.json()


        file_path = os.path.join(os.path.dirname(__file__), 'api_data.json')
        print(file_path)
        with open(file_path, "w") as f:
            json.dump(data["data"], f)

        self.stdout.write(self.style.SUCCESS("API data updated successfully"))


Command().handle()

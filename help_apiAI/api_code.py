#!/home/veigar/Desktop/API-s/lpp3ed/bin/python
import os
import json
import requests

os.chdir('/home/veigar/Desktop/API-s/btcapi/apiAI')

headers = {
    'X-CMC_PRO_API_KEY': '2239c60e-d1bf-4be8-8158-882ac87d5c9f',
    'Accepts': 'application/json',
}

params = {
    'start': '1',
    'limit': '60',
    'convert': 'USD',
}

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
response = requests.get(url, params=params, headers=headers)
data = response.json()


with open('api_data.json', 'w') as f:
    json.dump(data['data'], f)

print('executed')

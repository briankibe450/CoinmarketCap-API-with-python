from requests import Request, Session
import json 

url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'
parameter = {
    'slug':'bitcoin'
    'convert':'USD'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '755c83a4-1e9c-473b-99f6-bfec85be4b22'
}

session = Session()
session.headers.update(headers)
response = session.get(url, params=parameter)
print(response.text)
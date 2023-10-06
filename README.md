# CoinmarketCap-API-with-python
Install the requests library using pip if it's not already installed.
Obtain an API Key:

Sign up for a CoinMarketCap account if you don't have one.
Generate an API key from your CoinMarketCap account settings. You'll need this key to access the API.
Define API Endpoint:

CoinMarketCap provides an API endpoint for cryptocurrency data. Set the endpoint to 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'.
Set API Parameters:

Specify the parameters for your API request:
'symbol': 'BTC' to request data for Bitcoin.
'convert': 'USD' to convert the price to US Dollars.
Include API Key in Headers:

Create a dictionary for the headers of your API request and include your API key as 'X-CMC_PRO_API_KEY'.
Make the API Request:

Use the requests.get() function to send the API request to the defined endpoint with the specified parameters and headers.
Handle the Response:

Check the response status code to ensure it's 200 (indicating a successful request).
Parse the JSON response to extract the Bitcoin data.
Store the Data in a JSON File:

Define the name of the JSON file where you want to store the data, for example, 'bitcoin_data.json'.
Use the json.dump() method to write the Bitcoin data to the JSON file. This data will typically include information like the current price, market cap, volume, and more.

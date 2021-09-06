import json
from os import getenv

import requests
from dotenv import load_dotenv

# Load env-vars (from .env or system variables)
load_dotenv()

ZENVEST_API_BASE_URL = getenv('ZENVEST_API_BASE_URL')
ZENVEST_API_KEY = getenv('ZENVEST_API_KEY')

# Only supports NYSE, NASDAQ and AMEX
EXCHANGE = 'NYSE'

if __name__ == '__main__':
    api_response = requests.get(f'{ZENVEST_API_BASE_URL}/data/tickers?exchange={EXCHANGE}&api-key={ZENVEST_API_KEY}')
    data = json.loads(api_response.text)
    # Do whatever yoy want with the data
    print(data)

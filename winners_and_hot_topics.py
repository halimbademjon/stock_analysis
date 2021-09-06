import json
from os import getenv

import requests
from dotenv import load_dotenv

# Load env-vars (from .env or system variables)
load_dotenv()

ZENVEST_API_BASE_URL = getenv('ZENVEST_API_BASE_URL')

if __name__ == '__main__':
    api_response = requests.get(f'{ZENVEST_API_BASE_URL}/data/hot')
    data = json.loads(api_response.text)
    # Do whatever you want with the data
    print(data)

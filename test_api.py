import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('WCI_API_KEY')

url = f"https://www.worldcoinindex.com/apiservice/json?key={api_key}&fiat=USD&label=btcusd-ethusd"
res = requests.get(url)
print(res.status_code)
print(res.json())
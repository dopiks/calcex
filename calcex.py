
import requests
from keys import *

url = "http://data.fixer.io/api/latest?access_key=" + API_KEY + "&symbols=USD,CAD,JPY,ILS"

headers = {}

response = requests.request("GET", url, headers=headers)

print(response.text)

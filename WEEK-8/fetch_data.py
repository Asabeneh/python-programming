'''
numpy, pandas, matplotlib, scipy, requests

'''
from pprint import pprint
import requests
def fetch_data(url):
    response = requests.get(url)
    data = response.json()
    return data
# cats_api_url = 'https://api.thecatapi.com/v1/breeds'
# pprint(fetch_data(cats_api_url))

# countries_data_url = 'https://studies.cs.helsinki.fi/restcountries/api/all'
# pprint(fetch_data(countries_data_url))



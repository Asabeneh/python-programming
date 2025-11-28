from fetch_data import fetch_data
from generate_json import generate_json
from pprint import pprint

cats_api_url = 'https://api.thecatapi.com/v1/breeds'

cats = fetch_data(cats_api_url)
minified_cats = [{
    'name': cat['name'],
    'origin':cat['origin'],
    'description':cat['description'],
    'life_span':cat['life_span'],
    'weight':cat['weight']
    } for cat in cats]
# pprint(minified_cats)
generate_json(minified_cats, 'cats.json')

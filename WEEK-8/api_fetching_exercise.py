from fetch_data import fetch_data
from pprint import pprint
cats_api_url = 'https://api.thecatapi.com/v1/breeds'
cats = fetch_data(cats_api_url)


def create_freq_table(data):
    origins = [cat['origin'] for cat in data]
    freq_table = {}
    for origin in origins:
        if origin in freq_table:
            freq_table[origin] = freq_table[origin] + 1
        else:
            freq_table[origin] = 1
    items = freq_table.items()
    sorted_items = sorted(items, key=lambda item: item[1],  reverse=True)
    for item in sorted_items:
        key, value = item
        print(f'{key} - {value}')
 

def find_average_cat_life_span(data):
    cats_life_spans = []
    for cat in data:
        lowest, highest = cat['life_span'].split(' - ')
        average = (int(lowest) + int(highest)) / 2
        cats_life_spans.append(average)
    n = len(cats_life_spans)
    total = sum(cats_life_spans)
    mean = total / n 
    return mean


countries_data_url = 'https://studies.cs.helsinki.fi/restcountries/api/all'

countries = fetch_data(countries_data_url)
populations = [country['population'] for country in countries]
world_population = f'{sum(populations):,}'
print(world_population)

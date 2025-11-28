from countries_data import data 
from pprint import pprint 

# for country in data:
#     print(country['name'], country['capital'], country['population'])

def calculate_world_population():
    total = 0
    for country in data:
        population = country['population']
        total  = total + population
    return "{:,}".format(total)

print(calculate_world_population())

def find_ten_most_populated_countries():
   
    lst = []
    sorted_data = sorted(data, key = lambda country:country['population'], reverse=True)[:10]
    for country in sorted_data:
        dct = {}
        dct['name']  = country['name']
        dct['capital'] = country['capital']
        dct['population'] = country['population']
        lst.append(dct)
    return lst
    
pprint(find_ten_most_populated_countries())

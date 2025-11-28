from pprint import pprint
def read_json(filename):
    import json
    with open(filename, encoding='utf-8') as f:
        data = json.load(f)
        return data


"""
The cats json file has quite a lot of information and if process it we may get some insight about cats.
1. Let find the average weight of cat using the file
2. What is the life span of cat?
3. Origin, descption, 
4. Transform the data
"""

cats = read_json('cats.json')
number_of_cats = len(cats)
weights_all = []
for cat in cats:
    weights = cat['weight']['metric'].split(' - ')
    lowest = int(weights[0])
    heighest = int(weights[1])
    avg = (lowest + heighest) / 2
    weights_all.append(avg)


total_average = sum(weights_all) / number_of_cats
print(round(total_average, 2))

# Average life span
years = []
for cat in cats:
    life_span = cat['life_span'].split(' - ')
    lowest = int(life_span[0])
    heighest = int(life_span[1])
    avg = (lowest + heighest) / 2
    years.append(avg)

average_life_span = sum(years) / number_of_cats
print(round(average_life_span, 2))

# What is the maximum life span of cat?
# What is the minumum life span of cat
# What is the maximum weight of the cat
# What is the minum weight of the cat 

lst = []
for cat in cats:
    name = cat['name']
    origin = cat['origin']
    description = cat['description']
    dct = {
        'name':name ,
        'origin': origin,
        'description':description
    }
    lst.append(dct)
pprint(lst)
import json
def create_json_file(filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(lst, f, ensure_ascii=False, indent=4)

# create_json_file('tranformed-cat.json')
        



table  = {

}
for cat in cats:
    name = cat['name']
    origin = cat['origin']
    filtered_cats = list( filter(lambda c: c['origin'] == origin, cats))
    if origin not in table:
        table[origin] = len(filtered_cats)

print(len(cats))
print('Origin and number of cats')
pprint(table)

    

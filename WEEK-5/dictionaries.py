'''
Dictionaries: key value pair 

'''
from pprint import pprint
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'country':'Finland',
    'city':'Helsinki',
    'age':250,
    'is_married':True,
    'height':1.72,
    'weight': 75.5,
    'skills':['HTML','CSS', 'JavaScript','React','Python'],
    'address': {
         'zipcode':'02270',
         'street_name':'Space street'
     }
}

print(type(person))
print(len(person))
print(person['first_name'], person.get('first_name'))
print(person['last_name'], person.get('last_name'))

person['nationality'] = 'Ethiopian'

if 'nationality' in person:
    print(person['nationality'])
print(person.get('nationality'))
# print(person['nationality'])
person['skills'].append('MySQL')
person['age']  = 55
person['height'] = 1.85
pprint(person)

print({}, dict())
print('hobby' in person)
print('nationality' in person)

person.pop('age')

pprint(person)

person.popitem()
pprint(person)
del person['address']

pprint(person)

print(list(person))
pprint(person.items())

items = person.items()
print('Items:', items)
for item in items:
    key = item[0]
    value = item[1]
    print('key:', key, 'value:', value)
   
    

print(person)
# person_copy = {**person}
person_copy = person.copy()

person_copy['first_name'] = 'John'
person_copy['last_name'] = 'Doe'
pprint(person_copy)
pprint(person)

keys = person.keys()
print(keys)
values = person.values()
print(values)

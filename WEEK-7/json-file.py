import json 

person_json = '''{
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}'''

# changing JSON to dictionary

print(type(person_json))
person_dct = json.loads(person_json)
print(type(person_dct))


person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}

person_json = json.dumps(person, indent=2)
print(person_json)

import json
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
persons = [
    {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
},
{
    "name": "John",
    "country": "Finland",
    "city": "Stockholm",
    "skills": ["JavaScrip", "React", "Python"]
},
{
    "name": "Paul",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
]
def create_json_file(filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(persons, f, ensure_ascii=False, indent=4)

# create_json_file('./json_example.json')
        
from pprint import pprint
""" with open('cats.json', encoding='utf-8') as f:
    data = json.load(f)
    pprint(data) """

def read_json(filename):
    with open(filename, encoding='utf-8') as f:
        data = json.load(f)
        return data
read_json('cats.json')

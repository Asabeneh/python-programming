import json
# JSON
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''
print(type(person_json))
# let's change JSON to dictionary
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])



# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"],
    "is_married":True,
     "age":250,
     "height":1.73
}
# let's convert it to  json
person_json = json.dumps(person, indent=2) # indent could be 2, 4, 8. It beautifies the json
print(type(person_json))
print(person_json)


import json
# python dictionary
# person = {
#     "name": "Asabeneh",
#     "country": "Finland",
#     "city": "Helsinki",
#     "skills": ["JavaScrip", "React", "Python"]
# }
students = [
    {
        "id": 1,
        "name": "Asab",
        "country": "Finland",
        "gender": "Male",
    },
    {
        "id": 2,
        "name": "Eelon",
        "country": "Finland",
        "gender": "Male"
    },
    {
        "id": 3,
        "name": "Kinta",
        "country": "Sweden",
        "gender": "Female"
    }
]
with open('./students.json', 'w', encoding='utf-8') as f:
    json.dump(students, f, indent=4)
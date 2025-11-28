'''
Numbers(int, float, complex)
Strings
Booleans (True and False)
List  [1, 2, 3]
Tuple (1, 2, 3)
Set {1, 2, 3, 3}
Dictionary {'key':'value'}
'''

# Numbers
print(-3, -2, -1, 0, 1,  2, 3, type(-3), type(10))
print(3.14, 9.81, 2.77, 37.6, type(3.14), type(9.81))
print(1 + 2j, 3 - 4j, 1j, type(1 + 2j))

# Booleans: True or False
print(True, type(True))
print(False,type(False))
print(4 > 3)
print(4 == 4)

# Strings - textual data

print('a')
print('love')
print('I love peopole and if what else can I love')
print('''Python is a high-level programming language for general-purpose programming. It is an open source, interpreted, objected-oriented programming language. Python was created by a Dutch programmer, Guido van Rossum. The name of the Python programming language was derived from a British sketch comedy series, Monty Python's Flying Circus. 
'''.split())

# List
print(['Milk','Honey','Sugar','Potatoes','Avocado'])
print(['Kinta','Ahmed','Jyoti','Eelon','Blake']) # are mutables or modifiable
print(type(['Kinta','Ahmed','Jyoti','Eelon','Blake']))

# Tuple

print((1, 2, 3), type((1, 2, 3)))

# Set  - we use curly bracket to to make a set {1, 2, 3, 'dkdkdk', 'my', }
print({1, 2, 3, 4, 4, 5}, len({1, 2, 3, 4, 4, 5})) 

# Dictionary
print({'kirja':'book','talo':'house','auto':'car'})
print({
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'country':'Finland',
    'is_married':True,
    'city':'Helsinki',
    'skills':['HTML','CSS','Python','MySQL'],
    'educations':[
        {
            'field':'Information Technology',
            'degree':'Master',
            'started_year':'August 2020',
            'ending_year':'August 2024'
             
        },
        {
            'field':'Information Technology',
            'degree':'Master',
            'started_year':'August 2020',
            'ending_year':'August 2024'
             
        },
        {
            'field':'Information Technology',
            'degree':'Master',
            'started_year':'August 2020',
            'ending_year':'August 2024'
             
        }
    ]
    
    
})


'''
variables are storage, they store data

'''

num1 = 4
num2 = 3

total  = num1 + num2

first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsink'
age = 250
is_married = True
skills = ['Python','Databases','Node']
height = 1.73
mass = 76
gravity = 9.81

fullname = first_name + ' ' + last_name
print(fullname)
print(f'I am {fullname}. I live in {country}, {city}. I am {age} years old.')


weight = mass * gravity 
print(round(weight, 2))

bmi = mass / height ** 2
print(round(bmi, 2))


length = 40
width = 60
# area of rectangle = length * width 

# radius 50 and 3.14 for pi, area = pi * radius * radius


'''
- Builtin functions: print(),len(), str(), int(), float(), round(), input(), etc
- Custom functions
'''

'''
What is a function? 
It is a block of code that solve a certain problem

- name 
- declare
- call 

'''

def do_somthing(activity, place, time):
    return f'I am {activity} in {place} at {time}.'


print(do_somthing('teaching', 'Helsinki','17:30'))
print(do_somthing('studying', 'Espoo', '14:30'))
print(do_somthing('running', 'stadium', '08:30'))

'''
A function that change a number to its square
n > n * n => n ** 2

'''

def make_square(n):
    return n * n

    
print(make_square(3))
print(make_square(5))
print(make_square(10))

'''
The name of the function is add_two_num and it takes two parameters and returns the sum of these two numbers.


'''

def add_two_nums(x, y):
    return x + y

print(add_two_nums(10, 90))
print(add_two_nums(-20, -10))

'''

Calculate weight of body 
weight = mass * gravity 

The name of the function is calcualte_weight which takes two parameters: mass and gravity and it returns the weight.

'''

def calcualte_weight(mass, gravity = 9.81):
    weight = mass * gravity
    return round(weight, 2)
    
print(calcualte_weight(75.5))
print(calcualte_weight(75.5, 1.625))
print(calcualte_weight(85.5))
print(calcualte_weight(75.5, 3.73))


'''

'''
print(calcualte_weight(75.5, 1.625))


def calcuate_weight_from_gravities():
    mass = 75.5
    gravitational_forces = [9.81, 1.62, 3.73]
    for gravity in gravitational_forces:
        weight = round(gravity * mass, 2)
        print(f'The weight of the body with mass {mass} for {gravity} is {weight}')
# calcuate_weight_from_gravities()


'''
filter_countries_with_land() and it should return list of countries contain the word land

'''
from countries import countries

def filter_countries_with_land():
    countries_with_land = []
    for country in countries:
        if 'land' in country:
            countries_with_land.append(country)
    return countries_with_land

# print(filter_countries_with_land())


'''
filter_countries_by_starting_letter
'''


def filter_countries_by_starting_letter(starting_letter):
    new_lst = []
    for country in countries:
        if country.startswith(starting_letter):
            new_lst.append(country)
    return new_lst

print(filter_countries_by_starting_letter('E'))

# Denmark, Dominican republic, 
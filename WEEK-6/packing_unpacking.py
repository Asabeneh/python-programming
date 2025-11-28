def sum_all_nums(*args):
    print(args)
    return sum(args)

    
print(sum_all_nums(1, 2, 3, 4, 5, 6, 7, 8, 9))
print(sum_all_nums(100, 350, 550))

nums  = (1, 2, 3)
first, second, third = nums
print(first)
print(second)
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fi, sw, _, *rest = countries 
print(fi, sw, rest)

def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'
dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
print(unpacking_person_info(**dct)) # Asabeneh lives in Finland, Helsinki. He is 250 years old.

def packing_params(**kwargs):
    print(kwargs)
    for key in kwargs:
        print(key, kwargs[key])
    

packing_params(country ='Finland', city='Helsinki', population = '6M')

nums = [1, 2, 3, 4, 5]
print(max(*nums))

countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
for i in range(len(countries)):
    print(f"{i + 1} - {countries[i]}")
 
print('========= Enumerate ============')   
for item in enumerate(countries):
    index, country = item
    print(f"{index + 1} - {country}")
    
    
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
print(list(zip(fruits, vegetables)))
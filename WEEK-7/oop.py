from datetime import datetime
class Person():
    def __init__(self, first_name, last_name, country, birth_year):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.birth_year = birth_year
        
    def get_age (self):
        now = datetime.now()
        current_year = now.year 
        age = current_year - self.birth_year
        return age
    def get_person_info(self):
        age = self.get_age()
        return f'He is {self.first_name} {self.last_name}. He is from {self.country}. He is {age} years old.'
    
        
        
        
p1 = Person('Asab','Yeta','Finland', 1925)
p2 = Person('Donald','Trump','United States', 1946)
print(p1.first_name)
print(p1.last_name)
print(p1.country)
print(p1.get_person_info())
print('===== Person 2 ====')
print(p2.first_name)
print(p2.last_name)
print(p2.country)
print(p2.get_person_info())

# 

class Student(Person):
    def __init__(self, first_name, last_name, country, birth_year, gender):
        self.gender = gender
        super().__init__(first_name, last_name, country, birth_year)
        self.skills = []
    def get_person_info(self):
        age = self.get_age()
        pronoun = 'He' if self.gender == 'Male' else 'She'
        skill_count = len(self.skills)
        
        expression = f'has {skill_count} skills' if skill_count > 0 else ''
        
        return f'{pronoun} is {self.first_name} {self.last_name}. {pronoun} is from {self.country}. {pronoun} is {age} years old. {pronoun} {expression}.'
    def add_skill(self, skill):
        self.skills.append(skill)
    
    
    
s1 = Student('John','Doe','UK', 1990,'Male' )
s2 = Student('Marta','Robert','UK', 1995,'Female' )
print(s1.first_name)
print(s1.get_person_info())
print(s2.get_person_info())
s1.add_skill('Python')
s1.add_skill('Databases')
s1.add_skill('ML')
print(s1.skills)
print(s1.get_person_info())
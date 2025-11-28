# How create class in Python

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age 
    def get_person_info(self):
        return f'He is {self.first_name} {self.last_name}. He is {self.age} years old.'
        
        

p1 = Person('Asab', 'Yeta', 250)
p2 = Person('Donald', 'Trump', 80)
p3 = Person('Martha','Robert', 21)
print(p1.first_name)
print(p1.first_name, p1.last_name, p1.age)
print(p1.get_person_info())
print(p2.get_person_info())
print(p3.get_person_info())

class Student(Person):
    def __init__(self, first_name, last_name, age, country, gender):
        super().__init__( first_name, last_name, age)
        self.country = country
        self.gender = gender
        self.skills = []
    def add_skill(self, skill):
        self.skills.append(skill)
    def get_skills(self):
        return self.skills
    def get_person_info(self):
        pronoun = 'He' if self.gender == 'Male' else 'She'
        skill_count = len(self.skills)
        skill =  f'{pronoun} has {skill_count} skills 'if skill_count > 0 else ''
        return f'{pronoun} is {self.first_name} {self.last_name}. {pronoun} is {self.age} years old. {skill}'
        


s1 = Student('John','Doe', 21,'Sweden','Male')
s2 = Student('Martha','Robert', 21,'Finland','Female')
print(s1.first_name)
s1.add_skill('Python')
s1.add_skill('Data Analysis')
print(s1.skills)
print(s1.get_person_info())
print(s2.get_person_info())




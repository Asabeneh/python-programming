'''
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
animal_products = ('Milk','Meat', 'Cheese', 'Yoghurt')

'''
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
animal_products = ('Milk','Meat', 'Cheese', 'Yoghurt')

food_stuff = fruits + vegetables + animal_products

print(food_stuff)
print(len(food_stuff))

middle_index = len(food_stuff) // 2
print(food_stuff[middle_index])

'''
I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.

'''

sentence = 'I am a teacher and I love to inspire and teach people.'.replace('.', '').lower()
words = sentence.split()

print(sentence)
print(words, len(words))
unique_words = set(words)
print(unique_words, len(unique_words))

'''
'You cannot end a sentence with because because because is a conjunction'
'''
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because')) # to get the first occurrence
print(sentence.rfind('because')) # last occurrence
length_of_word = len('because')  # including the remaining character by using the string length
start = sentence.find('because')
end = sentence.rfind('because') + length_of_word
print(sentence[start:end]) # string slicing
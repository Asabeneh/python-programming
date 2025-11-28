import requests
from pprint import pprint
url = 'https://api.thecatapi.com/v1/breeds'
import json
import re

# get request

response = requests.get(url)
data = response.json()

# function programming, list comphres, regular loop

""" for cat in data:
    print('------')
    print(cat['origin'], cat['name'], cat['life_span']) """
    

def find_average_life_span():
    ages = []
    for cat in data:
        lowest, highest = cat['life_span'].split(' - ')
        average = (int(lowest) + int(highest)) / 2
        ages.append(average)

    average_life_span_cats = round(sum(ages) / len(ages), 2)
    return average_life_span_cats

def find_weight():
    weights = []
    for cat in data:
        lowest, heighest = cat['weight']['metric'].split(' - ')
        average = (int(lowest) + int(heighest)) / 2
        weights.append(average)
    print(weights)
    average_cat_weight = round(sum(weights) / len(weights), 2)
    return average_cat_weight

def clean_text():
    txt = ''
    for cat in data:
        txt += cat['description']
    pattern = r'[^a-zA-Z0-9 ]'
    cleaned_txt = re.sub(pattern, ' ', txt).lower()
    return cleaned_txt

def generate_word_cloud():
    from wordcloud import WordCloud, STOPWORDS
    import matplotlib.pyplot as plt
    import numpy as np
    cleaned_text = clean_text()
    wordcloud = WordCloud(width = 800, height = 800,
                    background_color ='white',
                    stopwords = STOPWORDS,
                    min_font_size = 10).generate(cleaned_text)
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud)
    plt.savefig('cat_words.png')
    # plt.axis("off")
    # plt.tight_layout(pad = 0)
    plt.show()

generate_word_cloud()




comments = [
    'I love people', 'I love programming', 'I do not like to do it again', 'It is not a very good course', 'I just love it', 'I am at cloud nine.'
    'satisfied', 'worried but optimistic', 'I recently completed the "Mastering Python" course, and I must say, it was a transformative experience. As someone with only a basic understanding of programming, I was initially apprehensive about the complexity of learning Python. However, the course was a revelation in terms of its structure, content, and teaching methodology.', """Firstly, the course was incredibly well-organized. The modules were structured logically, starting from the very basics of Python and gradually progressing to more advanced concepts. This gradual build-up was crucial for me, as it allowed me to solidify my understanding at each step before moving forward. The instructor was another highlight of the course. Not only were they knowledgeable, but also extremely patient and engaging. They had a knack for explaining complex concepts in a way that was easy to understand. The practical examples used throughout the course were relevant and interesting, which made the learning process much more enjoyable.""", 'I hate writing', 'I do not like this product'
]

from textblob import TextBlob
txt = '''I love people. If I do not love people. What else can I love? I do not like this. I will never recommend this'
'''
blob = TextBlob(txt)
print(dir(blob))
print(blob.word_counts)
print(blob.sentences)
print(blob.tags)

def find_sentiment(polarity):
    sentiment = ''
    if polarity > 0:
        sentiment = 'Positive'
    elif polarity == 0:
        sentiment = 'Neutral'
    elif polarity <= 0:
        sentiment = 'Negative'
    return sentiment



""" 
The sentiment property returns a namedtuple of the form Sentiment(polarity, subjectivity). The polarity score is a float within the range [-1.0, 1.0]. The subjectivity is a float within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective.


"""


sentiments = []
for comment in comments:
    blob = TextBlob(comment)
    polarity = blob.sentiment.polarity
    sentiment = find_sentiment(polarity)
    sentiments.append(sentiment)
    
print(sentiments)


import matplotlib.pyplot as plt
import numpy as np




""" x = np.array(list(range(-10, 11)))
y = x ** 2 

plt.plot(x, y)
plt.show() """


postives =[ senti for senti in sentiments if senti == 'Positive']
negatives =[ senti for senti in sentiments if senti == 'Negative']
neutrals =[ senti for senti in sentiments if senti == 'Neutral']


labels = ['Negative','Neutral','Positive']
data = [len(negatives), len(neutrals), len(postives)]


colors = ['red', 'orange', 'g']
y_pos = range(len(labels))
plt.bar(y_pos, data, color = colors)
# Rotation of the bars names
plt.xticks(y_pos, labels, rotation=90)
plt.title('Sentiment Analysis of Python course feedback')
plt.xlabel('Sentiment')
plt.ylabel('Counts')
plt.savefig('./sentiment.png')
plt.savefig('./sentiment.jpg')
plt.show()


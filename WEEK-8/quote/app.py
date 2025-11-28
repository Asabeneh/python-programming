from flask import Flask, render_template, url_for
import requests
from random import randint


def fetch_data (url):
    response = requests.get(url)
    return response.json()

app = Flask(__name__)

@app.route('/')
def home():
    url = 'https://type.fit/api/quotes'
    data = fetch_data(url)
    end = len(data) - 1
    index = randint(0, end)
    quote = data[index]
    return render_template('index.html', quote = quote)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/quotes')
def quotes():
    url = 'https://type.fit/api/quotes'
    data = fetch_data(url)
    return render_template('quotes.html', data = data)
    

if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0', port = 5000)
 

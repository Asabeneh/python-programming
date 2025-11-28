from flask import Flask, render_template
from fetch_data import fetch_data
from datetime import datetime


app = Flask(__name__)

cats_api_url = 'https://api.thecatapi.com/v1/breeds'
cats = fetch_data(cats_api_url)
simplified_cats = [{
    'country':cat['origin'],
    'name':cat['name'],
    'description':cat['description'],
    'life_span':cat['life_span'],
    'weight':cat['weight'],
    'image_url':'https://cdn2.thecatapi.com/images/' + cat.get('reference_image_id') + '.jpg'  if cat.get('reference_image_id') else '',
    'temperament':cat['temperament']
    
    } for cat in cats]


@app.route('/')
def home():
    now = datetime.now()
    new_year = datetime(2026, 1, 1)
    time_left = new_year - now
    return render_template('home.html', time_left  = time_left)


@app.route('/about')
def about():
    return '<h1 style="background:blue;color:white; font-size: 64px">It is all about me</h1>'

@app.route('/api/v1/cats')
def cats_api():
    return simplified_cats

@app.route('/cats')
def cats():
    n = len(simplified_cats)
    return render_template('cats.html', data = simplified_cats, n = n)




app.run(host='localhost', port=8000, debug=True)


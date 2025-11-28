from flask import Flask, render_template
from mysql.connector import connect
app = Flask(__name__)

db = connect(
    host='localhost',
    user = 'root',
    password = 'root'
)

cursor = db.cursor()

"""
DROP THE DATABEASE
CREATE THE DATABASE AGAIN
CREATE A BLOG TABLE
ACCESS DATA FROM THE TABLE
UPDATE THE TABLE
DELETE DATA FROM THE TABLE

"""


for d in cursor:
    print(d)


@app.route('/')
def home ():
    return render_template('index.html')


@app.route('/about')
def about ():
    return render_template('about.html')


@app.route('/contacts')
def contacts ():
    return render_template('contacts.html')

@app.route('/blogs')
def blogs ():
    return render_template('blogs.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port = 5000)
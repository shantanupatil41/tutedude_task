##Building an APIs

from flask import Flask, request, render_template, jsonify
from datetime import datetime
from dotenv import load_dotenv
import os
import pymongo

load_dotenv()  # Load environment variables from .env file
client = pymongo.MongoClient('mongodb+srv://yashshitole2003:12345@cluster0.vfgpaef.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client.test

collection = db['flask-tutorial']
app = Flask(__name__)
#first route
@app.route('/')

def home(): # This is the home route function
    # Render the index.html template when the home route is accessed
    day_of_week = datetime.now().strftime('%A')
    # Get the current day of the week
    return render_template('index.html', day_of_week=day_of_week)  # Render the index.html template

#second route- http://127.0.0.1:5000/second
@app.route('/second')
def second():
    return "This is the second page!"

#1) fetching data from request url 
@app.route('/third/<name>')
def third(name):
    return f"Hello, {name}!"

#2) fetching data from query json- http://127.0.0.1:5000/fourth?name=Yash&age=21
@app.route('/fourth')
def fourth():
    name = request.values.get('name')
    age = request.values.get('age')

    result = {
        'name': name,
        'age': age
    }
    return result
#task
@app.route('/api')
def api():
    name = request.values.get('name')
    id1 = request.values.get('id1')

    result = {
        'name': name,
        'id1': id1
    }
    return jsonify(result)
#submit
@app.route('/submit', methods=['POST'])
def submit():

    form_data = dict(request.form)
    collection.insert_one(form_data)
    # Insert the form data into the MongoDB collection
    return "data submitted successfully!"
    
if __name__ == '__main__': #run krnyasathi he compulosry ahe
    app.run(debug=True)  # Run the Flask application in debug mode


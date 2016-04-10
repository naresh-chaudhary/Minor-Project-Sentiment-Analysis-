from app import app
import json
from time import time
from random import random
from flask import Flask, render_template, make_response
from util import Util

u=Util()

@app.route('/')
def hello_world():
    return render_template('index.html', data='test')

@app.route('/live-data')
def live_data(): 
    #data = [time() * 1000, random() * 100, "Nishant"]
    data = u.get_tweets()
    print data
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response

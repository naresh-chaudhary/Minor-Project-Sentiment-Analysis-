import json
from time import time
from random import random
from flask import Flask, render_template, make_response, session
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', data='test')

@app.route('/live-data')
def live_data():
    print Info.tweets
    data = [time() * 1000, random() * 100, "Nishant"]
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response

if __name__ == '__main__':
    from daemon import Info
    app.run(debug=True, host='127.0.0.1', port=5000)

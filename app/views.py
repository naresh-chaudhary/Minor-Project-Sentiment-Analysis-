from app import app
from flask import render_template
from main import tweets


@app.route('/')
@app.route('/index')
def index():
	
	return render_template('index.html')	
	#return "I am all set baby... :D cover your ass !! "

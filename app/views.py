from app import app

@app.route('/')
@app.route('/index')
def index():
	return "I am all set baby... :D cover your ass !! "

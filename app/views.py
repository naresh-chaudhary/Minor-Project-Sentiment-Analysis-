from app import app
import json
import time
from random import random
from flask import Flask, render_template, make_response,request, redirect
from daemon import getTweets, getPoles, getTextAnalyse


@app.route('/', methods = ['GET', "POST"])
def home():
    if request.method == "POST":
        if request.form['query']:
            print request.form['query']
            tweets = getTweets(request.form['query'])
            pol = []
            temp_pol = getPoles()
            for item in temp_pol:
                pol.append({"name":item, "y" : temp_pol[item]})
            print pol
            query = "#"+str(request.form['query']).upper()
            return render_template('tweetsAnalyse.html', tweets = tweets, pol = json.dumps(pol), query = query)
    return render_template('index.html', data='test')


@app.route('/textanalyse', methods = ['GET','POST'])
def getData():
    result = None
    #keywords = {'Adjective': ['stick', 'incognito', 'more'], 'Verb': ['be', 'kept', 'Learn'],
     #'Noun': ['Pages', 'incognito', 'tabs', 'browser', 'history', 'cookie', 
     #'store', 'search', 'history', 'you', 'tabs', 'files', 'incognito', 'browsing']}
    if request.method == "POST":
        if request.form['texta']:
            result = getTextAnalyse(request.form['texta'])
            print result
            return render_template('textAnalysis.html', result = (result[0], result[1]), text = request.form['texta'], keywords=result[2])
    return render_template('textAnalysis.html', result = result)
'''
@app.route('/live-data')
def live_data():
    print "LIVE DATA CALLED"
    data = u.get_tweets()
    print "data:"
    print data
    print "analysed_tweet:"
    print analysed_tweet
    print "%"*60
    v = (data[1]['compound']+1)/2
    f.write(data[0]+"\n")
    print data[0], v
    data = [time() * 1000, v * 100]
    f.write(str(data))
    f.write("*"*50)
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response
'''

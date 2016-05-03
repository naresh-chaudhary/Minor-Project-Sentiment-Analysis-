from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from analyser import Analyser
import json
from naresh_twitter_credentials import ckey,csecret,atoken,asecret
#consumer key, consumer secret, access token, access secret.

tweets = []
analyze =  Analyser()
class listener(StreamListener):
    def on_data(self, data):
        try:
            d=(json.loads(data))
            k = analyze.get_all_info(d)
            tweets.append(k)
            print k
            print len(tweets)
            if len(tweets)>=50:
                return(False)
        except Exception as e:
            print e
        return(True)
    def on_error(self, status):
        print status

def getTweets(query):
    global tweets
    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    twitterStream = Stream(auth, listener())
    tweets = []
    twitterStream.filter(track=[query])
    return tweets

def getPoles():
    return analyze.getScores()

def getTextAnalyse(text):
    return analyze.textAnalyse(text)



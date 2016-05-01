from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from analyser import Analyser
import json

#consumer key, consumer secret, access token, access secret.
ckey="MAwfDbRqDa54geK8dxy4Vj4s0"
csecret="GzRZbkQxZYpfzy6Azhu5JhpfXuo10tFCpesVYFGed4AvLzh0DV"
atoken="147847030-tkzBAv4d5LnLoxv6IwyRRmh1CBe6MgjLbtkUVoRB"
asecret="Cbud9QKkT218O9dwWjNZqQXGPyg8PPeWYG1GompUiQlsT"
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



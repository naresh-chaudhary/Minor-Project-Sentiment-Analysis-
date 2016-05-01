
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import time
from naresh_twitter_credentials import ckey,csecret,atoken,asecret
from analyser import Analyser


k = open("feeshike.txt","a")
analyse=Analyser()
analysed_tweet=''
class listener(StreamListener):

    def on_data(self, data):
        d=(json.loads(data))
        k.write("#"*60)
        k.write(str(d))
        k.write("\n")
        print "-"*80
        analysed_tweet=analyse.get_all_info(d)
        print analysed_tweet
        return True

    def on_error(self, status):
        print status

class Util():
    def __init__(self):
        auth = OAuthHandler(ckey, csecret)
        auth.set_access_token(atoken, asecret)
        self.twitterStream = Stream(auth, listener())

    def get_tweets(self):
        return self.twitterStream.filter(track=["NitSrinagar"])



from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
from krati_twitter_credentials import ckey,csecret,atoken,asecret



print ckey
print csecret
print atoken
print asecret


f=open("NitSrinagar.txt","w")

class listener(StreamListener):
    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_status(self, status):
        print(status.text)
    
    '''
    def on_data(self, data):
        d=(json.loads(data))
        f.write(d["text"]+"\n")
        print "-"*80
        return(True)
    '''

    def on_error(self, status_code):
        print status_code
        if status_code==420:
            print "exiting"
            return False


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["NitSrinagar"],languages="en")


















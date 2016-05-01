from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from analyser import Analyser
from main import info
import json

#consumer key, consumer secret, access token, access secret.
ckey="MAwfDbRqDa54geK8dxy4Vj4s0"
csecret="GzRZbkQxZYpfzy6Azhu5JhpfXuo10tFCpesVYFGed4AvLzh0DV"
atoken="147847030-tkzBAv4d5LnLoxv6IwyRRmh1CBe6MgjLbtkUVoRB"
asecret="Cbud9QKkT218O9dwWjNZqQXGPyg8PPeWYG1GompUiQlsT"

k = open("feeshike.txt","w")
analyze =  Analyser()
class listener(StreamListener):

    def on_data(self, data):
        try:
            d=(json.loads(data))
            info = analyze.get_all_info(d)
            print info
        except:
            pass
        return(True)

    def on_error(self, status):
        print status

 
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["sunny"])



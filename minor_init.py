from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

#consumer key, consumer secret, access token, access secret.
ckey="MAwfDbRqDa54geK8dxy4Vj4s0"
csecret="GzRZbkQxZYpfzy6Azhu5JhpfXuo10tFCpesVYFGed4AvLzh0DV"
atoken="147847030-tkzBAv4d5LnLoxv6IwyRRmh1CBe6MgjLbtkUVoRB"
asecret="Cbud9QKkT218O9dwWjNZqQXGPyg8PPeWYG1GompUiQlsT"

class listener(StreamListener):

    def on_data(self, data):
        d=(json.loads(data))
        print d["text"]
        print "-"*80
        return(True)

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["ENGvsWI"])



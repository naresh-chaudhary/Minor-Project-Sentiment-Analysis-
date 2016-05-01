class Info:
    tweets = []

    @staticmethod
    def add_tweet(d):
        Info.tweets.append(d)
        print Info.tweets

    @staticmethod
    def get_tweet():
        return Info.tweets[-1]
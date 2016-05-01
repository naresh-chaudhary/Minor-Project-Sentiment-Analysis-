from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from tagger import Tagger
n=100
subj = [(sent, 'subj') for sent in subjectivity.sents(categories='subj')[:n]]
obj = [(sent, 'subj') for sent in subjectivity.sents(categories='obj')[:n]]
train_data = subj +obj
sa = SentimentAnalyzer()
neg_words = sa.all_words([mark_negation(doc) for doc in train_data])
uf = sa.unigram_word_feats(neg_words, min_freq=4)
sa.add_feat_extractor(extract_unigram_feats, unigrams=uf)
training_set = sa.apply_features(train_data)
#test_set = sentim_analyzer.apply_features(testing_docs)
trainer = NaiveBayesClassifier.train
classifier = sa.train(trainer, training_set)

class Analyser():
    def __init__(self):
        self.sia = SentimentIntensityAnalyzer()
        self.p = {"positive": 0, "negative": 0, "neutral":0}
        print "OBJECT CREATED"

    def getPolarity(self, tweet):
        temp = self.sia.polarity_scores(tweet['text'])
        if temp['compound']==0.0:
            self.p["neutral"]+=1
        elif temp['compound'] > 0.0:
            self.p["positive"]+=1
        else:
            self.p["negative"]+=1
        return temp

    def getlocation(self, tweet):
        if tweet['user']['location']:
            return str(tweet['user']['location'])
        else:
            return str(tweet['user']['time_zone'])

    def gettimestamp(self, tweet):
        return tweet['created_at']

    def get_all_info(self, tweet):
        print "Tweet Received"
        polarity = self.getPolarity(tweet)
        loc = self.getlocation(tweet)
        ts = self.gettimestamp(tweet)
        #print tweet['text'],polarity,loc,ts
        return ((tweet['text'],polarity,loc,ts))

    def getScores(self):
        return self.p

    def textAnalyse(self, text):
        t = Tagger(text)
        wordcloud = t.pos_tag()
        lines = text.split('.')
        pol_val = 0.0
        result = ''
        size = len(lines)
        for line in lines:
            temp = self.sia.polarity_scores(line)
            pol_val+=temp['compound']
            print line,temp
        pol_val = pol_val/size
        if pol_val < -0.1:
            result = "n"
        elif pol_val > 0.1:
            result = "p"
        else:
            result = "x"
        print pol_val, result
        return (result, abs(pol_val)*100.0, wordcloud )





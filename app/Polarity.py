from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer

n = 100
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
def getPolarity():
    sia = SentimentIntensityAnalyzer() 
    sia.polarity_scores(stri)

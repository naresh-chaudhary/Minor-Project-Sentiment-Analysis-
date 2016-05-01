from nltk import word_tokenize, pos_tag
from collections import defaultdict
tagger={"NN":"Noun","NNP":"Noun","NNPS":"Noun","NNS":"Noun","JJ":"Adjective",
"JJR":"Adjective","JJS":"Adjective","RB":"Adverb","RBR":"Adverb",
"RBS":"Adverb","VB":"Verb","VBG":"Verb","VBN":"Verb","VBN":"Verb"}


class Tagger():
	def __init__(self, raw_text):
		self.raw_text = raw_text
	
	def pos_tag(self):
		tokenized_text=word_tokenize(self.raw_text)
		tagged_text=pos_tag(tokenized_text)
		result=defaultdict(list)
		for tag in tagged_text:
			if tag[1] in tagger:
				result[tagger[tag[1]]].append(tag[0])
		return result


		




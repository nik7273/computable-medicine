import nltk

from nltk import Tree
from nltk.draw.util import CanvasFrame
from nltk.draw import TreeWidget

def preprocess(string_of_words):
	return string_of_words.replace('associated','').lower().split()


grammar = nltk.data.load(r'./sem.fcfg')

hpi = " A 33 year-old man with a past medical history of coronary artery disease (coronary artery bypass graft in 2010) presents with 3 days of crushing 6/10 chest pain that radiates down his left arm. There is no associated shortness of breath. There is diaphoresis. "
snippet_1 = preprocess("A 33_year_old man with a history of coronary_artery_disease complicated_by coronary_artery_bypass_graft in 2010 presents_with 3 days of crushing 6/10 chest pain that radiates down his arm")
snippet_2 = preprocess("There_is_no associated shortness_of_breath")
snippet_3 = preprocess("There_is diaphoresis")
parser = nltk.parse.FeatureEarleyChartParser(grammar)
parses = list(parser.parse(snippet_1))
#print len(parses)
parses[0].draw()

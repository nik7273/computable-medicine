import nltk

from nltk import Tree
from nltk.draw.util import CanvasFrame
from nltk.draw import TreeWidget

grammar = nltk.grammar.FeatureGrammar.fromstring("""
	% start S
	# Grammar Productions

	S -> N[BAR=2] V[BAR=2] | V[BAR=2] | N[BAR=2] LV N[BAR=2]
	N[BAR=2] -> Det N[BAR=1] | N[BAR=1]
	N[BAR=1] -> Adj[BAR=2] N[BAR=1] | N[BAR=0] | N[BAR=1] P[BAR=2] | N[BAR=0] Adj[BAR=2]

	V[BAR=2] -> Adv V[BAR=1] | V[BAR=1] N[BAR=2] | V[BAR=1]
	V[BAR=1] -> V[BAR=0]

	P[BAR=2] -> Prep N[BAR=2]

	Adj[BAR=2] -> Adj[BAR=1] | C[BAR=2]
	Adj[BAR=1] -> Adj[BAR=0]

	C[BAR=2] -> Complementizer N[BAR=2] | Complementizer S 

	# Lexical Productions
	Prep -> 'with' | 'of' | 'in' | 'down' 
	Det -> 'a'
	Complementizer -> 'complicated_by' | 'that'
	Adj[BAR=0] -> '33' | 'year_old' | 'coronary' | '3' | 'crushing' | 'chest' | '6/10' | 'his' | 'no' | 'associated' 
	N[BAR=0] -> 'man' | 'history' | 'disease' | 'artery' | 'coronary_artery_bypass_graft' | '2010' | 'coronary_artery_disease' | 'days' | 'pain' | 'arm' | 'shortness' | 'breath' | 'shortness_of_breath' | 'diaphoresis'
	V[BAR=0] -> 'presents_with' | 'radiates' | 'there_is' | 'there_is_no'
	""")

hpi = " A 33 year-old man with a past medical history of coronary artery disease (coronary artery bypass graft in 2010) presents with 3 days of crushing 6/10 chest pain that radiates down his left arm. There is no associated shortness of breath. There is diaphoresis. "
snippet_1 = "A 33 year_old man with a history of coronary_artery_disease complicated_by coronary_artery_bypass_graft in 2010 presents_with 3 days of crushing 6/10 chest pain that radiates down his arm".lower().split()
snippet_2 = "There_is_no associated shortness_of_breath".lower().split()
snippet_3 = "There_is diaphoresis".lower().split()
parser = nltk.parse.FeatureEarleyChartParser(grammar)
parses = list(parser.parse(snippet_3))
print len(parses)
parses[0].draw()

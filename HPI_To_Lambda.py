# -*- coding: utf-8 -*-

#HPI=> Lambda functions

import fcfg_wrapper as wrap
import nltk

#example
grammar = nltk.CFG.fromstring("""
	S -> NP VP | VP  | NP LV NP
	VP -> V NP | V | V NP NP | V PP 
	LV -> 'is'
	NP -> Det N | Det Adj N | Det Adj Adj N | Det Adj Adj N PP | Det N PP | Adj N | Adj N N | Adj N N CP | Adj N CP | N | N PP | N CP | Adj N PP | Adj Adj Adj N | Adj Adj Adj N CP | Adj Adj N PP | Adj Adj N 
	CP -> C NP | C VP 
	PP -> Prep NP  

	Prep -> 'with' | 'of' | 'in' | 'down' 
	Det -> 'a'
	C -> 'complicated_by' | 'that'
	Adj -> '33' | 'year_old' | 'coronary' | '3' | 'crushing' | 'chest' | '6/10' | 'his' | 'no' | 'associated' 
	N -> 'man' | 'history' | 'disease' | 'artery' | 'coronary_artery_bypass_graft' | '2010' | 'coronary_artery_disease' | 'days' | 'pain' | 'arm' | 'shortness' | 'breath' | 'shortness_of_breath' | 'diaphoresis'
	V -> 'presents_with' | 'radiates' | 'there_is' | 'there_is_no'
	""")
hpi = " A 33 year-old man with a past medical history of coronary artery disease (coronary artery bypass graft in 2010) presents with 3 days of crushing 6/10 chest pain that radiates down his left arm. There is no associated shortness of breath. There is diaphoresis. "
snippet_1 = "A 33 year_old man with a history of coronary_artery_disease complicated_by coronary_artery_bypass_graft in 2010 presents_with 3 days of crushing 6/10 chest pain that radiates down his arm".lower().split()
snippet_2 = "There_is_no associated shortness_of_breath".lower().split()
snippet_3 = "There_is diaphoresis".lower().split()

#incomplete: figure out how to check if term is verb, noun, adj, prep, etc.
def lambda_generator():
    lambda_functions = []
    for token in hpi.lower().split():
        #add lambda functions for each element of the hpi
        wrap.make_noun(token) #example operation
    return lambda_functions



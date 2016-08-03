#!/usr/bin/python
#coding=utf-8
import json 
from prettyprint import prettyprint 
from termcolor import colored, cprint


db = json.load(open('./db.json','rb'))

LAMBDA = u'\u03BB'
#--- Stage 1 : Processing HPI to lambda functions 
cprint(u'Recieved HPI and processed it to %s'%LAMBDA, 'red')
print '\n'
lambda_functions = []
#--- Stage 2 : Mapping lambda functions to conditionals probabilities
cprint(u'Converting %s to conditonals'%LAMBDA,'red')
print '\n'
#--- Stage 3 : Combining conditional probabilities with prior probabilities from lit
cprint(u'Combining conditionals with prior probabilities','red')
print "Extracted the following signs and symptoms from the HPI"
ssx = ['X','Y','Z']
for disease in db:
	print 'Computing P(%s | %s)'%(','.join(ssx),disease)
	print 'Approximating that as PI',
	print ' '.join(['P(%s | %s)'%(s,disease) for s in ssx])
	print '\n'
print '\n'
#--- Stage 4 : Calculating ordered diagnosis
cprint(u'Displaying top n most likely diagnoses','red')
print 'Prior probabilities for all known diseases:'
for disease in db:
	print "Disease %s; P (prior) = %.04f"%(disease,db[disease]["prior_probability"])
	print 'Need to calculate P (disease | signs and symptoms)'

if len(lambda_functions) == 0:
	print 'Recovered no lambda functions'

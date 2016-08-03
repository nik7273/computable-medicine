#!/usr/bin/python
#coding=utf-8

from prettyprint import prettyprint 
from termcolor import colored, cprint

LAMBDA = u'\u03BB'
#--- Stage 1 : Processing HPI to lambda functions 
cprint(u'Recieved HPI and processed it to %s'%LAMBDA, 'red')

#--- Stage 2 : Mapping lambda functions to conditionals probabilities
cprint(u'Converting %s to conditonals'%LAMBDA,'red')

#--- Stage 3 : Combining conditional probabilities with prior probabilities from lit
cprint(u'Combining conditionals with prior probabilities','red')

#--- Stage 4 : Calculating ordered diagnosis
cprint(u'Displaying top n most likely diagnoses','red')


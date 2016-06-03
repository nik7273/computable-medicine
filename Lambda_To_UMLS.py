# -*- coding: utf-8 -*-
import HPI_To_Lambda as h2l

lambdas = h2l.lambda_generator()

def UMLS_generator():
    #Access UMLS API and gather relations 
    UMLS = []
    for x in lambdas:
        #associate with terms
        #if x.phrase in UMLS association
        #UMLS += x.UMLSassociation #placeholder, x is in fact the UMLS association
        
    return UMLS    
    #incomplete due to trouble working with the UMLS API

#figure out how to get the term from the lambda function for string checking in UMLS
#figure out how to get all relations from UMLS API PROPERLY


# -*- coding: utf-8 -*-

import Lambda_To_UMLS as l2U

UMLS = l2U.UMLS_generator()

prior_probabilities = {}
def probability_generator():
    posterior_probabilities = {}
    for concept in UMLS:
        if prior_probabilities[str(concept)] != '':
            #bayesian equation, add posterior probability to dict.
            posterior_probabilities[str(concept)] = posterior_probabilities[str(prior_probabilities[str(concept)])] * prior_probabilities[str(concept)] / prior_probabilities[str(prior_probabilities[str(concept)])]
        else:
            posterior_probabilities[str(concept)] = 1 #random number for now, proof of concept
    
    return posterior_probabilities
    


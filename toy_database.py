# -*- coding: utf-8 -*-

def generateProbability(A, B, dictionary):
    if A == B:
        return dictionary[A]["general"]
    else:
        return dictionary[B][A] * dictionary[B]["general"] / dictionary[A]["general"]
        
    
    
database = {'A':{'A': 1,'B': 1,'C': 1,'D': 1,'general': 1}, 'B':{'A': 1,'B': 1,'C': 1,'D': 1,'general': 1}, 'C':{'A': 1,'B': 1,'C': 1,'D': 1,'general': 1}, 'D':{'A': 1,'B': 1,'C': 1,'D': 1,'general': 1}}

 #1 is a placeholder for probability. Half of these probabilities are undefined and their values are the function generateProbability(A,B,database)

diseases = ['A','B','C','D']
for disease in diseases:
    for other in diseases:
        database[disease][other] = generateProbability(disease,other,database)

probList = [database[disease][other] for other in diseases for disease in diseases]


                                                                                                              

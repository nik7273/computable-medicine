# -*- coding: utf-8 -*-
#generate_Figures

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd 

D = {'A':{'x':0.5,'y':0.4,'z':0.3,'general':0.1},
     'B':{'x':0.75,'y':0.65,'z':0.45,'general':0.2},
     'C':{'x':0.25,'y':0.15,'z':0.2,'general':0.1},
     'gen':{'x':0.05,'y':0.025,'z':0.1,'general':1}}


def posterior(disease,symptom):
    return D[disease][symptom] * D['gen'][symptom] / D[disease]['general']

database = {'x':{'A':0.5,'B':0.4,'C':0.3,'unconditional':0.1},
     'y':{'A':0.75,'B':0.65,'C':0.45,'unconditional':0.2},
     'z':{'A':0.25,'B':0.15,'C':0.2,'unconditional':0.1},
     'A':{'unconditional':0.1},
     'B':{'unconditional':0.2},
     'C':{'unconditional':0.3}}

#Create data table
diseases = ['A','B','C']
symptoms = ['x','y','z']

probabilities = np.zeros((len(diseases),len(symptoms)))

#Conditional probabilities
for i,disease in enumerate(diseases):
	for j,symptom in enumerate(symptoms):
		probabilities[j,i] = database[symptom][disease] * database[disease]['unconditional']/database[symptom]['unconditional']


conditional_probabilities = np.prod(probabilities, axis=1)
df = pd.DataFrame(np.c_[[conditional_probabilities,
	[database[disease]['unconditional'] for disease in diseases]]],
	index=['prior','posterior'],columns = diseases)

print df

df = pd.read_csv('./sample_dataframe.csv')
print df 

ax = sns.barplot(data=df, x='disease', y='probability', hue='type')
plt.show()

'''
xDependent = [posterior(disease,'x') for disease in D]
yDependent = [posterior(disease, 'y') for disease in D]
zDependent = [posterior(disease,'z') for disease in D]
priorProbability = [D[disease]['general'] for disease in D]

x = np.arange(4)
ax = plt.subplot(111)
priorBar = ax.bar(x-0.3, priorProbability, width=0.2,color='y',align='center')
xBar = ax.bar(x-0.1,xDependent,width=0.2,color='r',align='center')
yBar = ax.bar(x+0.1,yDependent,width=0.2,color='g',align='center')
zBar = ax.bar(x+0.3,zDependent,width=0.2,color='b',align='center')
#ax.legend( (priorBar[0], xBar[0], yBar[0], zBar[0]), ('Prior', 'x', 'y', 'z') )

ax.set_ylabel("Probabilities")
ax.set_xlabel("Disease")
ax.set_xticks(x)
ax.set_xticklabels([disease for disease in D])

"""def autolabel(rects):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%f' % round(h,2) ,
                ha='center', va='bottom')
                

autolabel(priorBar)
autolabel(xBar)
autolabel(yBar)
autolabel(zBar)"""
plt.suptitle("Posterior and Prior Probabilities of Diseases using Bayes' Theorem")
plt.show()
#plt.savefig("Posterior_prior_bar_graph")
'''
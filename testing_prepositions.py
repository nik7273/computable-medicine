import nltk

from nltk import Tree
from nltk.sem import cooper_storage as cs

grammar = nltk.data.load(r'./with.fcfg')

hpi = "33_year_old man with coronary_artery_disease and stroke" #in 2010
#hpi = "coronary_artery_disease complicated_by coronary_artery_bypass_graft"
#parser = nltk.parse.FeatureEarleyChartParser(grammar)
trees = cs.parse_with_bindops(hpi, grammar=r'./with.fcfg')
#trees = [tree for tree in parser.parse(hpi)]
if len(trees) == 1:
	phrase_tree = trees[0]
	phrase_tree.draw()
	semrep = trees[0].label()['SEM']
	cs_semrep = cs.CooperStore(semrep)
	cs_semrep.s_retrieve() #Must S-retrieve before can get readings. 
	reading = cs_semrep.readings[0]
else:
	print '%d trees. Have to choose'%len(trees)
	print 'No choice function defined'
	trees[0].draw()

print reading
print reading.predicates()
print reading.constants()

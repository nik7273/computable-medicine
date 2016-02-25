import nltk

from nltk import Tree
from nltk.sem import cooper_storage as cs

#grammar = nltk.data.load(r'./with.fcfg')
#grammar = nltk.data.load(r'./many-quantified-nps.fcfg')
def parse_cooper_storage(tree):
	semantic_representation = cs.CooperStore(tree.label()['SEM'])
	print semantic_representation.s_retrieve,'k'
	semantic_representation.s_retrieve()
	for reading in semantic_representation.readings:
		print 'Reading %s'%reading
		print 'Simplified Reading %s'%reading.simplify()
		print 'Predicates: ', reading.predicates()
		print 'Variables: ',reading.variables()

hpi = "33_year_old man with coronary_artery_disease complicated_by coronary_artery_bypass_graft in 2010"
#hpi = '33_year_old man'
#hpi = "stroke and coronary_artery_disease in 2010"
#hpi = "33_year_old man with coronary_artery_disease and stroke in 2010"
#hpi = "coronary_artery_disease complicated_by coronary_artery_bypass_graft"
#parser = nltk.parse.FeatureEarleyChartParser(grammar)
#trees = cs.parse_with_bindops(hpi, grammar=r'./with.fcfg')
trees = cs.parse_with_bindops(hpi, grammar=r'./many-quantified-nps.fcfg')

#trees = [tree for tree in parser.parse(hpi)]
if len(trees) == 1:
	trees[0].draw()
	parse_cooper_storage(trees[0])
	
else:
	print '%d trees. Have to choose'%len(trees)
	print 'No choice function defined'
	
	for tree in trees:
		tree.draw()
		parse_cooper_storage(tree)


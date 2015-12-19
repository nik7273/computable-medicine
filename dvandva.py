import nltk

from nltk import Tree
from nltk.draw.util import CanvasFrame
from nltk.draw import TreeWidget

grammar = nltk.data.load(r'./dvandva.fcfg')

hpi = "history of coronary artery disease".split()
parser = nltk.parse.FeatureEarleyChartParser(grammar,trace=2)
for tree in parser.parse(hpi):
	tree.draw()


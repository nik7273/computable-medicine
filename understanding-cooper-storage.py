from nltk.sem import cooper_storage as cs
from nltk.draw.util import CanvasFrame
from nltk.draw import TreeWidget

sentence = 'a girl chases a dog'

trees = cs.parse_with_bindops(sentence, grammar=r'./storage.fcfg')

trees[0].draw()
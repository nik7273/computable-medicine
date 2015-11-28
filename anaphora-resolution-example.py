import nltk

from nltk.sem import logic
from nltk.inference import TableauProver
from nltk.sem.drt import *

txt = "The patient is a 31 year-old Dominican female with no past medical history, a surgical history significant for gastric bypass and subsequent reconstructive surgery five years ago and a psychiatric history significant for alcohol dependence for which she went to rehab twice and was admitted once for withdrawal who presents mid-morning to Englewood Emergency Department complaining of chest pain."

dexpr = DrtExpression.fromstring
dp = DrtParser()

drs7 = dp.parse('([x, y], [angus(x), dog(y), own(x, y)])')
drs8 = dp.parse('([u, z], [PRO(u), irene(z), bite(u, z)])')
drs9 = drs7 + drs8
print drs9.simplify()
print drs9.simplify().resolve_anaphora()
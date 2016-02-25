
def make_noun(noun,bar=0):
    if bar == 0: # Sure it's a terminal
        return ["N[BAR=%d,SEM=[CORE=<%s>,STORE=(/)]] -> '%s'"%(bar,noun,noun)]
    else:
        return ["N[BAR=%d,SEM=[CORE=?n,STORE=?b1]] -> N[BAR=%d,SEM=[CORE=?n,STORE=?b1]]"%(bar,bar-1)] + make_noun(noun,bar-1)


def make_adjective(adjective,bar=0):
    if bar == 0:
        return ["A[BAR=%d,SEM=[CORE=<%s>,STORE=(/)]] -> '%s'"%(bar,adjective, adjective)]

    # What if higher bar?

updates = []
updates += make_noun('bob',bar=2)
updates += make_adjective('brillig',bar=0)

print updates
    
def update_file(filename):
    with open(filename,'a+') as grammar_file:
        for update in updates:
            print>>grammar_file,update

update_file('test.fcfg')

def make_noun(noun,bar=0):
    if bar == 0: # Sure it's a terminal
        return ["N[BAR=%d,SEM=[CORE=<%s>,STORE=(/)]] -> '%s'"%(bar,noun,noun)]
    else:
        return ["N[BAR=%d,SEM=[CORE=?n,STORE=?b1]] -> N[BAR=%d,SEM=[CORE=?n,STORE=?b1]]"%(bar,bar-1)] + make_noun(noun,bar-1)

def make_preposition(prep,bar=0):
    if bar == 0:
        return ["P[BAR=%d, SEM=[CORE=<%s>, STORE=(/)]] -> '%s'" % (bar, prep, prep)]


def make_adjective(adjective,bar=0):
    if bar == 0:
        return ["A[BAR=%d,SEM=[CORE=<%s>,STORE=(/)]] -> '%s'"%(bar,adjective, adjective)]

    # What if higher bar?

#deletes a terminal by searching for the terminals with the wanted value in them and then writing all lines to the same file besides those selected lines
def delete_terminal(value,filename):
    with open(filename, 'r+') as grammar_file:
        grammar_file_list = grammar_file.readlines()
        grammar_file.seek(0)
        for lambda_function in grammar_file_list:
            if value not in lambda_function.split(" "):
                grammar_file.write(lambda_function)
        grammar_file.truncate()

updates = []
updates += make_noun('bob',bar=2)
updates += make_adjective('brillig',bar=0)

print updates
    
def update_file(filename, u):
    with open(filename,'a+') as grammar_file:
        for update in u:
            print>>grammar_file,update

def edit_terminal(value,filename,endvalue,terminal_type):
    delete_terminal(value,filename)
    if terminal_type == 'adj':
        update_file(filename,[make_adjective(endvalue,bar=0)])
    elif terminal_type == 'n':
        update_file(filename,[make_noun(endvalue,bar=0)])
        
edit_terminal('bob','test.fcfg', 'dan', 'n')

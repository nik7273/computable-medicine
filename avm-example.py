from awesome_print import ap 
import numpy as np 
'''Calculate P (MI | {chest pain, male, 30})'''

test = {}
for key, unconditional_value in zip(["a","b","c","d"],[0.2,0.3,0.4,0.5]):
	test[key] = {}
	test[key]["unconditional"] = unconditional_value
	test[key]["a"] = unconditional_value + 0.1

def parse_query(dictionary,query):
	'''  P (a | {b,c,d})
		 = P(a|b) P(a|c) P(a|d) (by assumption)
		 = P(b|a)P(a)P(c|a)P(a)P(d|a)P(a) / P(b)P(c)P(d)
		 = P(b|a) P(c|a) P(d|a) P(a)^^(len(conditionals)) / P(b) P(c) P(d)
	'''
	query = query.strip()
	prior, conditionals = query.split('|')

	prior = prior.strip()
	conditionals = [x.strip() for x in conditionals.split(',')]

	return np.prod([dictionary[prior]["unconditional"] 
			if prior not in dictionary[conditional]
			else (dictionary[conditional][prior]* dictionary[prior]["unconditional"]/
				dictionary[conditional]["unconditional"])
			for conditional in conditionals if conditional in dictionary])

ap(parse_query(test,"a | b,c,d"))

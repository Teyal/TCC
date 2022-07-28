from random import randint, sample
import pandas as pd
import os
SIZE = int(os.getenv('SIZE'))
MAX = int(os.getenv('MAX'))

def all_nuns(size):
    reachables = set()
    for c in range(3,size): # clauses
        for v in range(3,size-c): # variables
            if c*3 >= v: # make sure it can be created in a 3-sat
                reachables.add((c/v,c,v))
    return reachables


def gen_ranges(ranges, size, num_values = 3):
    nums = all_nuns(size)

    finals = []
    for mi,ma in ranges:
        possible = [(n,c,v) for n,c,v in nums if n>mi and n<ma]
        print(f"[{mi},{ma}] -> {len(possible)}")
        finals.extend(possible)
        #if len(possible) < MAX:
        #    finals.extend(possible)    
        #else:
        #    finals.extend(sample(possible, k=MAX))
    return finals

min, max = 0, 0.5 # values that can be changed
ranges = [[min+0.5*i, max+0.5*i] for i in range(10)]
for i in range(25,31):
    print(f'Qubits: {i}')
    values = gen_ranges(ranges,i)
#values = gen_ranges(ranges,SIZE)

#print(values)
#df = pd.DataFrame(values, columns=['Clau/var', 'Cla','Var'])
#df.to_csv('sats/range_values.csv', index=False)
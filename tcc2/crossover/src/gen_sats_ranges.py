from random import randint, sample
import pandas as pd
import os
SIZE = os.getenv('SIZE')

def all_nuns(size):
    reachables = set()
    for n in range(3,size):
        for d in range(3,size-n):
            if n*3 > d: #make sure it can be created in a 3-sat
                reachables.add((n/d,n,d))
    return reachables


def gen_ranges(ranges, size = 23, num_values = 3):
    nums = all_nuns(size)

    finals = []
    for mi,ma in ranges:
        for i in range(num_values):
            possible = [(n,c,v) for n,c,v in nums if n>mi and n<ma]
        temp = []
        finals.extend(sample(possible, k=1))
    return finals
min, max = 0, 0.5
ranges = [[min+0.5*i, max+0.5*i] for i in range(10)]

values = gen_ranges(ranges,int(SIZE))
df = pd.DataFrame(values, columns=['Clau/var', 'Cla','Var'])
df.to_csv('src/range_values.csv', index=False)
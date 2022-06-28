import pandas as pd
from random import seed, randint
seed(17100538)

def gen_sat(num_var, num_cla):
    sat = f'''c     3-SAT autogerated in DIMACS-CNF format
p cnf {num_var} {num_cla}'''

    var_used = set()
    for c in range(num_cla):
        sat += '\n'
        for i in range(3):
            v = randint(1,num_var)
            var_used.add(v)
            sign = randint(0,1)
            if sign:
                v = -v
            sat += f'''{v} '''
        sat += '0'
    return sat, len(var_used)

df = pd.read_csv('sats/range_values.csv')
sat_ranges = df.values.tolist()
sat_list = []
for _, c, v in sat_ranges:
    print(f"gen: {c},{v}")
    while True:
        possible_sat, var_used = gen_sat(int(v),int(c))
        if var_used == v: # making sure all variables were used
            break
        #print(f'var requested: {v} var used={var_used}')
    sat_list.append(possible_sat)

sat_df = pd.DataFrame(sat_list)
sat_df.to_csv('../sats.csv')
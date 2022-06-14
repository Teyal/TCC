import pandas as pd
import random

def gen_sat(num_var, num_cla):
    sat = f'''3-SAT autogerated in DIMACS-CNF format
p cnf {num_var} {num_cla}'''

    var_used = set()
    for c in range(num_cla):
        sat += '\n'
        for i in range(3):
            v = random.randint(1,num_var)
            var_used.add(v)
            sign = random.randint(0,1)
            if sign:
                v = -v
            sat += f'''{v} '''
        sat += '0'
    return sat, len(var_used)

df = pd.read_csv('src/range_values.csv')
sat_ranges = df.values.tolist()
sat_list = []
for _, c, v in sat_ranges:
    while True:
        possible_sat, var_used = gen_sat(int(v),int(c))
        if var_used == v:
            break
        #print(f'var requested: {v} var used={var_used}')
    sat_list.append(possible_sat)

sat_df = pd.DataFrame(sat_list)
sat_df.to_csv('../sats.csv')
print(sat_list)
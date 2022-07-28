import pandas as pd

df = pd.read_csv('../sats.csv')
for i,sat in df.values.tolist():
    print(i)
    f = open(f"../DPLL-SAT-solver-master/test_cases/{i}.cnf","w")
    f.write(sat)
    f.close()

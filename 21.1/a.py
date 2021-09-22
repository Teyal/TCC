import numpy as np

max_c=14-3
for i in range(30):
    clasules = np.random.randint(3,11)
    max_var  = 14 - clasules
    variables = np.random.randint(3,max_var)
    print(f"[{clasules}, {variables}]")
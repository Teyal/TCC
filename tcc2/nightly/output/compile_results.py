import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import pi, sqrt

temp = pd.read_csv('../sats.csv')
sats = temp.iloc[:,1].tolist()
v = np.array([int(s.split()[8]) for s in sats])
c = np.array([int(s.split()[9]) for s in sats])

df = pd.read_csv(f'output/results_iteraion_{0}.csv')

# print(df['Clau/var'][10])
# print(c[10]/v[10])
    
results = {'%.5f'%x[0]: [] for x in zip(c/v)}

# print(df)

colors = {True:'blue', False:'red'}
ax = df.plot.scatter(x="Clau/var", y="Iterações", c=df['Achado'].map(colors))

k = 0
for i in range(1,10):
    df = pd.read_csv(f'output/results_iteraion_{i}.csv')
    # print(len(df))
    df.plot.scatter(x="Clau/var", y="Iterações", c=df['Achado'].map(colors), ax=ax)
    for j in range(len(df)):
        k += 1 
        cv = df['Clau/var'][j]
        results['%.5f'%cv].append(df['Iterações'][j])

def avg(lst):
    return sum(lst)/len(lst)

plt.show()

# x, y =[], []
# for i in results.keys():
#    for j in results[i]:
#        x.append(i)
#        y.append(j)
#    plt.scatter(x, y, colors = )
#    plt.legend(results.keys())
# plt.show()

# x = [float(x) for x in results.keys()]
# y = results.values()
# print(y)
# xs,ys = zip(*results.values())
# plt.scatter(xs,ys)
# plt.show()

means = [(float(key),avg(results[key])) for key in results]

# plt.scatter(*zip(*means))
# plt.show()

min, max = 0, 0.5 # values that can be changed
ranges = [(min+0.5*i, max+0.5*i) for i in range(10)]

range_means = {x:[]  for x in ranges}

# print(range_means)
for cv, m in means:
    for min, max in range_means:
        # (min,max) = rang 
        if cv > min and cv < max:
            range_means[(min,max)].append(m)
            # print(f'({min},{max} : {m}')
            break

# print(range_means)
for k in range_means:
    (mi, ma) = k
    print(f"[{mi},{ma}]: {avg(range_means[k])}")

# print(ranges)
# print(means)

# df = pd.read_csv(f'output/results_iteraion_{3}.csv')
# print(df['Clau/var'][10])
# print(df['Iterações'][10])

#     max_value = df.max(axis=0)[0]
#     x = [i for i in np.arange(0.1,max_value,0.1)]

# cv = np.array(c) / np.array(v)

# y_n = [n_func(int(i)) for i in v]
# y_sqrt_n = [sqrt_n(int(i)) for i in v]

# cv
# y_sqrt_n
# lists = sorted({x: y for x, y in zip(cv, y_sqrt_n)}.items())
# x, y = zip(*lists)

# #ax = plt.axes()

# #ax.plot(x,y)

# #x1,x2,y1,y2 = plt.axis()
# #plt.axis((x1,x2,0,60))

# #ax.scatter(df, c=df['Achado'].map(colors))
# df.plot.scatter(x="Clau/var", y="Iterações", c=df['Achado'].map(colors))
# plt.show()

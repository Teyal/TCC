import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import pi, sqrt

colors = {True:'blue', False:'red'}
n_func = lambda t : int((pi/4)*(2**t))
sqrt_n = lambda t : int((pi/4)*sqrt(2**t))

df = pd.read_csv('output/results_iteraion_0.csv')
# df = pd.read_csv('output/results_1-4.csv')
max_value = df.max(axis=0)[0]
x = [i for i in np.arange(0.1,max_value,0.1)]

temp = pd.read_csv('../sats.csv')
sats = temp.iloc[:,1].tolist()
v = [int(s.split()[8]) for s in sats]
c = [int(s.split()[9]) for s in sats]


cv = np.array(c) / np.array(v)

y_n = [n_func(int(i)) for i in v]
y_sqrt_n = [sqrt_n(int(i)) for i in v]

print(type(x))
cv
y_sqrt_n
lists = sorted({x: y for x, y in zip(cv, y_sqrt_n)}.items())
x, y = zip(*lists)

#ax = plt.axes()

#ax.plot(x,y)

#x1,x2,y1,y2 = plt.axis()
#plt.axis((x1,x2,0,60))

#ax.scatter(df, c=df['Achado'].map(colors))
df.plot.scatter(x="Clau/var", y="Iterações", c=df['Achado'].map(colors))

plt.show()

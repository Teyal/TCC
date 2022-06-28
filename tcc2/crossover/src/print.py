import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('final_new.csv')
colors = {True:'blue', False:'red'}
df.plot.scatter(x="Clau/var", y="Iterações", c=df['Achado'].map(colors))
plt.show()
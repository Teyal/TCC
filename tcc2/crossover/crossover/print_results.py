import matplotlib.pyplot as plt
from math import sqrt, floor, ceil
from matplotlib.transforms import Bbox
import pandas as pd
import numpy as np

def up_bound(t, n=256):
    result = 0
    try:
        result = n/(2 * sqrt((n-t)*t))
    except ValueError:
        pass
    except ZeroDivisionError:
        print('Error zero div with n=',n,', t=',t)
    return (9/2) * result

if __name__ == '__main__':

    results = pd.read_csv('results.csv').transpose()

    total = results.transpose().mean()
    total.plot(kind = 'bar', fc=(0,0,1,0.5))

    up_line = []
    for i in range(len(results.index)): 
        max = results.iloc[i].max()
        min = results.iloc[i].min()
        
        plt.plot(i,max,'bo')
        plt.plot(i,min,'bo')
        #plt.vlines(i, min, max)
        std = results.iloc[i].std()
        mean = results.iloc[i].mean()
        plt.vlines(i, mean - std, mean + std)

        x = [i+0.25 for x in range(len(results.iloc[i]))]
        plt.plot(x,results.iloc[i],'-ok')

        t = int(results.index[i])
        up_line.append(up_bound(t))
    plt.plot(up_line, color = 'red')
    plt.title('All plots')

    plt.show()%                       
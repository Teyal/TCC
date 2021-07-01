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

    for i in range(len(results.index)): 
        t = int(results.index[i])
        results.iloc[i].plot(kind = 'bar')
        plt.axhline(results.iloc[i].mean(), color='orange')
        plt.axhline(up_bound(t), color='red')

        plt.title('Número de respostas: {}'.format(t))
        plt.xlabel('Testes')
        plt.ylabel('Consultas')
        #plt.text(10,50,' ', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        plt.show()


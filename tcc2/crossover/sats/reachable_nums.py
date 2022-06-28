import matplotlib.pyplot as plt

def reachable_nums_skip(size):
    size = size + 1
    reachables = []
    colors = []
    for n in range(3,size):
        for d in range(3,size-n):
            if n*3 > d: #make sure it can be created in a 3-sat
                reachables.append(n/d)
    return reachables, colors

fig, ax = plt.subplots()

x, y, color = [], [], []
min, max = 23, 29
for s in range(min,max):
    reachables, colors = reachable_nums_skip(s)
    x.extend(reachables)
    y.extend([s]*len(reachables))
    color.extend(colors)
ax.scatter(x, y)
ax.set_xlabel("Cla/Var")
ax.set_ylabel("# Qubits")
ax.set_yticks(range(min,max))
ax.set_xticks(range(8))
plt.show()


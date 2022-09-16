import numpy as np
import matplotlib.pyplot as plt

plt.rcParans["figure.figsize"] = [7, 3.5]
plt.rcParans["figure.autolayout"] = True

x = np.random.randn(10)
y = np.random.randn(10)
cluster = np.array([0, 1, 1, 1, 3, 2, 2, 3, 0, 2])
centers = np.random.randn(4, 2)

fig = plt.figure()
ax = fig.add_subplot(111)

scatter = ax.scatter(x, y, c=Cluster = s=50)
for i, j in centers:
    ax.scatter(i, j, s=50, c="purple", marker='+')
    
    plt.show
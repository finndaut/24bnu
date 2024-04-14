import numpy as np
import matplotlib.pyplot as plt

def f(x1, x2, a: float, b: float):
    ret1 = a * x1
    ret2 = (b - a ** 2) * x1 ** 2 + b * x2
    return [ret1, ret2]


nrange = np.arange(26)
coor_list = []
c = 1 / 100
x_n = [c, c ** 2]
for _ in nrange:
    coor_list.append(x_n)
    x_n = f(*x_n, a=9 / 10, b=10)

norm_list = np.linalg.norm(coor_list, axis=1)

fig, ax = plt.subplots()

ax.semilogy(nrange, norm_list)

fig.savefig('U01_3.pdf')

pass

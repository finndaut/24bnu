import numpy as np


def f(x1, x2, a=float(0), b=float(0)):
    ret1 = a * x1
    ret2 = (b - a ** 2) * x1 ** 2 + b * x2
    return ret1, ret2


nrange = np.arange(25) + 1
coor_list = []
c = 1 / 100
x_n = (c, c ** 2)
for _ in nrange:
    coor_list.append(x_n)
    x_n = f(*x_n, a=9 / 10, b=10)
coor_list.append(x_n)
norm_list = np.

pass

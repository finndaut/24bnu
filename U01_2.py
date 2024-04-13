import numpy as np
from matplotlib import pyplot

j_range = np.arange(8) + 1
n_range = 2 ** j_range


def s(n):
    ret = 0
    for k in (np.arange(n) + 1):
        ret += 1 / k ** 2
    return ret


def s_rev(n):
    ret = 0
    for k in (n - np.arange(n)):
        ret += 1 / k ** 2
    return ret


s_vec = np.vectorize(s)
s_rev_vec = np.vectorize(s_rev)

s_ret = s_vec(n_range)
s_rev_ret = s_rev_vec(n_range)
deviation = abs(s_ret - s_rev_ret)


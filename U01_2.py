import numpy as np
from matplotlib import pyplot

j_range = np.arange(8) + 1
n_range = 2 ** j_range


def s(n_range):
    ret_list = []
    for n in n_range:
        summe = 0
        for k in (np.arange(n) + 1):
            summe += 1 / k ** 2
    return ret_list


def s_rev(n_range):
    ret_list = []
    for n in n_range:
        summe = 0
        for k in (n - np.arange(n)):
            summe += 1 / k ** 2
    return ret_list


s_ret = s(n_range)
s_rev_ret = s_rev(n_range)
deviation = abs(s_ret - s_rev_ret)


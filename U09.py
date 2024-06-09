import numpy as np


#def cholesky(pseudo_mat, )


def pseudo_a(n, m, dim_m=2):
    if n == m:
        ret = 4
    elif abs(n - m) == abs(dim_m) or (abs(n - m) == 1 and not ((n%dim_m != 1) and (m%dim_m != 1))):
        ret = -1
    else:
        ret = 0

    return ret


def pseudo_h(n, m, dim_m=2):
    return 1 / (n + m + 1)


pseudo_a = np.vectorize(pseudo_a)
pseudo_h = np.vectorize(pseudo_h)


print(pseudo_a(*np.ogrid[0:3**2, 0:3**2], dim_m=3))
print(np.arange(9)%3)
print(np.arange(9)%3)

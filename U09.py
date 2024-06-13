import pickle
import numpy as np
from scipy import sparse


def cholesky(matrix):
    i_dim, _ = np.shape(matrix)
    g_arr = np.zeros_like(matrix)
    g_arr[0, 0] = matrix[0, 0] ** (1 / 2)
    g_arr[1:, 0] = matrix[1:, 0] / matrix[0, 0] ** (1 / 2)
    for i in range(1, i_dim):
        g_arr[i, i] = (matrix[i, i] - np.sum(g_arr[i, 0:i] ** 2)) ** (1 / 2)
        g_arr[i + 1:, i] = (matrix[i + 1:, i] - np.sum(g_arr[i + 1:, 0:i] * g_arr[i, 0:i], axis=1)) / g_arr[i, i]
    return g_arr


def a_func(n, m, dim_m=2):
    if n == m:
        ret = 4
    elif abs(n - m) == abs(dim_m) or (abs(n - m) == 1 and not (n + m + 1) % (2 * dim_m) == 0):
        ret = -1
    else:
        ret = 0
    return np.float64(ret)


def h_func(n, m, dim_m=2):
    return 1 / np.float64(n + m + 1)


print('a_func', len(pickle.dumps(a_func)))

a_func = np.vectorize(a_func)
h_func = np.vectorize(h_func)

for dim in range(2, 21):
    print("dim = %i" % dim)
    a_dens = h_func(*np.ogrid[0:dim ** 2, 0:dim ** 2], dim_m=dim)
    a_diag = sparse.dia_matrix(a_dens)
    a_coor = sparse.coo_matrix(a_dens)
    print('a_dens       ', len(pickle.dumps(a_dens)))

    g_dens = cholesky(a_dens)
    g_diag = sparse.dia_matrix(g_dens)
    g_coor = sparse.coo_matrix(g_dens)
    print('a_diag g_diag', len(pickle.dumps(a_diag)), len(pickle.dumps(g_diag)))
    print('a_cood g_cood', len(pickle.dumps(a_coor)), len(pickle.dumps(g_coor)))
    norm = np.linalg.norm(a_dens - g_dens @ g_dens.T, ord=1)
    print(norm)

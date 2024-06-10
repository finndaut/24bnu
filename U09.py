import numpy as np


def cholesky(matrix):
    i_dim, _ = np.shape(matrix)
    g_arr = np.zeros_like(matrix)
    g_arr[0, 0] = matrix[0, 0] ** (1/2)
    g_arr[1:, 0] = matrix[1:, 0] / matrix[0, 0] ** (1/2)
    for i in range(1, i_dim):
        g_arr[i, i] = (matrix[i, i] - np.sum(g_arr[i, 0:i]**2)) ** (1/2)
        g_arr[i+1:, i] = (matrix[i+1:, i] - np.sum(g_arr[i+1:, 0:i] * g_arr[i, 0:i], axis=1)) / g_arr[i, i]
    return g_arr



def pseudo_a(n, m, dim_m=2):
    if n == m:
        ret = 4
    elif abs(n - m) == abs(dim_m) or (abs(n - m) == 1 and not (n+m+1) % (2*dim_m) == 0):
        ret = -1
    else:
        ret = 0

    return np.float64(ret)


def pseudo_h(n, m, dim_m=2):
    return 1 / np.float64(n + m + 1)


pseudo_a = np.vectorize(pseudo_a)
pseudo_h = np.vectorize(pseudo_h)

for dim in range(2,21):
    a_mat = pseudo_h(*np.ogrid[0:dim**2, 0:dim**2], dim_m=dim)
    g_mat = cholesky(a_mat)
    norm = np.linalg.norm(a_mat-g_mat@g_mat.T, ord=1)

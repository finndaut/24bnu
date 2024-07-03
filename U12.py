import numpy as np
from scipy import sparse


def f_funct(y_arr, lambda_val):
    n, m = y_arr.shape
    ret_arr = sparse.lil_array((n, m))
    ret_arr[0, 0] = -1
    ret_arr[0, -1] = -1
    for index in y_arr.nonzero():
        if len(index):
            i, j = index
            y_val = y_arr[i, j]
            ret_arr[i, j] += 2 * y_val - lambda_val * np.exp(y_val / (1+2*y_val))
            if not j == 0:
                ret_arr[i, j-1] -= y_val
            if not j == m-1:
                ret_arr[i, j+1] -= y_val
    return ret_arr


def f_deriv(y_arr, lambda_val):
    n, m = y_arr.shape
    ret_arr = sparse.lil_array((m, m))
    for index in y_arr.nonzero():
        if len(index):
            i, j = index
            y_val = y_arr[i, j]
            ret_arr[j, j] += 2 - lambda_val * np.exp(y_val / (1+2*y_val)) / (1+2*y_val)**2
            if not j == 0:
                ret_arr[j-1, j] -= 1
            if not j == m-1:
                ret_arr[j+1, j] -= 1
    return ret_arr


def newton(lambda_val, m_val, funct, deriv):
    x_arr = sparse.lil_array((1,m_val))
    while sparse.linalg.norm(funct(x_arr, lambda_val)) > 10**-5:
        a_arr = sparse.linalg.inv(deriv(x_arr, lambda_val))
        x_arr = x_arr - funct(x_arr, lambda_val)
        # print(x_arr.toarray())
    return x_arr.toarray()


print(newton(0.1, 100, f_funct, f_deriv))
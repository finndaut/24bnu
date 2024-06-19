import numpy as np
from scipy import sparse


def norm(matrix, x_vector, b_vector):
    norm = np.linalg.norm(matrix@x_vector-b_vector, ord=np.inf)/np.linalg.norm(x_vector, ord=np.inf)
    return norm


def jacobi(matrix, b_vector):
    k = 0
    x_vector = np.ones_like(b_vector)
    while (norm(matrix, x_vector, b_vector) > 10**-8) and (k < 2*10**4):
        k += 1
        x_temp = b_vector.copy()
        for i in range(len(b_vector)):
            x_temp[i] -= np.sum(
                np.delete(
                    matrix[i,:] * x_vector, i
                )
            )
            x_temp[i] /= matrix[i, i]
        x_vector = x_temp
    print(norm(matrix, x_vector, b_vector), k)

    return x_vector


def gausseidel(matrix, b_vector):
    k = 0
    x_vector = np.ones_like(b_vector)
    while (norm(matrix, x_vector, b_vector) > 10**-8) and (k < 2*10**4):
        k += 1
        x_temp = b_vector.copy()
        for i in range(len(b_vector)):
            x_temp[i] -= np.sum(
                matrix[i, :i] * x_temp[:i]
            )
            x_temp[i] -= np.sum(
                matrix[i, i+1:] * x_vector[i+1:]
            )
            x_temp[i] /= matrix[i, i]
        x_vector = x_temp.copy()
    print(norm(matrix, x_vector, b_vector), k)
    return x_vector


def sor(matrix, b_vector, relax_par):
    k = 0
    x_vector = np.ones_like(b_vector)
    while (norm(matrix, x_vector, b_vector) > 10**-8) and (k < 2*10**4):
        k += 1
        x_temp = b_vector.copy()
        for i in range(len(b_vector)):
            x_temp[i] -= np.sum(
                matrix[i, :i] * x_temp[:i]
            )
            x_temp[i] -= np.sum(
                matrix[i, i+1:] * x_vector[i+1:]
            )
            x_temp[i] *= relax_par / matrix[i, i]
            x_temp[i] += (1 - relax_par) * x_vector[i]
        x_vector = x_temp.copy()
    print(norm(matrix, x_vector, b_vector), k)
    return x_vector


def a_func(n, m, dim_m=2):
    if n == m:
        ret = 4
    elif abs(n - m) == abs(dim_m) or (abs(n - m) == 1 and not (n + m + 1) % (2 * dim_m) == 0):
        ret = -1
    else:
        ret = 0
    return ret


a_func = np.vectorize(a_func)
for k in range(1, 3):
    m = 2**k
    a_dens = a_func(*np.ogrid[0:m ** 2, 0:m ** 2], dim_m=m)
    h = 1 / (m+1)
    relax_par = 2 / (1 + np.sqrt(1-np.cos(h*np.pi)**2))
    b_vector = np.ones(m**2)
    jacobi_vec = jacobi(a_dens, b_vector)
    gausseidel_vec = gausseidel(a_dens, b_vector)
    sor_vec = sor(a_dens, b_vector, relax_par)


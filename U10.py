import numpy as np

b_vector = np.ones(3**2)


def norm(matrix, x_vector, b_vector):
    norm = np.linalg.norm(matrix@x_vector-b_vector, ord=np.inf)/np.linalg.norm(x_vector, ord=np.inf)
    return norm


def jacobi(matrix, b_vector):
    k = 0
    x_vector = np.ones_like(b_vector)
    while (norm(matrix, x_vector, b_vector) > 10**-8) and (k < 2*10**4):
        k += 1
        x_temp = np.array(b_vector)
        for i in range(len(x_vector)):
            x_temp[i] -= np.sum(
                np.delete(
                    matrix[i] * x_vector, i
                )
            )
            x_temp[i] /= matrix[i, i]
        x_vector = x_temp
    print(norm(matrix, x_vector, b_vector), k)

    return x_vector


def gausseidel(matrix, b_vector):
    k = 0
    x_vector = np.zeros_like(b_vector)
    while (norm(matrix, x_vector, b_vector) > 10**-8) and (k < 2*10**4):
        k += 1
        x_temp = np.array(b_vector)
        for i in range(len(x_vector)):
            x_temp[i] -= np.sum(
                matrix[i, :k] * x_temp[:k]
            )
            x_temp[i] -= np.sum(
                matrix[i, k+1:] * x_vector[k+1:]
            )
            x_temp[i] /= matrix[i, i]
        x_vector = x_temp
    print(norm(matrix, x_vector, b_vector), k)
    return ...

def a_func(n, m, dim_m=2):
    if n == m:
        ret = 4
    elif abs(n - m) == abs(dim_m) or (abs(n - m) == 1 and not (n + m + 1) % (2 * dim_m) == 0):
        ret = -1
    else:
        ret = 0
    return np.float64(ret)


a_func = np.vectorize(a_func)


a_dens = a_func(*np.ogrid[0:3 ** 2, 0:3 ** 2], dim_m=3)
gausseidel(a_dens, b_vector)


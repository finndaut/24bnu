import numpy as np


def f0(x):
    return np.tanh(x) - x / 2 - 1 / 2

def deriv0(x):
    return np.cosh(x)**-2 - 1 / 2


def f1(x):
    return np.tanh(x) - x / 10 - 1 / 2


def deriv1(x):
    return np.cosh(x)**-2 - 1 / 10


def f2(x):
    return x - x*1j + 1


def bisect(func, start, sigma, fehler):
    x_n = start
    ret_list = [x_n]
    if func(x_n + sigma) * func(x_n - sigma) < 0:
        while np.linalg.norm(func(x_n)) > fehler:
            if func(x_n + sigma) * func(x_n) < 0:
                sigma /= 2
                x_n += sigma
            elif func(x_n + sigma) == 0:
                x_n += sigma
            elif func(x_n - sigma) * func(x_n) < 0:
                sigma /= 2
                x_n -= sigma
            elif func(x_n - sigma) == 0:
                x_n -= sigma
            ret_list.append(x_n)
    else:
        return 'Kein VW'
    return ret_list


def sekante(func, start, sigma, fehler):
    x_offset = start - sigma
    x_n = start + sigma
    ret_list = [start - sigma, start + sigma]
    while np.linalg.norm(func(x_n)) > fehler:
        x_offset = x_n - (x_n - x_offset) * func(x_n) / (func(x_n) - func(x_offset))
        x_n, x_offset = x_offset, x_n
        ret_list.append(x_n)
    return ret_list


def newton(func, deriv, start, sigma, fehler):
    x_n = start + sigma
    ret_list = [x_n]
    while np.linalg.norm(func(x_n)) > fehler:
        x_n -= func(x_n) / deriv(x_n)
        ret_list.append(x_n)
    return ret_list


print(bisect(f0, -3, 0.2, 10 ** -10))
print(bisect(f1, -15, 0.2, 10 ** -10))
print(bisect(f1, 0.6, 0.2, 10 ** -10))
print(bisect(f1, 5, 0.2, 10 ** -10))


print(sekante(f0, -3, 0.2, 10 ** -10))
print(sekante(f1, -15, 0.2, 10 ** -10))
print(sekante(f1, 0.6, 0.2, 10 ** -10))
print(sekante(f1, 5, 0.2, 10 ** -10))


print(newton(f0, deriv0, -3, 0.2, 10 ** -10))
print(newton(f1, deriv1, -15, 0.2, 10 ** -10))
print(newton(f1, deriv1, 0.6, 0.2, 10 ** -10))
print(newton(f1, deriv1, 5, 0.2, 10 ** -10))

print(sekante(f2, 0, 1, 10 ** -10))

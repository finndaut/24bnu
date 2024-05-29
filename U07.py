import numpy as np
import matplotlib.pyplot as plt


def f(x): 
    return (x-1)**(1/5)


def intf(x0):
    return (2)**(1/5) * 5 / 3 - 5 / 6 * (x0-1)**(6/5)


def romberg(start):
    stop = 3
    float2 = np.float64(2)

    n_range = np.arange(0, 10)
    h_range = (stop - start) * float2 ** -n_range

    T_arr = np.empty([10,10])
    m_n = np.empty([10])
    T_arr[0, 0] = h_range[1]*(f(start)+f(stop))
    m_n[0] = 0

    for n in range(1,):
        i_range = np.arange(0, 2**n)
        m_n[n] = h_range[n] * np.sum(f(start + (2 * i_range + 1) * h_range[n+1]))

    for n in n_range[1:10]:
        T_arr[n, 0] = 1/2 * (T_arr[n-1, 0] + m_n[n-1])

    for k in n_range[1:10]:
        T_arr[k:, k] = (4**k * T_arr[k:, k-1] - T_arr[k-1:-1,k-1]) / (4**k - 1)


    return T_arr


start = 1.0
error = abs(romberg(start) - intf(start))
i_range = np.arange(0,10)


fig, ax = plt.subplots()

for k in [0,1]:
    plot_range = i_range[k:]
    ax.semilogy(plot_range, error[k,plot_range], label='k=%i' %k)

ax.semilogy(i_range, error[i_range,i_range], label='k=i')
ax.set(xlabel='i', ylabel='Fehler')
ax.legend()
plt.show()

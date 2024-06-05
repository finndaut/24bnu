import numpy as np

A_arr = np.array([[1, 0, 2],
                  [1, 10**-20, 3],
                  [2, 1, 1]])
b_arr = np.array([15, 17, 21])

# A_arr = np.array([[2, -1, -3, 3],
#                   [4,  0, -3, 1],
#                   [6,  1, -1, 6],
#                   [-2, -5, 4, 1]], dtype=float)
# b_arr = np.array([1, -8, -16, -12])


def lr_zerlegung(A_arr, b_arr, type):
    R_arr = np.array(A_arr)
    L_arr = np.zeros_like(R_arr)
    i_dim, _ = A_arr.shape
    i_idx = np.arange(i_dim)

    for k in range(0, i_dim-1):
        if type > 1:
            i_pivot = k + np.argmax(abs(R_arr[i_idx[k:], k]))
            i_idx[k], i_idx[i_pivot] = i_idx[i_pivot], i_idx[k]

        for i in range(k+1, i_dim):
            lij = R_arr[i_idx[i], k] / R_arr[i_idx[k], k]
            L_arr[i_idx[i], k] = lij
            R_arr[i_idx[i], k:] -= lij * R_arr[i_idx[k], k:]
    print(R_arr[i_idx, :])

    L_arr[i_idx, :] += np.eye(i_dim)

    print(b_arr)
    x_arr = np.zeros_like(b_arr)
    x_arr[0] = b_arr[i_idx[0]]
    for i in range(1, i_dim):
        x_arr[i] = (b_arr[i_idx[i]] - np.sum(L_arr[i_idx[i], :i-1] * b_arr[i_idx[:i-1]])) / L_arr[i_idx[i], i]

    print(x_arr)
    y_arr = np.zeros_like(b_arr)
    y_arr[i_dim-1] = x_arr[i_dim-1]/R_arr[i_dim-1, i_dim-1]
    for i in range(i_dim-1, -1, -1):
        print(i)
        y_arr[i] = (x_arr[i] - np.sum(R_arr[i_idx[i], i+1:] * x_arr[i+1:])) / R_arr[i_idx[i], i]

    print(y_arr)
    return np.linalg.norm(A_arr@y_arr-b_arr)


# print(lr_zerlegung(A_arr, b_arr, 1))
print(lr_zerlegung(A_arr, b_arr, 2))
print(lr_zerlegung(A_arr, b_arr, 3))

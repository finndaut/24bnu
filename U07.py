import numpy as np

B_arr = np.array([[1, 0, 2],
                  [1, 10**-20, 3],
                  [2, 1, 1]])


def lr_zerlegung(A_arr, type):
    R_arr = A_arr
    L_arr = A_arr
    

    return R_arr, L_arr

lr_zerlegung(B_arr, 0)
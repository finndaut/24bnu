import numpy as np

def pqspecial(w):
    return max(
        abs(-w+1/2+np.sqrt(w-3/4)),
        abs(-w+1/2-np.sqrt(w-3/4))
        )
pqspecial = np.vectorize(pqspecial)

arg_arr = np.arange(0.8, 1.5, 0.1)
print(arg_arr)
print(pqspecial(arg_arr))

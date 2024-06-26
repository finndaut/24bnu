import numpy as np

def pqspecial(w):

    return max(
        np.linalg.norm(1-w+w**2/8 + w/2*np.sqrt(w**2/16-w+1)),
        np.linalg.norm(1-w+w**2/8 - w/2*np.sqrt(w**2/16-w+1))
        )
pqspecial = np.vectorize(pqspecial)

arg_arr = np.arange(0.8, 1.5, 0.1)
print(arg_arr)
print(pqspecial(arg_arr))

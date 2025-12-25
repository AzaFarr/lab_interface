import numpy as np

def gauss_seidel(
        x_old: np.ndarray,
        A: np.ndarray,
        b: np.ndarray ):

    """ returns new set (T_arr) """

    N: int = len(x_old)
    x_new: np.ndarray = np.zeros(shape=N, dtype=float)

    for i in range(N):
        x_new[i] = 1/A[i][i] * ( b[i] - np.sum(A[i][0:i] * x_new[0:i]) - np.sum(A[i][i+1:N] * x_old[i+1:N]) )

    return x_new

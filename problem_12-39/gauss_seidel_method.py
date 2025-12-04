import numpy as np

def gauss_seidel(
        T_old: np.ndarray,
        A: np.ndarray,
        b: np.ndarray ):

    """ returns new set (T_arr) """

    N: int = len(T_old)
    T_new: np.ndarray = np.zeros(shape=N, dtype=float)

    for i in range(N):
        T_new[i] = 1/A[i][i] * ( b[i] - np.sum(A[i][0:i] * T_new[0:i]) - np.sum(A[i][i+1:N] * T_old[i+1:N]) )

    return T_new

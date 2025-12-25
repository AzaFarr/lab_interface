import numpy as np

def poly_coef(
        m: np.ndarray,
        n: np.ndarray ):

    A: np.ndarray = np.zeros((10, 10))  # по задаче это зависимые переменные m и n, по ним находятся интерполяционные коэффициенты потом
    for k in range(9, -1, -1):
        i = 0
        j = 0
        for l in range(9, -1, -1):
            A[k][l] = pow(m[k], i) * pow(n[k], j)
            if (i + j) < 3:
                i += 1
            elif (j < 3):
                j += 1
                i = 0

    return A

def polynom(
        a: np.ndarray, # по задаче это интерполяционные коэффициенты
        m: float, n: float):

   X: np.ndarray = np.zeros(shape=10, dtype=float) # по задаче это зависимые переменные m и n
   b: float = 0

   i = 0
   j = 0
   for l in range(9, -1, -1):
        if (i + j) <= 3:
            X[l] = pow(m, i) * pow(n, j)
            i += 1
        elif (j < 3):
            j += 1
            i = 0

   for l in range(0, 10):
       b += a[0] * X[0]

   return b

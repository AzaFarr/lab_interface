import numpy as np

class Analyt():

    def __init__(self, T_right: float,
                       T_left: float,
                       L: float, N: int,
                       q: float, k: float):

        self.T_right = T_right
        self.T_left = T_left
        self.q = q
        self.k = k

        self.L = L
        self.N: int = N
        self.x: np.ndarray = np.linspace(0, L, N)


    def analytical_formula(self, T: np.ndarray) -> None:
        '''
          Analytical solution for one-dimension stationary heat conductivity
        '''
        for i in range(0, self.N):
            T[i] = (((self.T_right - self.T_left) / self.L) + (self.q / (2 * self.k)) * (self.L - self.x[i])) * self.x[i] + self.T_left

    @property
    def X(self):
        return self.x


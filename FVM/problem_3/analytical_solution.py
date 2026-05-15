import numpy as np


class Analyt():

    def __init__(self, T_right: float,
                       T_left: float,
                       L: float, N: int,
                       n: float):

        self.T_right = T_right
        self.T_left = T_left
        self.n = n

        self.L = L
        self.N: int = N
        self.x: np.ndarray = np.linspace(0, L, N)


    def analytical_formula(self, T: np.ndarray) -> None:
        '''
          Analytical solution for one-dimension stationary heat conductivity
        '''
        # T[0] = self.T_left
        for i in range(0, self.N):
            T[i] = (self.T_left - self.T_right) * (1 - 1 / (1 + np.exp(-2 * self.n * self.L))) * np.exp(self.n * self.x[i]) + ((self.T_left - self.T_right) / (1 + np.exp(-2 * self.n * self.L))) * np.exp(-self.n * self.x[i]) + self.T_right

    @property
    def X(self):
        return self.x


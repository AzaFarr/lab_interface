import numpy as np

from gauss_method import gauss_elimination
from interpolate_func import polynom, poly_coef

class Solution():

    """ Class for solution problem 20-27 with Interpolation and Gauss-Elimination Method """

    def __init__( self,
                  a: float,
                  b: float,
                  z: float,
                  q: float ):

        self.a: float = a
        self.b: float = b
        self.z: float = z
        self.q: float = q / (self.a * self.b)

        x: np.ndarray = np.zeros(shape=10, dtype=float)

        self.m_var: float
        self.n_var: float
        self.f_var: float
        self.sigma: float

        self.f_arr: np.ndarray = np.array([
            0.08323, # m=0.3 n=1.2
            0.08561, # m=0.3 n=1.4
            0.08709, # m=0.3 n=1.6
            0.10631, # m=0.4 n=1.2
            0.10941, # m=0.4 n=1.4
            0.11135, # m=0.4 n=1.6
            0.12626, # m=0.5 n=1.2
            0.13003, # m=0.5 n=1.4
            0.13241, # m=0.5 n=1.6
            0.14749 # m=0.6 n=1.4
        ])

        self.m_arr: np.ndarray = np.array([
            0.3,
            0.3,
            0.3,
            0.4,
            0.4,
            0.4,
            0.5,
            0.5,
            0.5,
            0.6
        ])

        self.n_arr: np.ndarray = np.array([
            1.2,
            1.4,
            1.6,
            1.2,
            1.4,
            1.6,
            1.2,
            1.4,
            1.6,
            1.4
        ])

        print("start poly_coef solving")
        self.A: np.ndarray = poly_coef(self.m_arr, self.n_arr)
        print("poly_coef solved")
        print(self.A, "\n\n")

    def solve(self):

        self.x = gauss_elimination(self.A, self.f_arr)

        self.m_var: float = self.a / self.z
        self.n_var: float = self.b / self.z

        self.f_var = polynom(self.x, self.m_var, self.n_var)
        print(self.f_var)

        self.sigma = self.q * self.f_var

# s = Solution(1, 2, 3, 4)
# s.solve()
# print(s.x)
# print(s.sigma)




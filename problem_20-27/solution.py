import numpy as np

from gauss_seidel_method import gauss_elimination
from interpolate_func import polynom, poly_coef

class Solution():

    """ Class for solution problem 20-27 with Gauss-Seidel Method """

    def __init__( self,
                  a: float,
                  b: float,
                  z: float,
                  q: float ):

        self.a: float = a
        self.b: float = b
        self.z: float = z
        self.q: float = q

        x: np.ndarray = np.zeros(shape=10, dtype=float)

        self.f_var: float
        self.sigma: float

        self.f: np.ndarray = np.array([
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

        self.m: np.ndarray = np.array([
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

        self.n: np.ndarray = np.array([
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
        self.A: np.ndarray = poly_coef(self.m, self.n)
        print("poly_coef solved")
        print(self.A, "\n\n")

    def solve(self):

        f = self.f

        self.x = gauss_elimination(self.A, f)

        m: float = self.a / self.z
        n: float = self.b / self.z

        self.f_var = polynom(self.x, m, n)

        self.sigma = self.q * self.f_var

# s = Solution(1, 2, 3, 4)
# s.solve()
# print(s.x)
# print(s.sigma)


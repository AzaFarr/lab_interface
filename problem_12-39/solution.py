import numpy as np
import math as m

from gauss_seidel_method import gauss_seidel

class Solution():

    """ Class for solution problem 12-39 with Gauss-Seidel Method """

    def __init__( self,
                  T: np.ndarray,
                  x: float,
                  y: float,
                  Error: float ):


        self.T_arr: np.ndarray = T  # it's a matrix [4 x 4]
        self.x: float = x
        self.y: float = y
        self.Error: float = Error

        self.T_start: np.ndarray = np.zeros(shape=4, dtype=float)  # T = [ T23_edit, T32_edit, T22_edit, T33_edit ]
        # self.T_start: np.ndarray = np.array([
        #     10,
        #     130,
        #     100,
        #     30
        # ])

        a = 1/pow(self.x, 2)
        b = 1/pow(self.y, 2)
        c = -2 * (a + b)

        self.A: np.ndarray = np.array([
            [c, a, b, 0],
            [a, c, 0, b],
            [b, 0, c, a],
            [0, b, a, c]
        ])

        self.b: np.ndarray = np.array([
            -(self.T_arr[1][0] * a + self.T_arr[0][1] * b),
            -(self.T_arr[1][3] * a + self.T_arr[0][2] * b),
            -(self.T_arr[2][0] * a + self.T_arr[3][1] * b),
            -(self.T_arr[2][3] * a + self.T_arr[3][2] * b),
        ])


    def solve(self):

        T_old: np.array
        T_new: np.array = np.copy(self.T_start)
        cur_error: float = 1e5

        while cur_error > self.Error:
            T_old = np.copy(T_new)
            T_new = gauss_seidel(T_old=T_old, A=self.A, b=self.b)
            cur_error = abs(T_old[0] - T_new[0])
            print("cur_error = ", cur_error)
            print("T_new = ", T_new)
            print("T_old = ", T_old)

        return T_new

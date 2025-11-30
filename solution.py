import numpy as np
import math as m

from bisection_method import bisec

class Solution():

    """ Class for solution problem 8-34 with Bisection Method """

    def __init__( self,
                  Re: float,
                  f_0: float,
                  f_n: float,
                  Error: float ):

        self.Re: float = Re
        self.f_0: float = f_0
        self.f_n: float = f_n
        self.Error: float = Error

        self.f_arr: np.ndarray = np.linspace(start=self.f_0, stop=self.f_n, num=10)
        self.var_Func_arr: np.ndarray = self.Func_arr(self.Re, self.f_arr)


    def Func(self, Re: float, f: float):

        return 1 / m.sqrt(f) - 4 * m.log10(Re * m.sqrt(f)) + 0.4


    def Func_arr(self, Re: float, f: np.ndarray) -> np.ndarray:

        return 1 / np.sqrt(f) - 4 * np.log10(Re * np.sqrt(f)) + 0.4


    def solve(self):

        Func_0: float
        Func_n: float
        Func_middle: float
        cur_error: float = 10000

        if (self.Func(self.Re, self.f_0) * self.Func(self.Re, self.f_n) < 0):

            while cur_error > self.Error:
                Func_0 = self.Func(self.Re, self.f_0)
                Func_n = self.Func(self.Re, self.f_n)
                Func_middle = self.Func(self.Re, (self.f_n + self.f_0) / 2)
                self.f_0, self.f_n = bisec(self.f_0, self.f_n, Func_0, Func_n, Func_middle)
                cur_error = (abs(self.f_0 - self.f_n) / abs(self.f_n))
                print("cur_error = ", cur_error)

            return ''

        else:

            self.f_n = 0
            return 'there is no solution!\nplease, choose different\narea for f'


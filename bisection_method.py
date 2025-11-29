import numpy as np

def bisec(
        a: float,
        b: float,
        f_a: float,
        f_b: float,
        f_middle: float ):

    """ returns new set (a, b) """

    a_new: float = 0
    b_new: float = 0

    if (f_a*f_middle < 0):
        a_new = a
        b_new = (a + b) / 2
    if (f_b*f_middle < 0):
        a_new = (a + b) / 2
        b_new = b

    return a_new, b_new




import numpy as np
import scipy as sp
import math as m


def calculate(mean_value_array: np.ndarray):
    """если нижняя грань пластины располагается
       на уровне горизонта жидкости, то вводить
               rho_alpha = pho_beta

       если пластина располагается выше/ниже
       горизонта жидкости, то:
           * ниже горизонта => h<0
           * выше горизонта => h>0
    """

    l, t, h, F, phi, rho_alpha, rho_beta = mean_value_array[0], mean_value_array[1], mean_value_array[2], mean_value_array[3], mean_value_array[4], mean_value_array[5], mean_value_array[6]
    g = sp.constants.g

    return (F + t * l * h * (rho_alpha - rho_beta) * g) / (2 * l * m.cos(phi))

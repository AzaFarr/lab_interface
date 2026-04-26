import numpy as np
import scipy as sp


def calculate(mean_value_array: np.ndarray):

    P, R, r, rho_a, rho_b = mean_value_array[0], mean_value_array[1], mean_value_array[2], mean_value_array[3], mean_value_array[4]
    P = P * 1e-5 / 0.01
    R = R * 0.01
    r = r * 0.01
    pi = sp.constants.pi
    a = 0.7250
    b = 0.0009075
    C = 0.04534 - 1.679 * (r / R)

    return P * (a + pow(((4 * b / pi**2) * (1 / R**2) * (P / (rho_a - rho_b)) + C), 0.5))

# [64.89 0.4143 0.01070 1000 1.3] ring no.1 from Harkins, 1 dyn = 1e(-5) newtons
# [82.11 1.8277 0.02986 1000 1.3] ring no.12 from Harkins

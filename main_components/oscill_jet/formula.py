import numpy as np
import scipy as sp


def calculate(mean_value_array: np.ndarray):

    rho, Q, r_o, lambdae = mean_value_array[0], mean_value_array[1], mean_value_array[2], mean_value_array[3]
    g = sp.constants.g

    return (2 * rho * (Q ** 2)) / (3 * r_o * (lambdae ** 2))

#[1000 0.000031 0.01, 0.03]

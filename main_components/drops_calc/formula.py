import numpy as np


def calculate(mean_value_array: np.ndarray):

    alpha_o, rho_o, n_o, rho, n = mean_value_array[0], mean_value_array[1], mean_value_array[2], mean_value_array[3], mean_value_array[4]

    return (alpha_o * rho * n_o) / (n * rho_o)



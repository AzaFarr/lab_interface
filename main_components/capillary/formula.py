import numpy as np
import scipy as sp


def calculate(mean_value_array: np.ndarray):

    rho, r_1, r_2, delta_H = mean_value_array[0], mean_value_array[1], mean_value_array[2], mean_value_array[3]
    g = sp.constants.g

    return (rho * g * r_1 * r_2 * delta_H) / (2 * (r_2 - r_1))


arr = np.array([1000, 0.001, 0.0015, 0.0049])
print(calculate(arr))

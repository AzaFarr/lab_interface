import numpy as np


def calculate(mean_value_array: np.ndarray):

    r, delta_P = mean_value_array[0], mean_value_array[1]

    return r * delta_P / 2

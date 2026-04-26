import numpy as np
import scipy as sp


def calculate(mean_value_array: np.ndarray):

    m_mean, d = mean_value_array[0], mean_value_array[1]
    g = sp.constants.g
    pi = sp.constants.pi

    return (m_mean * g) / (d * pi)

# [0.000219 0.0094]

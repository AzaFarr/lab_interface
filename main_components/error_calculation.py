from tables import Model

import numpy as np
import scipy as sp
from typing import Callable

#TODO: ValueError, RuntimeError/Warnings, ZeroDivision
#      должны быть исключены еще на моменте ввода данных,
#      поэтому надо написать свой обработчик исключений
#      на случаи неправильного ввода, пустых ячеек и т.п.

class Error():

    def __init__(self, header: list[str], function: Callable[[np.ndarray], float]):

        """
            mean_value_array - array of mean measured physical values
            abs_err_value_array - array of absolute errors of measured physical values

            mean_value - value of mean surface tension
            abs_err_value - value of absolute error of surface tension
            rel_err_value - value of relative error of surface tension
        """


        self.header = header
        self.values = []
        self.instrument_error = []
        self.alpha: float = 0.2
        self.n: int = 0

        self.function = function

        self.size = len(self.header) - 2
        self.sys_error_message: str = ''

        self.mean_value_array: np.ndarray = np.zeros(shape=self.size, dtype=float)
        self.abs_err_value_array: np.ndarray = np.zeros(shape=self.size, dtype=float)

        self.mean_value: float = 0
        self.abs_err_value: float = 0
        self.rel_err_value: float = 0

        # Структура: t_student[n][alpha] = значение
        # n - число степеней свободы, alpha - доверительная вероятность
        self.t_student = {
            2: {0.2: 0.33, 0.4: 0.73, 0.5: 1.00, 0.6: 1.38, 0.7: 2.0,
                0.8: 3.1, 0.9: 6.3, 0.95: 12.7, 0.98: 31.8, 0.99: 63.7},

            3: {0.2: 0.29, 0.4: 0.62, 0.5: 0.82, 0.6: 1.06, 0.7: 1.3,
                0.8: 1.9, 0.9: 2.9, 0.95: 4.3, 0.98: 7.0, 0.99: 9.9},

            4: {0.2: 0.28, 0.4: 0.58, 0.5: 0.77, 0.6: 0.98, 0.7: 1.3,
                0.8: 1.6, 0.9: 2.4, 0.95: 3.2, 0.98: 4.5, 0.99: 5.8},

            5: {0.2: 0.27, 0.4: 0.57, 0.5: 0.74, 0.6: 0.94, 0.7: 1.2,
                0.8: 1.5, 0.9: 2.1, 0.95: 2.8, 0.98: 3.7, 0.99: 4.6},

            6: {0.2: 0.27, 0.4: 0.56, 0.5: 0.73, 0.6: 0.92, 0.7: 1.2,
                0.8: 1.5, 0.9: 2.0, 0.95: 2.6, 0.98: 3.4, 0.99: 4.0},

            7: {0.2: 0.26, 0.4: 0.55, 0.5: 0.71, 0.6: 0.90, 0.7: 1.1,
                0.8: 1.4, 0.9: 1.9, 0.95: 2.4, 0.98: 3.1, 0.99: 3.7},

            8: {0.2: 0.26, 0.4: 0.54, 0.5: 0.71, 0.6: 0.90, 0.7: 1.1,
                0.8: 1.4, 0.9: 1.9, 0.95: 2.4, 0.98: 3.0, 0.99: 3.5},

            9: {0.2: 0.26, 0.4: 0.54, 0.5: 0.71, 0.6: 0.90, 0.7: 1.1,
                0.8: 1.4, 0.9: 1.9, 0.95: 2.3, 0.98: 2.9, 0.99: 3.4},

            10: {0.2: 0.26, 0.4: 0.54, 0.5: 0.70, 0.6: 0.88, 0.7: 1.1,
                 0.8: 1.4, 0.9: 1.8, 0.95: 2.3, 0.98: 2.8, 0.99: 3.3},

            15: {0.2: 0.26, 0.4: 0.54, 0.5: 0.69, 0.6: 0.87, 0.7: 1.1,
                 0.8: 1.3, 0.9: 1.8, 0.95: 2.1, 0.98: 2.6, 0.99: 3.0},

            20: {0.2: 0.26, 0.4: 0.53, 0.5: 0.69, 0.6: 0.86, 0.7: 1.1,
                 0.8: 1.3, 0.9: 1.7, 0.95: 2.1, 0.98: 2.5, 0.99: 2.9},

            25: {0.2: 0.26, 0.4: 0.53, 0.5: 0.69, 0.6: 0.86, 0.7: 1.1,
                 0.8: 1.3, 0.9: 1.7, 0.95: 2.1, 0.98: 2.5, 0.99: 2.8},

            30: {0.2: 0.26, 0.4: 0.53, 0.5: 0.68, 0.6: 0.85, 0.7: 1.1,
                 0.8: 1.3, 0.9: 1.7, 0.95: 2.0, 0.98: 2.5, 0.99: 2.8},

            40: {0.2: 0.26, 0.4: 0.53, 0.5: 0.68, 0.6: 0.85, 0.7: 1.1,
                 0.8: 1.3, 0.9: 1.7, 0.95: 2.0, 0.98: 2.4, 0.99: 2.7},

            60: {0.2: 0.25, 0.4: 0.53, 0.5: 0.68, 0.6: 0.85, 0.7: 1.0,
                 0.8: 1.3, 0.9: 1.7, 0.95: 2.0, 0.98: 2.4, 0.99: 2.7},

            120: {0.2: 0.25, 0.4: 0.53, 0.5: 0.68, 0.6: 0.85, 0.7: 1.0,
                  0.8: 1.3, 0.9: 1.7, 0.95: 2.0, 0.98: 2.4, 0.99: 2.6},

            121: {0.2: 0.25, 0.4: 0.52, 0.5: 0.67, 0.6: 0.84, 0.7: 1.0,
                  0.8: 1.3, 0.9: 1.6, 0.95: 2.0, 0.98: 2.3, 0.99: 2.6}
        }



    def calculate(self):
        try:
            self.sys_error_message = ''

            data = np.array(self.values, dtype=float)
            instrument_error = np.array(self.instrument_error, dtype=float)

            # print('start')
            self.mean_value_array = self.get_mean(data)
            print(self.mean_value_array)
            # print('mean success')
            mean_variance = self.get_mean_variance(data)
            print(mean_variance)
            self.abs_err_value_array = self.get_absolute_error(mean_variance, instrument_error)
            # print('abs error success')

            self.mean_value = self.function(self.mean_value_array)
            # print('success')
            self.abs_err_value = self.absolute_error_of_function(self.function)
            # print('success')
            self.rel_err_value = self.get_relative_error()
            # print('success')

        except Exception as e:
            print(e)
            self.sys_error_message = f'<html><body style="color: #D40D0D;"><p>Проверьте корректность ввода данных.</p><p>Ошибка: {e}</p></body></html>'

    def get_student_coefficient(self, n, alpha):
        return self.t_student[n][alpha]

    def get_mean(self, data: np.ndarray):
        return np.sum(a=data, axis=1) / self.n

    def get_mean_variance(self, data: np.ndarray):
        return np.var(a=data, axis=1, ddof=1) / self.n

    def get_absolute_error(self, mean_variance: np.ndarray, instrument_error: np.ndarray):
        abs_err_squared = ((pow(self.get_student_coefficient(self.n, self.alpha), 2) * mean_variance) +
                           pow(self.get_student_coefficient(121, self.alpha) * instrument_error / 3, 2))
        abs_err = pow(abs_err_squared, 0.5)
        return abs_err

    def get_relative_error(self):
        return self.abs_err_value / self.mean_value


    def absolute_error_of_function(self, function):
        def f_vec(x):
            res = np.apply_along_axis(function, 0, x)
            return res

        abs_err_squared = 0
        diff = sp.differentiate.jacobian(f_vec, self.mean_value_array, initial_step=1e-6).df
        # diff = sp.differentiate.jacobian(function, self.mean_value_array).df
        print('diff = ', diff)
        print('abs_err_array = ', self.abs_err_value_array)

        for i in range(self.size):
            abs_err_squared += pow(diff[i], 2) * pow(self.abs_err_value_array[i], 2)

        return pow(abs_err_squared, 0.5)

from tables import Model

import numpy as np

#TODO: ValueError, RuntimeError/Warnings, ZeroDivision
#      должны быть исключены еще на моменте ввода данных,
#      поэтому надо написать свой обработчик исключений
#      на случаи неправильного ввода, пустых ячеек и т.п.

class Error():

    def __init__(self, tabModel: Model):

        self.tabModel = tabModel
        self.sys_error_message: str = ''
        try:
            self.data: np.ndarray = np.array(
                [float(self.tabModel.model.item(k, 1).text()) for k in range(self.tabModel.model.rowCount())])
            self.mean_value = self.mean()
            self.abs_err_value = self.standard_deviation()
            self.rel_err_value = self.relative_error()
        except Exception as e:
            print(e)
            self.sys_error_message = f'<html><body style="color: #D40D0D;"><p>Проверьте корректность ввода данных.</p><p>Ошибка: {e}</p></body></html>'


    def mean(self):
        return sum(self.data) / self.tabModel.model.rowCount()


    def standard_deviation(self):
        return np.std(self.data, ddof=1) / np.sqrt(len(self.data))

    def relative_error(self):
        return self.abs_err_value / self.mean_value


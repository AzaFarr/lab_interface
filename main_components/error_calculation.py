from tables import Model

import numpy as np

class Error():

    def __init__(self, tabModel: Model):

        self.tabModel = tabModel
        self.data: np.ndarray = np.array([float(self.tabModel.model.item(k, 1).text()) for k in range(self.tabModel.model.rowCount())])
        print(self.data)

        self.mean_value = self.mean()
        self.abs_err_value = self.standard_deviation()
        self.rel_err_value = self.relative_error()

    def mean(self):
        return sum(self.data) / self.tabModel.model.rowCount()

    def standard_deviation(self):
        return np.std(self.data, ddof=1) / np.sqrt(len(self.data))

    def relative_error(self):
        return self.abs_err_value / self.mean_value


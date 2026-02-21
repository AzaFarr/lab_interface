from PyQt5 import QtWidgets, QtGui
from load_ui import MainWindow

#TODO: как сделать так, чтобы ширина таблиц задавалась пропорционально
#TODO: как сделать так, чтобы вот этот класс работал для табличек

class Tables(QtWidgets.QTableView):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.col_prop = [0.1, 0.55, 0.35]

    def resizeEvent(self, event):
        super().resizeEvent(event)
        return self.proportional_resize()

    def resize_columns_proportionally(self):

        total_width = self.viewport().width()
        if self.verticalScrollBar().isVisible():
            total_width -= self.verticalScrollBar().width()

        for col, prop in enumerate(self.col_prop):
            if col < self.model().columnCount():
                width = int(total_width * prop)
                self.setColumnWidth(col, width)


class Model():

    def __init__(self):

        self.model = QtGui.QStandardItemModel()

        self.model.setColumnCount(3)
        self.model.setHorizontalHeaderLabels(["№", "Значение", "Время"])


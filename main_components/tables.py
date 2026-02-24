from PyQt5 import QtWidgets, QtGui
from load_ui import MainWindow


class Tables(QtWidgets.QTableView):

    def __init__(self, parent=MainWindow):

        super().__init__(parent)
        self.col_prop = [0.1, 0.55, 0.35]

    def resizeEvent(self, event):  # Метод resizeEvent — встроенный обработчик событий, который срабатывает при изменении размера виджета.
                                   # Объект event содержит метаданные об изменении размера, включая новый размер
        super().resizeEvent(event)
        return self.resize_columns_proportionally()  # таким образом мы накладываем дополнительные действия
                                                     # на метод resizeEvent

    def resize_columns_proportionally(self):

        total_width = self.width()
        print(total_width)
        if self.verticalScrollBar().isVisible():
            total_width -= self.verticalScrollBar().width()
            print(total_width)

        for col, prop in enumerate(self.col_prop):
            if col < 3:
                width = int(total_width * prop)
                self.setColumnWidth(col, width)


class Model():

    def __init__(self):

        self.model = QtGui.QStandardItemModel()
        self.model.setColumnCount(3)
        self.model.setHorizontalHeaderLabels(["№", "Значение", "Время"])

from PyQt5 import QtWidgets, QtGui

from load_ui import MainWindow


class Tables(QtWidgets.QTableView):
    """
       Настройка равномерной ширины столбцов

       model: QtGui.QStandardItemModel - стандартная модель представления таблиц,
                                         задается чтобы определить количество столбцов
                                         (через хэдер) и в конечном итоге правильно их
                                         распределить по ширине таблицы.
    """

    def __init__(self, parent=MainWindow):

        super().__init__(parent)
        self.model: QtGui.QStandardItemModel
        self.columnCount = self.model.columnCount()
        self.col_prop = [((1 - 0.1) / self.columnCount) for i in range(self.columnCount)]
        self.col_prop[0] = 0.1
        print(self.col_prop)

    def resizeEvent(self, event):  # Метод resizeEvent — встроенный обработчик событий, который срабатывает при изменении размера виджета.
                                   # Объект event содержит метаданные об изменении размера, включая новый размер
        super().resizeEvent(event)
        return self.resize_columns_proportionally()  # таким образом мы накладываем дополнительные действия
                                                     # на метод resizeEvent

    def resize_columns_proportionally(self,):

        total_width = self.width()
        if self.verticalScrollBar().isVisible():
            total_width -= self.verticalScrollBar().width()

        for col, prop in enumerate(self.col_prop):
            width = int(total_width * prop)
            self.setColumnWidth(col, width)


class Model():
    """
        Задается стандартная модель элементов таблицы

        header: list[str] - список заголовков столбцов
    """

    def __init__(self, header: list[str]):

        self.header = header
        self.model = QtGui.QStandardItemModel()
        self.model.setColumnCount(len(self.header))
        self.model.setHorizontalHeaderLabels(header)
        self.i: int = 1


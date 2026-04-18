from PyQt5 import QtWidgets, QtGui

from load_ui import MainWindow


class Tables(QtWidgets.QTableView):

    def __init__(self, parent=MainWindow):

        super().__init__(parent)

    def resizeEvent(self, event):  # Метод resizeEvent — встроенный обработчик событий, который срабатывает при изменении размера виджета.
                                   # Объект event содержит метаданные об изменении размера, включая новый размер
        super().resizeEvent(event)
        return self.resize_columns_proportionally()  # таким образом мы накладываем дополнительные действия
                                                     # на метод resizeEvent

    def resize_columns_proportionally(self):
        """
        Настройка равномерной ширины столбцов

        self.horizontalHeader().count() - ключеваое действие, чтобы определить количество
                                          столбцов и в конечном счете правильно их
                                          распределить по ширине таблицы.
        """

        n = self.horizontalHeader().count()
        col_prop = [((1 - 0.1) / (n - 1)) for i in range(n)]
        col_prop[0] = 0.1
        total_width = self.width()
        if self.verticalScrollBar().isVisible():
            total_width -= self.verticalScrollBar().width()

        for col, prop in enumerate(col_prop):
            width = int(total_width * prop)
            self.setColumnWidth(col, width)


class Model():
    """
        Задается стандартная модель элементов таблицы

        header: list[str] - список заголовков столбцов
    """

    def __init__(self, header: list[str]):

        self.header = header
        self.data: list[str]
        self.model = QtGui.QStandardItemModel()
        self.model.setColumnCount(len(self.header))
        self.model.setHorizontalHeaderLabels(header)
        self.i: int = 1


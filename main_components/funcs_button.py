from PyQt5 import QtWidgets, QtGui

def add_item(model: QtGui.QStandardItemModel):

    def command():
        model.appendRow([QtGui.QStandardItem(str(i)) for i in range(3)])

    return command()


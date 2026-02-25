from PyQt5 import QtWidgets, QtGui

#TODO: убрать первый столдец с нумерацией, который автоматически возникает

def add_item(model: QtGui.QStandardItemModel):
    model.appendRow([QtGui.QStandardItem(str(i)) for i in range(3)])



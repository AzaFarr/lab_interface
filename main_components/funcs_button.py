from PyQt5 import QtWidgets, QtGui
from tables import Model
import datetime as dt


def add_item(tabModel: Model, lineEdit: str):
    number = QtGui.QStandardItem(str(tabModel.i))
    exp_data = QtGui.QStandardItem(lineEdit)
    date = QtGui.QStandardItem(str(dt.datetime.now()))
    data = [number, exp_data, date]
    tabModel.model.appendRow(data)
    tabModel.i += 1

def clear_table(tabModel: Model):
    for k in range(tabModel.i):
        tabModel.model.removeRow(0)
    tabModel.i = 1


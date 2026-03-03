from PyQt5 import QtWidgets, QtGui
from tables import Model
import datetime as dt


def add_item(tabModel: Model, lineEdit: str):
    print('lineEdit_6 func started')
    number = QtGui.QStandardItem(str(tabModel.i))
    exp_data = QtGui.QStandardItem(lineEdit)
    date = QtGui.QStandardItem(str(dt.datetime.now()))
    data = [number, exp_data, date]
    tabModel.model.appendRow(data)
    tabModel.i += 1



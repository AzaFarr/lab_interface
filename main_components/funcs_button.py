from PyQt5 import QtWidgets, QtGui

from tables import Model
from error_calculation import Error

import datetime as dt


def rec_data_base(data, dirPaths: list[str]):
    for i, path in enumerate(dirPaths):
        with open(path, 'a') as data_base:
            data_base.write(data[i] + '\n')

def clear_data_base(dirPaths: list[str]):
    for path in (dirPaths):
        with open(path, 'w') as data_base:
            pass

def get_data_base(content: list[list[str]], dirPaths: list[str]):
    del content[:]
    for path in (dirPaths):
        line = []
        string = '-'
        with open(path, 'r') as data_base:
            while string!='':
                string = data_base.readline()[:-1]
                line.append(string)
            content.append(line[:-1])

def let_transfer_data(content, data):
    content = data

def update_data_error(error: Error, dirPaths: list[str], instrument_error: list[str], n: int, alpha: float):
    get_data_base(error.values, dirPaths)
    error.instrument_error = instrument_error
    error.n = n
    error.alpha = alpha


def obtain_data(data, *lineEdits):
    del data[:]
    for value in lineEdits:
        data.append(value)
    print(data)

def add_item(tabModel: Model, data: list[str]):

    try:
        size = len(data)
        data_table = []
        data_table.append(QtGui.QStandardItem(str(tabModel.i)))
        for i in range(size): data_table.append(QtGui.QStandardItem(str(data[i])))
        data_table.append(QtGui.QStandardItem(str(dt.datetime.now())))
        tabModel.model.appendRow(data_table)
        tabModel.i += 1
    except Exception as e:
        print(e)

def clear_table(tabModel: Model):

    for k in range(tabModel.i):
        tabModel.model.removeRow(0)
    tabModel.i = 1

def print_error(error: Error,
                tB_conf_int: QtWidgets.QTextBrowser,
                tB_rel_err: QtWidgets.QTextBrowser,
                tB_sys_err_mes: QtWidgets.QTextBrowser):

    error.calculate()
    tB_sys_err_mes.setHtml(error.sys_error_message)

    try:
        tB_conf_int.setText(f"{error.mean_value:.5f} ± {error.abs_err_value:.5f}  [Н / м]")
        tB_rel_err.setText(f"{error.rel_err_value:.4f}  д.ед.")
    except Exception as e:
        tB_conf_int.setText("")
        tB_rel_err.setText("")


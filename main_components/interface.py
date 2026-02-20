from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PyQt5 import QtWidgets, uic

import sys



class MainWindow(QWidget, QMainWindow):
    def setupUi(self):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1512, 877)
        icon = QIcon()
        icon.addFile(u"../media/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 411, 51))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.frame = QFrame(self.tab)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 80, 1331, 351))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 21, 421, 31))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setUnderline(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(153, 79, 160, 31))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(14)
        font2.setUnderline(False)
        self.lineEdit.setFont(font2)
        self.textBrowser_2 = QTextBrowser(self.frame)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(320, 78, 110, 34))
        self.textBrowser_3 = QTextBrowser(self.frame)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        self.textBrowser_3.setGeometry(QRect(62, 78, 80, 34))
        self.textBrowser_4 = QTextBrowser(self.frame)
        self.textBrowser_4.setObjectName(u"textBrowser_4")
        self.textBrowser_4.setGeometry(QRect(320, 120, 110, 34))
        self.textBrowser_5 = QTextBrowser(self.frame)
        self.textBrowser_5.setObjectName(u"textBrowser_5")
        self.textBrowser_5.setGeometry(QRect(62, 120, 80, 34))
        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(153, 121, 160, 31))
        self.lineEdit_2.setFont(font2)
        self.textBrowser_6 = QTextBrowser(self.frame)
        self.textBrowser_6.setObjectName(u"textBrowser_6")
        self.textBrowser_6.setGeometry(QRect(320, 160, 110, 34))
        self.textBrowser_7 = QTextBrowser(self.frame)
        self.textBrowser_7.setObjectName(u"textBrowser_7")
        self.textBrowser_7.setGeometry(QRect(62, 160, 80, 34))
        self.lineEdit_3 = QLineEdit(self.frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(153, 161, 160, 31))
        self.lineEdit_3.setFont(font2)
        self.textBrowser_8 = QTextBrowser(self.frame)
        self.textBrowser_8.setObjectName(u"textBrowser_8")
        self.textBrowser_8.setGeometry(QRect(320, 200, 110, 34))
        self.textBrowser_9 = QTextBrowser(self.frame)
        self.textBrowser_9.setObjectName(u"textBrowser_9")
        self.textBrowser_9.setGeometry(QRect(62, 200, 80, 34))
        self.lineEdit_4 = QLineEdit(self.frame)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(153, 201, 160, 31))
        self.lineEdit_4.setFont(font2)
        self.textBrowser_10 = QTextBrowser(self.frame)
        self.textBrowser_10.setObjectName(u"textBrowser_10")
        self.textBrowser_10.setGeometry(QRect(320, 240, 110, 34))
        self.textBrowser_11 = QTextBrowser(self.frame)
        self.textBrowser_11.setObjectName(u"textBrowser_11")
        self.textBrowser_11.setGeometry(QRect(62, 240, 81, 34))
        self.lineEdit_5 = QLineEdit(self.frame)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(153, 241, 160, 31))
        self.lineEdit_5.setFont(font2)
        self.textBrowser = QTextBrowser(self.frame)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(730, 10, 561, 321))
        self.frame_2 = QFrame(self.tab)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(20, 460, 1331, 311))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 30, 411, 31))
        self.label_3.setFont(font1)
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(90, 90, 201, 31))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setUnderline(False)
        font3.setWeight(75)
        self.label_4.setFont(font3)
        self.textBrowser_12 = QTextBrowser(self.frame_2)
        self.textBrowser_12.setObjectName(u"textBrowser_12")
        self.textBrowser_12.setGeometry(QRect(337, 129, 110, 34))
        self.textBrowser_13 = QTextBrowser(self.frame_2)
        self.textBrowser_13.setObjectName(u"textBrowser_13")
        self.textBrowser_13.setGeometry(QRect(79, 129, 80, 34))
        self.lineEdit_6 = QLineEdit(self.frame_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(170, 130, 160, 31))
        self.lineEdit_6.setFont(font2)
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(230, 180, 211, 31))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(11)
        self.pushButton.setFont(font4)
        self.tableView = QTableView(self.frame_2)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(600, 60, 581, 241))
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(620, 20, 201, 31))
        self.label_5.setFont(font3)
        self.tabWidget.addTab(self.tab, "")
        self.frame.raise_()
        self.label.raise_()
        self.frame_2.raise_()
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.tabWidget.addTab(self.tab_8, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.tabWidget.addTab(self.tab_9, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.tabWidget.addTab(self.tab_10, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1512, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow",
                                                             u"\u041c\u044b \u0435\u0449\u0435 \u043d\u0435 \u0437\u0430\u043a\u043e\u043d\u0447\u0438\u043b\u0438..",
                                                             None))
        self.label.setText(QCoreApplication.translate("MainWindow",
                                                      u"\u041c\u0435\u0442\u043e\u0434 \u043a\u0430\u043f\u0438\u043b\u043b\u044f\u0440\u043d\u044b\u0439",
                                                      None))
        self.label_2.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u0412\u0432\u043e\u0434 \u044d\u043a\u0441\u043f\u0435\u0440\u0438\u043c\u0435\u043d\u0442\u0430\u043b\u044c\u043d\u044b\u0445 \u0434\u0430\u043d\u043d\u044b\u0445",
                                                        None))
        self.lineEdit.setText("")
        self.textBrowser_2.setHtml(QCoreApplication.translate("MainWindow",
                                                              u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                              "p, li { white-space: pre-wrap; }\n"
                                                              "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">[\u043a\u0433 / \u043c</span><span style=\" font-size:14pt; font-weight:600; vertical-align:super;\">3</span><span style=\" font-size:14pt; font-weight:600;\">]</span></p></body></html>",
                                                              None))
        self.textBrowser_3.setHtml(QCoreApplication.translate("MainWindow",
                                                              u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                              "p, li { white-space: pre-wrap; }\n"
                                                              "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">\u03c1 = </span></p></body></html>",
                                                              None))
        self.textBrowser_4.setHtml(QCoreApplication.translate("MainWindow",
                                                              u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                              "p, li { white-space: pre-wrap; }\n"
                                                              "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">[\u043c / \u0441</span><span style=\" font-size:14pt; font-weight:600; vertical-align:super;\">2</span><span style=\" font-size:14pt; font-weight:600;\">]</span></p></body></html>",
                                                              None))
        self.textBrowser_5.setHtml(QCoreApplication.translate("MainWindow",
                                                              u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                              "p, li { white-space: pre-wrap; }\n"
                                                              "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">g = </span></p></body></html>",
                                                              None))
        self.lineEdit_2.setText("")
        self.textBrowser_6.setHtml(QCoreApplication.translate("MainWindow",
                                                              u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                              "p, li { white-space: pre-wrap; }\n"
                                                              "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">[\u043c]</span></p></body></html>",
                                                              None))
        self.textBrowser_7.setHtml(QCoreApplication.translate("MainWindow",
                                                              u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                              "p, li { white-space: pre-wrap; }\n"
                                                              "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">r</span><span style=\" font-size:14pt; font-weight:600; vertical-align:sub;\">1</span><span style=\" font-size:14pt; font-weight:600;\"> = </span></p></body></html>",
                                                              None))
        self.lineEdit_3.setText("")
        self.textBrowser_8.setHtml(QCoreApplication.translate("MainWindow",
                                                              u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                              "p, li { white-space: pre-wrap; }\n"
                                                              "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">[\u043c]</span></p></body></html>",
                                                              None))
        self.textBrowser_9.setHtml(QCoreApplication.translate("MainWindow",
                                                              u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                              "p, li { white-space: pre-wrap; }\n"
                                                              "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">r</span><span style=\" font-size:14pt; font-weight:600; vertical-align:sub;\">2</span><span style=\" font-size:14pt; font-weight:600;\"> = </span></p></body></html>",
                                                              None))
        self.lineEdit_4.setText("")
        self.textBrowser_10.setHtml(QCoreApplication.translate("MainWindow",
                                                               u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                               "p, li { white-space: pre-wrap; }\n"
                                                               "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">[\u043c]</span></p></body></html>",
                                                               None))
        self.textBrowser_11.setHtml(QCoreApplication.translate("MainWindow",
                                                               u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                               "p, li { white-space: pre-wrap; }\n"
                                                               "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Times New Roman','serif'; font-size:14pt; font-weight:600; color:#000000;\">\u0394H</span><span style=\" font-size:14pt; font-weight:600;\"> = </span></p></body></html>",
                                                               None))
        self.lineEdit_5.setText("")
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow",
                                                            u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><title>\u041a\u0430\u043f\u0438\u043b\u043b\u044f\u0440\u043d\u044b\u0439 \u043c\u0435\u0442\u043e\u0434 \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u044f \u043f\u043e\u0432\u0435\u0440\u0445\u043d\u043e\u0441\u0442\u043d\u043e\u0433\u043e \u043d\u0430\u0442\u044f\u0436\u0435\u043d\u0438\u044f</title><style type=\"text/css\">\n"
                                                            "p, li { white-space: pre-wrap; }\n"
                                                            "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\" bgcolor=\"#ffffff\">\n"
                                                            "<p style=\"-qt-paragraph-type:empty; margin-top:40px; margin-bottom:21px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><br /></p>\n"
                                                            "<p style=\" margin-top:40px; margin-bottom:21px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" f"
                                                            "ont-family:'Times New Roman','Times','serif'; font-size:14pt; color:#000000;\">\u0414\u0430\u043d\u043d\u044b\u0439 \u043c\u0435\u0442\u043e\u0434 \u0434\u043e\u0432\u043e\u043b\u044c\u043d\u043e \u0442\u043e\u0447\u043d\u044b\u0439 \u0438 \u043d\u0435\u0441\u043b\u043e\u0436\u043d\u044b\u0439, \u0447\u0442\u043e \u0434\u0435\u043b\u0430\u0435\u0442 \u0435\u0433\u043e \u0440\u0430\u0441\u043f\u0440\u043e\u0441\u0442\u0440\u0430\u043d\u0435\u043d\u043d\u044b\u043c \u0434\u043b\u044f \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u044f \u043f\u043e\u0432\u0435\u0440\u0445\u043d\u043e\u0441\u0442\u043d\u043e\u0433\u043e \u043d\u0430\u0442\u044f\u0436\u0435\u043d\u0438\u044f. \u041e\u043d \u0437\u0430\u043a\u043b\u044e\u0447\u0430\u0435\u0442\u0441\u044f \u0432 \u0438\u0441\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u043d\u0438\u0438 \u043f\u043e\u0434\u044a\u0435\u043c\u0430 \u0436\u0438\u0434\u043a\u043e\u0441\u0442\u0438 \u0432 \u043a\u0430\u043f\u0438\u043b\u043b\u044f\u0440\u043d\u043e\u0439 \u0442"
                                                            "\u0440\u0443\u0431\u043a\u0435. \u041f\u043e\u0434\u043d\u044f\u0442\u0438\u0435 \u0436\u0438\u0434\u043a\u043e\u0441\u0442\u0438 \u0432 \u043a\u0430\u043f\u0438\u043b\u043b\u044f\u0440\u0435 \u043c\u043e\u0436\u043d\u043e \u043e\u0431\u044a\u044f\u0441\u043d\u0438\u0442\u044c, \u0435\u0441\u043b\u0438 \u043f\u0440\u0435\u0434\u043f\u043e\u043b\u043e\u0436\u0438\u0442\u044c, \u0447\u0442\u043e \u0436\u0438\u0434\u043a\u043e\u0441\u0442\u044c \u043f\u0440\u0438\u043b\u0438\u043f\u0430\u0435\u0442 \u043a \u0441\u0442\u0435\u043d\u043a\u0430\u043c \u043a\u0430\u043f\u0438\u043b\u043b\u044f\u0440\u0430 \u0432 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u0435 \u0441\u043c\u0430\u0447\u0438\u0432\u0430\u043d\u0438\u044f \u0441\u0442\u0435\u043d\u043e\u043a \u0438 \u0442\u044f\u043d\u0435\u0442\u0441\u044f \u0432\u0432\u0435\u0440\u0445. \u0418\u0437\u0432\u0435\u0441\u0442\u043d\u043e, \u0447\u0442\u043e \u0436\u0438\u0434\u043a\u043e\u0441\u0442\u044c \u043f\u043e\u0434\u043d\u0438\u043c\u0435\u0442\u0441"
                                                            "\u044f \u0438\u043b\u0438 \u043e\u043f\u0443\u0441\u0442\u0438\u0442\u0441\u044f \u0434\u043e \u0442\u043e\u0433\u043e \u0443\u0440\u043e\u0432\u043d\u044f, \u043f\u043e\u043a\u0430 \u0434\u043e\u0431\u0430\u0432\u043e\u0447\u043d\u043e\u0435 \u0434\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043f\u043e\u0434 \u043c\u0435\u043d\u0438\u0441\u043a\u043e\u043c \u043d\u0435 \u0443\u0440\u0430\u0432\u043d\u043e\u0432\u0435\u0441\u0438\u0442 \u0433\u0438\u0434\u0440\u043e\u0441\u0442\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0432\u0435\u0441 \u0441\u0442\u043e\u043b\u0431\u0430 \u0436\u0438\u0434\u043a\u043e\u0441\u0442\u0438. </span></p>\n"
                                                            "<p style=\" margin-top:0px; margin-bottom:21px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:'Times New Roman','Times','serif'; font-size:14pt; color:#000000;\">\u0415\u0441\u043b\u0438 \u0436\u0438\u0434\u043a\u043e\u0441\u0442\u044c \u043f\u043e\u043b\u043d\u043e\u0441\u0442\u044c\u044e "
                                                            "\u0441\u043c\u0430\u0447\u0438\u0432\u0430\u0435\u0442 \u043f\u043e\u0432\u0435\u0440\u0445\u043d\u043e\u0441\u0442\u044c \u043a\u0430\u043f\u0438\u043b\u043b\u044f\u0440\u0430, \u0442\u043e \u0440\u0430\u0434\u0438\u0443\u0441 \u043a\u0440\u0438\u0432\u0438\u0437\u043d\u044b \u043c\u0435\u043d\u0438\u0441\u043a\u0430 \\( R \\) \u0441\u043e\u0432\u043f\u0430\u0434\u0430\u0435\u0442 \u0441 \u0432\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u043c \u0440\u0430\u0434\u0438\u0443\u0441\u043e\u043c \u043a\u0430\u043f\u0438\u043b\u043b\u044f\u0440\u0430 \\( r \\). \u0412 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0438\u0438 \u0441 \u0444\u043e\u0440\u043c\u0443\u043b\u043e\u0439 \u041b\u0430\u043f\u043b\u0430\u0441\u0430 \u0438\u043c\u0435\u0435\u043c </span></p>\n"
                                                            "<p align=\"center\" style=\" margin-top:25px; margin-bottom:25px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:'Times New Roman','Times','serif'; font-size"
                                                            ":14pt; color:#000000;\">\\[ \\Delta P = \\frac{2\\alpha}{R} = \\frac{2\\alpha}{r} \\] </span></p>\n"
                                                            "<p style=\" margin-top:0px; margin-bottom:21px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:'Times New Roman','Times','serif'; font-size:14pt; color:#000000;\">\u0422\u043e\u0433\u0434\u0430 \u0438\u0437 \u0440\u0430\u0432\u0435\u043d\u0441\u0442\u0432\u0430 \u0434\u043e\u0431\u0430\u0432\u043e\u0447\u043d\u043e\u0433\u043e \u0434\u0430\u0432\u043b\u0435\u043d\u0438\u044f \\( \\Delta P \\) \u0438 \u0433\u0438\u0434\u0440\u043e\u0441\u0442\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u0433\u043e \u0434\u0430\u0432\u043b\u0435\u043d\u0438\u044f \\( P = \\rho g h \\) \u043f\u043e\u043b\u0443\u0447\u0430\u0435\u043c </span></p>\n"
                                                            "<p align=\"center\" style=\" margin-top:25px; margin-bottom:25px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:'Times New Roman','T"
                                                            "imes','serif'; font-size:14pt; color:#000000;\">\\[ \\Delta P = \\frac{2\\alpha}{r} = \\rho g h \\] </span></p>\n"
                                                            "<p style=\" margin-top:0px; margin-bottom:21px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:'Times New Roman','Times','serif'; font-size:14pt; color:#000000;\">\u0433\u0434\u0435 \\( \\rho \\) \u2013 \u043f\u043b\u043e\u0442\u043d\u043e\u0441\u0442\u044c \u0436\u0438\u0434\u043a\u043e\u0441\u0442\u0438, \\( g \\) \u2013 \u0443\u0441\u043a\u043e\u0440\u0435\u043d\u0438\u0435 \u0441\u0438\u043b\u044b \u0442\u044f\u0436\u0435\u0441\u0442\u0438, \\( h \\) \u2013 \u0432\u044b\u0441\u043e\u0442\u0430 \u0435\u0435 \u043f\u043e\u0434\u043d\u044f\u0442\u0438\u044f \u0432 \u043a\u0430\u043f\u0438\u043b\u043b\u044f\u0440\u0435, \\( \\alpha \\) \u2013 \u043a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442 \u043f\u043e\u0432\u0435\u0440\u0445\u043d\u043e\u0441\u0442\u043d\u043e\u0433\u043e \u043d\u0430\u0442\u044f\u0436\u0435"
                                                            "\u043d\u0438\u044f \u0436\u0438\u0434\u043a\u043e\u0441\u0442\u0438. \u041e\u043f\u0440\u0435\u0434\u0435\u043b\u044f\u0435\u043c \\( \\alpha \\) \u0447\u0435\u0440\u0435\u0437 \u0434\u043e\u0431\u0430\u0432\u043e\u0447\u043d\u043e\u0435 \u0434\u0430\u0432\u043b\u0435\u043d\u0438\u0435: </span></p>\n"
                                                            "<p align=\"center\" style=\" margin-top:25px; margin-bottom:25px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:'Times New Roman','Times','serif'; font-size:14pt; color:#000000;\">\\[ \\alpha = \\frac{1}{2} \\rho g h r \\] </span></p>\n"
                                                            "<p style=\" margin-top:0px; margin-bottom:21px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:'Times New Roman','Times','serif'; font-size:14pt; color:#000000;\">\u041f\u0440\u0438 \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u0438 \u043e\u043f\u044b\u0442\u0430 \u0441 \u0434\u0432\u0443\u043c\u044f \u043a\u0430\u043f\u0438"
                                                            "\u043b\u043b\u044f\u0440\u0430\u043c\u0438, \u0440\u0430\u0434\u0438\u0443\u0441\u044b \u043a\u043e\u0442\u043e\u0440\u044b\u0445 \\( r_1 \\) \u0438 \\( r_2 \\), \u043a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442 \u043f\u043e\u0432\u0435\u0440\u0445\u043d\u043e\u0441\u0442\u043d\u043e\u0433\u043e \u043d\u0430\u0442\u044f\u0436\u0435\u043d\u0438\u044f \u0431\u0443\u0434\u0435\u0442 \u0440\u0430\u0432\u0435\u043d: </span></p>\n"
                                                            "<p align=\"center\" style=\" margin-top:25px; margin-bottom:25px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:'Times New Roman','Times','serif'; font-size:14pt; color:#000000;\">\\[ \\alpha = \\frac{1}{2} \\rho g h_1 r_1 = \\frac{1}{2} \\rho g h_2 r_2 \\] </span></p>\n"
                                                            "<p style=\" margin-top:0px; margin-bottom:21px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:'Times New Roman','Times','serif'; font-size:14pt; color:#0"
                                                            "00000;\">\u041e\u0442\u0441\u044e\u0434\u0430 \u043f\u043e\u043b\u0443\u0447\u0430\u0435\u043c </span></p>\n"
                                                            "<p align=\"center\" style=\" margin-top:25px; margin-bottom:25px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:'Times New Roman','Times','serif'; font-size:14pt; color:#000000;\">\\[ h_1 - h_2 = \\Delta H = \\frac{2\\alpha}{\\rho g r_1} - \\frac{2\\alpha}{\\rho g r_2} \\] </span></p>\n"
                                                            "<p style=\" margin-top:0px; margin-bottom:21px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:'Times New Roman','Times','serif'; font-size:14pt; color:#000000;\">\u0421\u043b\u0435\u0434\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u043d\u043e, \u043e\u043a\u043e\u043d\u0447\u0430\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u0444\u043e\u0440\u043c\u0443\u043b\u0430 \u0434\u043b\u044f \u0440\u0430\u0441\u0447\u0435\u0442\u0430 \u043a\u043e\u044d\u0444\u0444\u0438\u0446\u0438"
                                                            "\u0435\u043d\u0442\u0430 \u043f\u043e\u0432\u0435\u0440\u0445\u043d\u043e\u0441\u0442\u043d\u043e\u0433\u043e \u043d\u0430\u0442\u044f\u0436\u0435\u043d\u0438\u044f \u0432 \u044d\u0442\u043e\u043c \u0441\u043b\u0443\u0447\u0430\u0435 \u0431\u0443\u0434\u0435\u0442 \u0438\u043c\u0435\u0442\u044c \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0438\u0439 \u0432\u0438\u0434: </span></p>\n"
                                                            "<p align=\"center\" style=\" margin-top:25px; margin-bottom:25px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:'Times New Roman','Times','serif'; font-size:14pt; color:#000000;\">\\[ \\alpha = \\frac{\\rho g r_1 r_2}{2 (r_2 - r_1)} \\Delta H \\] </span></p>\n"
                                                            "<p style=\" margin-top:0px; margin-bottom:21px; margin-left:37px; margin-right:37px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:'Times New Roman','Times','serif'; font-size:14pt; color:#000000;\">\u0433\u0434\u0435 \\( \\Delta H \\) \u2013 \u0440\u0430\u0437\u043d"
                                                            "\u043e\u0441\u0442\u044c \u043e\u0442\u0441\u0447\u0435\u0442\u043e\u0432 \u043c\u0435\u0436\u0434\u0443 \u043d\u0438\u0436\u043d\u0438\u043c\u0438 \u0438 \u0432\u0435\u0440\u0445\u043d\u0438\u043c\u0438 \u043a\u0440\u0430\u044f\u043c\u0438 \u043c\u0435\u043d\u0438\u0441\u043a\u043e\u0432 \u0432 \u043a\u0430\u043f\u0438\u043b\u043b\u044f\u0440\u0430\u0445. </span></p></body></html>",
                                                            None))
        self.label_3.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u0412\u044b\u0432\u043e\u0434 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u043e\u0432 \u044d\u043a\u0441\u043f\u0435\u0440\u0438\u043c\u0435\u043d\u0442\u0430",
                                                        None))
        self.label_4.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u0422\u0435\u043a\u0443\u0449\u0438\u0439 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442:",
                                                        None))
        self.textBrowser_12.setHtml(QCoreApplication.translate("MainWindow",
                                                               u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                               "p, li { white-space: pre-wrap; }\n"
                                                               "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">[\u041d / \u043c]</span></p></body></html>",
                                                               None))
        self.textBrowser_13.setHtml(QCoreApplication.translate("MainWindow",
                                                               u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                               "p, li { white-space: pre-wrap; }\n"
                                                               "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">\u03b1 = </span></p></body></html>",
                                                               None))
        self.lineEdit_6.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow",
                                                           u"\u0412\u0432\u0435\u0441\u0442\u0438 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0432 \u0442\u0430\u0431\u043b\u0438\u0446\u0443",
                                                           None))
        self.label_5.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u0421\u0432\u043e\u0434\u043a\u0430 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u043e\u0432:",
                                                        None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow",
                                                                                               u"\u041c\u0435\u0442\u043e\u0434 \u043a\u0430\u043f\u0438\u043b\u043b\u044f\u0440\u043d\u044b\u0439",
                                                                                               None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow",
                                                                                                 u"\u041c\u0435\u0442\u043e\u0434 \u043e\u0442\u0440\u044b\u0432\u0430 \u043a\u043e\u043b\u044c\u0446\u0430",
                                                                                                 None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow",
                                                                                                 u"\u041c\u0435\u0442\u043e\u0434 \u043f\u043b\u0430\u0441\u0442\u0438\u043d\u044b",
                                                                                                 None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow",
                                                                                                 u"\u041c\u0435\u0442\u043e\u0434 \u0432\u0438\u0441\u044f\u0447\u0435\u0439 \u043a\u0430\u043f\u043b\u0438",
                                                                                                 None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("MainWindow",
                                                                                                 u"\u041c\u0435\u0442\u043e\u0434 \u043e\u0441\u0446\u0438\u043b\u043b\u0438\u0440\u0443\u044e\u0449\u0435\u0439 \u0441\u0442\u0440\u0443\u0438",
                                                                                                 None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), QCoreApplication.translate("MainWindow",
                                                                                                 u"\u041c\u0435\u0442\u043e\u0434 \u043f\u0443\u0437\u044b\u0440\u044c\u043a\u043e\u0432\u043e\u0433\u043e \u0434\u0430\u0432\u043b\u0435\u043d\u0438\u044f",
                                                                                                 None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), QCoreApplication.translate("MainWindow",
                                                                                                 u"\u041c\u0435\u0442\u043e\u0434 \u0441\u0447\u0435\u0442\u043d\u044b\u0445 \u043a\u0430\u043f\u0435\u043b\u044c",
                                                                                                 None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), QCoreApplication.translate("MainWindow",
                                                                                                  u"\u0420\u0430\u0441\u0447\u0435\u0442 \u043f\u043e\u0433\u0440\u0435\u0448\u043d\u043e\u0441\u0442\u0435\u0439",
                                                                                                  None))
        # retranslateUi

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)

        self.showMaximized()

    # setupUi




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Ui_MainWindow()
    main.show()
    app.exec_()



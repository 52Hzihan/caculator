# -*- coding: utf-8 -*-

from layout import *
from state import State


if __name__ == "__main__":

    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    MainWindow.setFixedSize(MainWindow.size())

    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from ui.createQuestion import Ui_createQuestion
from ui.test import Ui_Test
from ui.reviewCompletedTests import Ui_ReviewTests


class Ui_MainWindow(object):

    # define actions as 'constants' rather than just passing random strings around
    CREATE_ARITHMETIC_QUESTION = 1
    TAKE_A_TEST = 2
    REVIEW_COMPLETED_TESTS = 3

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.arithmeticQuestionButton = QtWidgets.QPushButton(self.centralwidget)
        self.arithmeticQuestionButton.setGeometry(QtCore.QRect(190, 20, 391, 31))
        self.arithmeticQuestionButton.setObjectName("arithmeticQuestionButton")
        self.arithmeticQuestionButton.clicked.connect(lambda: self.openDialog(self.CREATE_ARITHMETIC_QUESTION))

        self.takeTestButton = QtWidgets.QPushButton(self.centralwidget)
        self.takeTestButton.setGeometry(QtCore.QRect(190, 70, 391, 31))
        self.takeTestButton.setObjectName("takeTestButton")
        self.takeTestButton.clicked.connect(lambda: self.openDialog(self.TAKE_A_TEST))

        self.reviewTestsButton = QtWidgets.QPushButton(self.centralwidget)
        self.reviewTestsButton.setGeometry(QtCore.QRect(190, 120, 391, 31))
        self.reviewTestsButton.setObjectName("reviewTestsButton")
        self.reviewTestsButton.clicked.connect(lambda: self.openDialog(self.REVIEW_COMPLETED_TESTS))

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.arithmeticQuestionButton.setText(_translate("MainWindow", "Create an Arithmetic Question"))
        self.takeTestButton.setText(_translate("MainWindow", "Take a Test"))
        self.reviewTestsButton.setText(_translate("MainWindow", "Review Completed Tests"))

    def openDialog(self, dialogType):
        self.ui = None
        if dialogType == self.CREATE_ARITHMETIC_QUESTION:
            self.ui = Ui_createQuestion()
        elif dialogType == self.TAKE_A_TEST:
            self.ui = Ui_Test()
        elif dialogType == self.REVIEW_COMPLETED_TESTS:
            self.ui = Ui_ReviewTests()
        else:
            return False

        self.dialog = QtWidgets.QDialog()
        self.ui.setupUi(self.dialog)
        self.dialog.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


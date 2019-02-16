# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'createTest.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_createQuestion(object):
    def setupUi(self, createQuestion):
        createQuestion.setObjectName("createQuestion")
        createQuestion.resize(399, 591)
        self.buttonBox = QtWidgets.QDialogButtonBox(createQuestion)
        self.buttonBox.setGeometry(QtCore.QRect(30, 550, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.label_6 = QtWidgets.QLabel(createQuestion)
        self.label_6.setGeometry(QtCore.QRect(30, 10, 321, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(createQuestion)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 81, 17))
        self.label_2.setObjectName("label_2")
        self.testNameInput = QtWidgets.QLineEdit(createQuestion)
        self.testNameInput.setGeometry(QtCore.QRect(160, 60, 211, 21))
        self.testNameInput.setObjectName("testNameInput")
        self.line = QtWidgets.QFrame(createQuestion)
        self.line.setGeometry(QtCore.QRect(30, 90, 341, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(createQuestion)
        self.label.setGeometry(QtCore.QRect(30, 110, 311, 21))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(createQuestion)
        self.lineEdit.setGeometry(QtCore.QRect(30, 140, 231, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(createQuestion)
        self.pushButton.setGeometry(QtCore.QRect(260, 140, 101, 25))
        self.pushButton.setObjectName("pushButton")
        self.listWidget = QtWidgets.QListWidget(createQuestion)
        self.listWidget.setGeometry(QtCore.QRect(30, 180, 331, 271))
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.pushButton_2 = QtWidgets.QPushButton(createQuestion)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 460, 181, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(createQuestion)
        self.label_3.setGeometry(QtCore.QRect(40, 510, 341, 31))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(createQuestion)
        self.buttonBox.accepted.connect(createQuestion.accept)
        self.buttonBox.rejected.connect(createQuestion.close)
        QtCore.QMetaObject.connectSlotsByName(createQuestion)

    def retranslateUi(self, createQuestion):
        _translate = QtCore.QCoreApplication.translate
        createQuestion.setWindowTitle(_translate("createQuestion", "Dialog"))
        self.label_6.setText(_translate("createQuestion", "Create a Test"))
        self.label_2.setText(_translate("createQuestion", "Test Name:"))
        self.label.setText(_translate("createQuestion", "Find questions by searching for a tag:"))
        self.pushButton.setText(_translate("createQuestion", "Search"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("createQuestion", "item 2"))
        item = self.listWidget.item(1)
        item.setText(_translate("createQuestion", "item 3"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_2.setText(_translate("createQuestion", "Add selected to Test"))
        self.label_3.setText(_translate("createQuestion", "Once finished adding questions, save the test!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    createQuestion = QtWidgets.QDialog()
    ui = Ui_createQuestion()
    ui.setupUi(createQuestion)
    createQuestion.show()
    sys.exit(app.exec_())


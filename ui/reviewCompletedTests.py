# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reviewCompletedTests.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ReviewTests(object):
    def setupUi(self, ReviewTests):
        ReviewTests.setObjectName("ReviewTests")
        ReviewTests.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(ReviewTests)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(ReviewTests)
        self.label.setGeometry(QtCore.QRect(100, 10, 191, 61))
        self.label.setObjectName("label")

        self.retranslateUi(ReviewTests)
        self.buttonBox.accepted.connect(ReviewTests.accept)
        self.buttonBox.rejected.connect(ReviewTests.reject)
        QtCore.QMetaObject.connectSlotsByName(ReviewTests)

    def retranslateUi(self, ReviewTests):
        _translate = QtCore.QCoreApplication.translate
        ReviewTests.setWindowTitle(_translate("ReviewTests", "Dialog"))
        self.label.setText(_translate("ReviewTests", "Review Completed Dialog"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ReviewTests = QtWidgets.QDialog()
    ui = Ui_ReviewTests()
    ui.setupUi(ReviewTests)
    ReviewTests.show()
    sys.exit(app.exec_())


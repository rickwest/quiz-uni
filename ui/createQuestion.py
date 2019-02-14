# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'createQuestion.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from question.AutoMarkedQuestion import TfQuestion, Calculation
from question.Question import QuestionBank

class Ui_createQuestion(object):
    def setupUi(self, createQuestion):
        createQuestion.setObjectName("createQuestion")
        createQuestion.resize(400, 300)

        self.buttonBox = QtWidgets.QDialogButtonBox(createQuestion)
        self.buttonBox.setGeometry(QtCore.QRect(40, 260, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")

        self.questionInput = QtWidgets.QLineEdit(createQuestion)
        self.questionInput.setGeometry(QtCore.QRect(160, 20, 211, 21))
        self.questionInput.setObjectName("questionInput")

        self.answerInput = QtWidgets.QLineEdit(createQuestion)
        self.answerInput.setGeometry(QtCore.QRect(160, 50, 211, 21))
        self.answerInput.setObjectName("answerInput")

        self.label = QtWidgets.QLabel(createQuestion)
        self.label.setGeometry(QtCore.QRect(30, 20, 81, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(createQuestion)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 111, 20))
        self.label_2.setObjectName("label_2")

        self.tags = QtWidgets.QLineEdit(createQuestion)
        self.tags.setGeometry(QtCore.QRect(30, 150, 341, 41))
        self.tags.setObjectName("tags")

        self.label_4 = QtWidgets.QLabel(createQuestion)
        self.label_4.setGeometry(QtCore.QRect(30, 120, 341, 31))
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(createQuestion)
        self.label_3.setGeometry(QtCore.QRect(30, 80, 67, 17))
        self.label_3.setObjectName("label_3")

        self.points = QtWidgets.QComboBox(createQuestion)
        self.points.setGeometry(QtCore.QRect(160, 80, 211, 25))
        self.points.setObjectName("points")
        self.points.addItem("")
        self.points.addItem("")
        self.points.addItem("")
        self.points.addItem("")
        self.points.addItem("")
        self.points.addItem("")
        self.points.addItem("")
        self.points.addItem("")
        self.points.addItem("")
        self.points.setItemText(9, "")

        self.retranslateUi(createQuestion)
        self.buttonBox.accepted.connect(self.createQuestion)
        self.buttonBox.rejected.connect(createQuestion.close)
        QtCore.QMetaObject.connectSlotsByName(createQuestion)

    def retranslateUi(self, createQuestion):
        _translate = QtCore.QCoreApplication.translate
        createQuestion.setWindowTitle(_translate("createQuestion", "Dialog"))
        self.label.setText(_translate("createQuestion", "Question:"))
        self.label_2.setText(_translate("createQuestion", "Correct Answer:"))
        self.label_4.setText(_translate("createQuestion", "Tags (Enter values, separated by a comma):"))
        self.label_3.setText(_translate("createQuestion", "Points:"))
        self.points.setItemText(0, _translate("createQuestion", "10"))
        self.points.setItemText(1, _translate("createQuestion", "15"))
        self.points.setItemText(2, _translate("createQuestion", "20"))
        self.points.setItemText(3, _translate("createQuestion", "25"))
        self.points.setItemText(4, _translate("createQuestion", "30"))
        self.points.setItemText(5, _translate("createQuestion", "35"))
        self.points.setItemText(6, _translate("createQuestion", "40"))
        self.points.setItemText(7, _translate("createQuestion", "45"))
        self.points.setItemText(8, _translate("createQuestion", "50"))

    def createQuestion(self):
        # We currently only deal with multiple choice questions or arithmetic questions, therefore we can simply determine
        # the type of question from the answer input.

        answerInput = self.answerInput.text()
        questionInput = self.questionInput.text()

        if not answerInput or not questionInput:
            return False

        tags = self.tags.text()
        points = self.points.currentText()

        # create a question of relevant type
        if answerInput.lower == 'true':
            question = TfQuestion(questionInput, answerInput, tags, points)
        else:
            question = Calculation(questionInput, answerInput, tags, points)

        # get singleton questionBank and add new question
        questionBank = QuestionBank.getInstance()
        questionBank.add(question)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    createQuestion = QtWidgets.QDialog()
    ui = Ui_createQuestion()
    ui.setupUi(createQuestion)
    createQuestion.show()
    sys.exit(app.exec_())


from PyQt5 import QtWidgets
from ui.main import MainWindowUi
from question.Question import QuestionBank

"""The application entry point"""


class App:
    @staticmethod
    def setup():
        import sys

        # When first running the application, we set up our QuestionBank singleton.
        # By doing this here, we ensure that if we have a question bank persisted,
        # then it will be loaded into memory straight away.
        QuestionBank.getInstance()

        # set up the ui
        app = QtWidgets.QApplication(sys.argv)
        mainWindow = QtWidgets.QMainWindow()
        ui = MainWindowUi()
        ui.setupUi(mainWindow)
        mainWindow.show()
        sys.exit(app.exec_())


if __name__ == "__main__":
    App.setup()

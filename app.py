from PyQt5 import QtWidgets
from ui.main import MainWindowUi


"""The application entry point"""


class App:
    @staticmethod
    def setup():
        import sys
        app = QtWidgets.QApplication(sys.argv)
        mainWindow = QtWidgets.QMainWindow()
        ui = MainWindowUi()
        ui.setupUi(mainWindow)
        mainWindow.show()
        sys.exit(app.exec_())


if __name__ == "__main__":
    App.setup()

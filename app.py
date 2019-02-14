from PyQt5 import QtWidgets
from ui.main import Ui_MainWindow

'''The application entry point'''


class App:
    @staticmethod
    def setup():
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())


if __name__ == "__main__":
    App.setup()

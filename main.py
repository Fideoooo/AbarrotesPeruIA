from PyQt5 import QtWidgets
from Backend.login_backend import LoginWindow
import sys, res

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = LoginWindow()
    window.show()
    app.exec()
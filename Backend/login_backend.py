from PyQt5 import QtWidgets, QtGui
import webbrowser
from Backend.database import Database
from Diseno.login_ui import Ui_Form
from Backend.menu_inicio_backend import MenuInicioWindow   


class LoginWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
 
        # Conectar a la DB
        self.db = Database()

        # Conectar botones
        self.ui.pushButton.clicked.connect(self.login)          # Botón "Ingresar"
        self.ui.pushButton_2.clicked.connect(self.open_github)  # Botón con logo GitHub

    def login(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        
        user = self.db.validar_usuario(username, password)
        if user:
            QtWidgets.QMessageBox.information(self, "Login correcto", f"¡Bienvenido {user.Nombre}!")
            self.empleado_id = user.EmpleadoID
            self.menu = MenuInicioWindow(self.empleado_id)   # ✅ Usa la clase importada
            self.menu.show()
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Usuario o contraseña incorrectos")

    def open_github(self):
        webbrowser.open("https://github.com/Fideoooo")

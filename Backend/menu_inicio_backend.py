import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
from Diseno.menu_inicio_ui import Ui_Form
from Backend.database import Database
from Backend.camera_backend import CameraThread
from Backend.ventas_ydetalles_backend import VentasBackend




# NOTA: ya no importa VerStockWindow al inicio, sino dentro de abrir_stock()
class MenuInicioWindow(QtWidgets.QWidget):
    def __init__(self, empleado_id):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Guardamos el empleado_id
        self.empleado_id = empleado_id
        print("MenuInicioWindow inicializado")

        # Conectar botones
        self.ui.pushButton.clicked.connect(self.abrir_ver_stock)
        self.ui.pushButton_2.clicked.connect(self.abrir_ver_productos)
        self.ui.pushButton_3.clicked.connect(self.abrir_categorias)
        self.ui.pushButton_4.clicked.connect(self.abrir_marcas)
        self.ui.pushButton_5.clicked.connect(self.abrir_ventas)
        self.ui.btn_close.clicked.connect(self.close)  # Botón cerrar


    def abrir_ver_stock(self):
        # Import local para evitar importación circular
        from Backend.ver_stock_backend import VerStockWindow
        self.ver_stock = VerStockWindow(self.empleado_id)
        self.ver_stock.show()
        self.close()

    def abrir_ver_productos(self):
        # Import local para evitar importación circular
        from Backend.ver_productos_backend import VerProductoWindow

        self.ver_producto = VerProductoWindow(self.empleado_id)
        self.ver_producto.show()
        self.close()

    def abrir_categorias(self):
        from Backend.categoria_backend import CategoriasWindow
        self.categorias_window = CategoriasWindow(self.empleado_id)
        self.categorias_window.show()
        self.close()


    def abrir_marcas(self):
        from Backend.marcas_backend import MarcasWindow
        self.marcas_window = MarcasWindow(self.empleado_id)
        self.marcas_window.show()
        self.close()

    def abrir_ventas(self):
        self.ventas_detalles = VentasBackend(self.empleado_id)
        print("Empleado ID:", self.empleado_id)
        self.ventas_detalles.show()
        self.close()
    

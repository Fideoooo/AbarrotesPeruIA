# ver_stock_backend.py
from PyQt5 import QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from Backend.database import Database

class VerStockWindow(QtWidgets.QWidget):
    def __init__(self, empleado_id):
        super().__init__()
        from Diseno.ver_stock_ui import Ui_Form  # importa tu diseño real
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.empleado_id = empleado_id
        self.db = Database()
        

        # ---------------- CONFIGURAR TABLA ----------------
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["ProductoID", "Nombre del producto", "Stock actual"])
        self.ui.tableView.setModel(self.model)

        # Cargar datos al iniciar
        self.cargar_datos()

        # ---------------- BOTONES RETROCEDER Y CERRAR ----------------
        self.ui.btn_retroceder.clicked.connect(self.retroceder)
        self.ui.btn_cerrar.clicked.connect(self.close)
        # -------------------------------------------------------------

        # ---------------- CONEXIONES ----------------
        self.ui.toolButton.clicked.connect(self.buscar_producto)
        self.ui.pushButton.clicked.connect(self.agregar_stock)

    # -------------------------------------------------------------
    # CARGAR DATOS
    # -------------------------------------------------------------
    def cargar_datos(self):
        """Carga el inventario (ProductoID, Nombre, StockActual)"""
        self.model.removeRows(0, self.model.rowCount())
        inventario = self.db.obtener_inventario_completo()

        for item in inventario:
            row = [
                QStandardItem(str(item[0])),  # ProductoID
                QStandardItem(str(item[1])),  # Nombre del producto
                QStandardItem(str(item[2]))   # StockActual
            ]
            self.model.appendRow(row)

        self.ui.tableView.resizeColumnsToContents()

    # -------------------------------------------------------------
    # BUSCAR PRODUCTO
    # -------------------------------------------------------------
    def buscar_producto(self):
        """Filtra el inventario según el texto ingresado"""
        nombre = self.ui.lineEdit.text().strip()
        self.model.removeRows(0, self.model.rowCount())

        inventario = self.db.buscar_inventario_por_nombre(nombre)
        for item in inventario:
            row = [
                QStandardItem(str(item[0])),
                QStandardItem(str(item[1])),
                QStandardItem(str(item[2]))
            ]
            self.model.appendRow(row)

        self.ui.tableView.resizeColumnsToContents()
     #BOTON AGREGAR STOCK
    def agregar_stock(self):
        """Maneja la acción del botón Agregar (sumar cantidad al stock)."""
        # Verificar selección válida
        seleccion = self.ui.tableView.selectionModel().currentIndex()
        if not seleccion.isValid():
            QtWidgets.QMessageBox.warning(self, "Seleccionar producto", "Por favor selecciona un producto primero.")
            return

        fila = seleccion.row()
        try:
            producto_id = int(self.model.item(fila, 0).text())
        except Exception:
            QtWidgets.QMessageBox.warning(self, "Error", "ID de producto inválido.")
            return

        nombre_producto = self.model.item(fila, 1).text() if self.model.item(fila, 1) else ""

        # Pedir cantidad con cuadro emergente (solo enteros >= 1)
        cantidad, ok = QtWidgets.QInputDialog.getInt(
            self,
            f"Agregar stock a {nombre_producto}",
            "Ingrese la cantidad a agregar:",
            value=1, min=1, step=1
        )
        if not ok:
            return  # usuario canceló

        # Registrar movimiento (usa empleado_id pasado desde MenuInicioWindow)
        empleado_id = getattr(self, "empleado_id", None)
        if empleado_id is None:
            QtWidgets.QMessageBox.warning(self, "Error", "Empleado no identificado. Vuelve a iniciar sesión.")
            return

        success = self.db.registrar_movimiento(producto_id, cantidad, "Entrada", empleado_id)
        if success:
            QtWidgets.QMessageBox.information(self, "Éxito", f"Se registró una entrada de {cantidad} unidades para {nombre_producto}.")
            self.cargar_datos()
        else:
            QtWidgets.QMessageBox.critical(self, "Error", "No se pudo registrar el movimiento.")

    #retroceder
    def retroceder(self):
        """Cierra la ventana de VerStock y abre la ventana principal."""
        from Backend.menu_inicio_backend import MenuInicioWindow
        self.menu_inicio = MenuInicioWindow(self.empleado_id)
        self.menu_inicio.show()
        self.close()

    # -------------------------------------------------------------
    # VOLVER AL MENÚ
    # -------------------------------------------------------------
    def volver_menu(self):
        """Cierra la ventana y vuelve al menú principal"""
        from Backend.menu_inicio_backend import MenuInicioWindow
        self.menu_inicio = MenuInicioWindow(self.empleado_id)
        self.menu_inicio.show()
        self.close()
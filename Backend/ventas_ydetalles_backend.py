from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox, QInputDialog
from Diseno.ventas_ydetalles_ui import Ui_Form  # Tu UI
from Backend.camera_backend import CameraThread
from PyQt5.QtCore import Qt
from Backend.database import Database
import sys

class VentasBackend(QtWidgets.QWidget):
    def __init__(self, empleado_id):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.db = Database() # Instancia de la base de datos
        self.empleado_id = empleado_id  # <-- guardamos el ID del empleado actual

        # Lista temporal de ventas antes de guardar en DB
        self.venta_temporal = []
        self.total = 0.0

        # Cargar productos en el combobox   
        self.load_products()

        # Conectar botones
        self.ui.pushButton.clicked.connect(self.add_product)       # Agregar producto temporal
        self.ui.pushButton_2.clicked.connect(self.finalize_sale)   # Finalizar venta
        self.ui.pushButton_3.clicked.connect(self.cancel_sale)     # Cancelar venta
        self.ui.pushButton_4.clicked.connect(self.open_historico_ventas)
        self.ui.pushButton_5.clicked.connect(self.abrir_agregar_producto_cam) #Boton Agregar Producto camara



       # ---------------- BOTONES RETROCEDER Y CERRAR ----------------
        self.ui.backButton.clicked.connect(self.retroceder)  # Retroceder a menú principal
        self.ui.closeButton.clicked.connect(self.close)      # Cerrar ventana
        # -----------------------------------------------------------

        # Inicializar tabla y total
        self.update_table()

    # --- Cargar productos desde DB ---
    def load_products(self):
        productos = self.db.obtener_productos()
        self.products_dict = {}
        self.ui.comboBox.clear()
        for row in productos:
            prod_id = row.ProductoID
            nombre = row.Nombre
            precio = row.Precio
            marca = row.Marca       # <- ahora viene del JOIN
            presentacion = row.Presentacion
            categoria = row.Categoria

            self.products_dict[nombre] = {
                "ProductoID": prod_id,
                "Precio": precio,
                "Marca": marca,
                "Presentacion": presentacion,
                "Categoria": categoria
            }
            self.ui.comboBox.addItem(nombre)

    # --- Agregar producto temporal ---
    def add_product(self):
        nombre = self.ui.comboBox.currentText()
        cantidad = self.ui.spinBox.value()
        if cantidad <= 0:
            QMessageBox.warning(self, "Error", "Cantidad debe ser mayor a 0")
            return

        producto = self.products_dict[nombre]

        # Calcular subtotal
        subtotal = cantidad * producto["Precio"]

        # Crear item con todos los datos
        item = {
            "ProductoID": producto["ProductoID"],
            "Nombre": nombre,
            "Marca": producto["Marca"],
            "Presentacion": producto["Presentacion"],
            "Cantidad": cantidad,
            "Precio": producto["Precio"],
            "Subtotal": subtotal
        }   

        self.venta_temporal.append(item) 
        self.update_table()     # Actualizar la tabla





    # --- Actualizar QTableWidget y total ---
    def update_table(self):
        self.ui.tableWidget.setRowCount(len(self.venta_temporal))
        self.ui.tableWidget.setColumnCount(7)
        self.ui.tableWidget.setHorizontalHeaderLabels(["ProductoID", "Nombre", "Marca", "Presentación", "Cantidad", "Precio Unitario", "Subtotal"])

        total = 0
        for row, item in enumerate(self.venta_temporal):
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(item["ProductoID"])))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(item["Nombre"]))
            self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(item["Marca"]))
            self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(item["Presentacion"]))
            self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(str(item["Cantidad"])))
            self.ui.tableWidget.setItem(row, 5, QTableWidgetItem(f"{item['Precio']:.2f}"))
            self.ui.tableWidget.setItem(row, 6, QTableWidgetItem(f"{item['Subtotal']:.2f}"))

            total += item["Subtotal"]

        self.total = total
        self.ui.label_8.setText(f"{self.total:.2f}")


    # --- Finalizar venta (guarda en DB usando triggers) ---
    # --- Finalizar venta (guarda en DB usando triggers) ---
    def finalize_sale(self):
        nombre = self.ui.comboBox.currentText()
        cantidad = self.ui.spinBox.value()

        if not self.venta_temporal:
            if cantidad > 0:
                QMessageBox.warning(
                    self,
                    "Error",
                    "Debes presionar 'Agregar producto' antes de finalizar la venta."
                )
            else:
                QMessageBox.warning(
                    self,
                    "Error",
                    "No hay productos para vender."
                )
            return

        # Preparar datos para DB
        detalles = [{"ProductoID": i["ProductoID"], "Cantidad": i["Cantidad"]} for i in self.venta_temporal]

        # Registrar venta pasando el empleado_id
        success, result = self.db.registrar_venta(detalles, self.empleado_id)

        if success:
            QMessageBox.information(self, "Venta", f"Venta finalizada correctamente. ID de la venta: {result}")
            self.venta_temporal = []
            self.update_table()
        else:
            QMessageBox.critical(self, "Error", f"No se pudo completar la venta:\n{result}")


    # --- Cancelar venta temporal ---
    def cancel_sale(self):
        self.venta_temporal = []
        self.update_table()
        self.ui.label_8.setText("0")



       # --- Retroceder a menú principal ---
    def retroceder(self):
        from Backend.menu_inicio_backend import MenuInicioWindow  # Import aquí para evitar import circular
        self.menu_inicio = MenuInicioWindow(self.empleado_id)
        self.menu_inicio.show()
        self.close()
    # ------------------ AGREGAR PRODUCTO CON CÁMARA ------------------
    def abrir_agregar_producto_cam(self):
        """Inicia el hilo de cámara para detección de productos"""
        self.camera_thread = CameraThread(parent=self)
        self.camera_thread.producto_detectado_signal.connect(self.mostrar_confirmacion_producto_venta)
        self.camera_thread.start()


    def mostrar_confirmacion_producto_venta(self, producto):
        """Se ejecuta cuando la IA detecta un producto"""
        self.camera_thread.running = False  # Pausar cámara mientras preguntamos
        nombre_detectado = producto["nombre"]

        # Validar si el producto existe en la base de datos
        if nombre_detectado not in self.products_dict:
            QMessageBox.critical(self, "Error", f"El producto '{nombre_detectado}' no existe en la base de datos.")
            self.camera_thread.running = True
            return

        # Confirmar si desea agregarlo al detalle de venta
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Agregar producto detectado")
        msg_box.setText(f"¿Deseas agregar el producto detectado: '{nombre_detectado}' a la venta?")
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg_box.setWindowFlag(Qt.WindowStaysOnTopHint)
        respuesta = msg_box.exec_()

        if respuesta == QMessageBox.Yes:
            # Pedimos cantidad al usuario
            cantidad, ok = QInputDialog.getInt(
                self,
                "Cantidad del producto",
                f"Ingrese la cantidad para '{nombre_detectado}':",
                1,   # valor inicial
                1,   # mínimo
                100, # máximo (puedes cambiarlo)
                1    # paso
            )

            if ok:
                # Seleccionamos el producto y agregamos con la cantidad indicada
                self.ui.comboBox.setCurrentText(nombre_detectado)
                self.ui.spinBox.setValue(cantidad)
                self.add_product()
                QMessageBox.information(self, "Agregado", f"'{nombre_detectado}' fue agregado con cantidad {cantidad}.")
            else:
                QMessageBox.information(self, "Cancelado", "No se agregó el producto detectado.")

            self.camera_thread.running = True
        else:
            self.camera_thread.running = True

    #Abre el historico de ventas
    def open_historico_ventas(self):
        from Backend.historico_ventas_backend import HistoricoVentasWindow
        print(f"DEBUG: open_historico_ventas() - empleado_id: {self.empleado_id} self visible before: {self.isVisible()}")
        self.historico_window = HistoricoVentasWindow(parent=self, empleado_id=self.empleado_id)
        self.historico_window.show()
        print(f"DEBUG: VentasBackend hidden, historico shown: {self.historico_window.isVisible()}")
        self.hide()



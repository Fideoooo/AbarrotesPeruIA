from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMessageBox, QInputDialog
from Backend.database import Database
from Diseno.ver_productos_ui import Ui_Form
from Backend.camera_backend import CameraThread


class VerProductoWindow(QtWidgets.QWidget):
    def __init__(self, empleado_id):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.empleado_id = empleado_id

        # Conectar a la BD
        self.db = Database()

        self.cargar_categorias()
        self.cargar_marcas()
        



        # Configurar modelo de tabla
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(
            ["ID", "Nombre", "Presentación", "Código Barras", "Categoría", "Marca", "Precio"]
        )
        self.ui.tableView.setModel(self.model)

        # Cargar datos al iniciar
        self.cargar_datos()

        # Inicializar estado de botones
        self.estado_inicial()

        # ---------------- BOTONES RETROCEDER Y CERRAR ----------------
        self.ui.btn_back.clicked.connect(self.retroceder)
        self.ui.btn_close.clicked.connect(self.close)
        # -------------------------------------------------------------

    def estado_inicial(self):
        """Estado inicial de la interfaz"""
        # Arriba habilitados
        self.ui.pushButton.setEnabled(True)   # Nuevo
        self.ui.pushButton_2.setEnabled(True) # Editar
        self.ui.pushButton_3.setEnabled(True) # Eliminar
        self.ui.pushButton_6.setEnabled(True) # Agregar producto con cam

        # Abajo deshabilitados
        self.ui.pushButton_4.setEnabled(False) # Agregar
        self.ui.pushButton_5.setEnabled(False) # Modificar

        # Conexiones
        self.ui.pushButton.clicked.connect(self.nuevo_producto)
        self.ui.pushButton_2.clicked.connect(self.editar_producto)
        self.ui.pushButton_3.clicked.connect(self.eliminar_producto)
        self.ui.pushButton_6.clicked.connect(self.abrir_agregar_producto_cam)

    # ------------------ NUEVO ------------------
    def nuevo_producto(self):
        self.limpiar_campos()

        # Arriba deshabilitados
        self.ui.pushButton.setEnabled(False)
        self.ui.pushButton_2.setEnabled(False)
        self.ui.pushButton_3.setEnabled(False)

        # Abajo → solo Agregar habilitado
        self.ui.pushButton_4.setEnabled(True)
        self.ui.pushButton_5.setEnabled(False)

        # Evitar conexiones múltiples
        try:
            self.ui.pushButton_4.clicked.disconnect()
        except TypeError:
            pass  # si no estaba conectado, no pasa nada

        self.ui.pushButton_4.clicked.connect(self.agregar_producto)
        

    def agregar_producto(self):
        categoria_id = self.ui.comboBox_categoria.currentData()
        marca_id = self.ui.comboBox_marca.currentData()
        """Inserta producto nuevo en la BD"""
        # Aquí tomas los datos de los QLineEdit / QComboBox de tu UI
        producto = {
            "Nombre": self.ui.lineEdit_nombre.text(),
            "Presentacion": self.ui.lineEdit_presentacion.text(),
            "CodigoBarras": self.ui.lineEdit_codigobarras.text(),
            "CategoriaID": categoria_id,
            "Marca": marca_id,
            "Precio": float(self.ui.lineEdit_precio.text())
        }

        exito, mensaje = self.db.insertar_producto(producto)

        if exito:
            QMessageBox.information(self, "Éxito", mensaje)
            self.cargar_datos()
            self.estado_inicial()
        else:
            QMessageBox.warning(self, "Atención", mensaje)

        
    #COMBO BOX CATEOGIRAS PARA LLENAR
    def cargar_categorias(self):
        categorias = self.db.obtener_categorias()
        self.ui.comboBox_categoria.clear()  

        for cat in categorias:
            categoria_id, nombre = cat
            # Mostramos el nombre pero guardamos el ID
            self.ui.comboBox_categoria.addItem(nombre, categoria_id)

    #COMBO BOX MARCA PARA LLENAR    
    def cargar_marcas(self):
        marcas = self.db.obtener_marcas()
        self.ui.comboBox_marca.clear()

        for marca in marcas:
            marca_id, nombre = marca
            self.ui.comboBox_marca.addItem(nombre, marca_id)
    
    

    # ------------------ EDITAR ------------------
    def editar_producto(self):
        """Carga los datos seleccionados en el formulario"""
        index = self.ui.tableView.currentIndex()
        if not index.isValid():
            QMessageBox.warning(self, "Atención", "Seleccione un producto para editar.")
            return

        fila = index.row()
        producto_id = self.model.item(fila, 0).text()
        nombre = self.model.item(fila, 1).text()
        presentacion = self.model.item(fila, 2).text()
        cod_barras = self.model.item(fila, 3).text()
        categoria = self.model.item(fila, 4).text()
        marca = self.model.item(fila, 5).text()
        precio = self.model.item(fila, 6).text()

        # Rellenar campos
        self.ui.lineEdit_nombre.setText(nombre)
        self.ui.lineEdit_presentacion.setText(presentacion)
        self.ui.lineEdit_codigobarras.setText(cod_barras)
        self.ui.comboBox_categoria.setCurrentText(categoria)
        self.ui.comboBox_marca.setCurrentText(marca)
        self.ui.lineEdit_precio.setText(precio)

        # Guardar ID para actualizar
        self.producto_id_editando = producto_id

        # Arriba deshabilitados
        self.ui.pushButton.setEnabled(False)
        self.ui.pushButton_2.setEnabled(False)
        self.ui.pushButton_3.setEnabled(False)

        # Abajo → solo Modificar habilitado
        self.ui.pushButton_4.setEnabled(False)
        self.ui.pushButton_5.setEnabled(True)

        self.ui.pushButton_5.clicked.connect(self.modificar_producto)

    def modificar_producto(self):
        categoria_id = self.ui.comboBox_categoria.currentData()
        marca_id = self.ui.comboBox_marca.currentData()
        """Actualiza producto existente"""
        producto = {
            "ProductoID": self.producto_id_editando,
            "Nombre": self.ui.lineEdit_nombre.text(),
            "Presentacion": self.ui.lineEdit_presentacion.text(),
            "CodigoBarras": self.ui.lineEdit_codigobarras.text(),
            "CategoriaID": categoria_id,
            "MarcaID": marca_id,
            "Precio": float(self.ui.lineEdit_precio.text())
        }

        self.db.actualizar_producto(producto)   # <-- debe existir en database.py
        self.cargar_datos()
        self.estado_inicial()

    # ------------------ ELIMINAR ------------------
    def eliminar_producto(self):
        """Elimina producto seleccionado"""
        index = self.ui.tableView.currentIndex()
        if not index.isValid():
            QMessageBox.warning(self, "Atención", "Seleccione un producto para eliminar.")
            return

        fila = index.row()
        producto_id = self.model.item(fila, 0).text()

        confirm = QMessageBox.question(
            self,
            "Confirmar",
            f"¿Está seguro de eliminar el producto ID {producto_id}?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if confirm == QMessageBox.Yes:
            self.db.eliminar_producto(producto_id)  # <-- debe existir en database.py
            self.cargar_datos()

    # ------------------ UTILIDADES ------------------
    def cargar_datos(self):
        """Carga los productos de la BD en la tabla"""
        self.model.removeRows(0, self.model.rowCount())
        productos = self.db.obtener_productos()  # <-- debe existir en database.py

        for prod in productos:
            row = [
                QStandardItem(str(prod[0])),
                QStandardItem(str(prod[1])),
                QStandardItem(str(prod[2])),
                QStandardItem(str(prod[3])),
                QStandardItem(str(prod[4])),
                QStandardItem(str(prod[5])),
                QStandardItem(str(prod[6])),
            ]
            self.model.appendRow(row)

    def limpiar_campos(self):
        """Vacía los campos del formulario"""
        self.ui.lineEdit_nombre.clear()
        self.ui.lineEdit_presentacion.clear()
        self.ui.lineEdit_codigobarras.clear()
        self.ui.comboBox_categoria.setCurrentIndex(0)
        self.ui.comboBox_marca.setCurrentIndex(0)
        self.ui.lineEdit_precio.clear()

    def retroceder(self):
        """Cierra la ventana de VerProducto y abre la ventana principal."""
        from Backend.menu_inicio_backend import MenuInicioWindow
        self.menu_inicio = MenuInicioWindow(self.empleado_id)
        self.menu_inicio.show()
        self.close()

    def abrir_agregar_producto_cam(self):
        self.camera_thread = CameraThread(parent=self)
        self.camera_thread.producto_detectado_signal.connect(self.mostrar_confirmacion_producto)
        self.camera_thread.start()

    def mostrar_confirmacion_producto(self, producto):
        self.camera_thread.running = False
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Agregar producto")
        msg_box.setText(f"¿Deseas agregar '{producto['nombre']}' a la base de datos?")
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg_box.setWindowFlag(Qt.WindowStaysOnTopHint)
        respuesta = msg_box.exec_()

        if respuesta == QMessageBox.Yes:
            precio, ok = QInputDialog.getDouble(
                self, "Precio del producto",
                f"Ingrese precio para '{producto['nombre']}':",
                decimals=2
            )
            if ok:
                db = Database()
                success, msg = db.agregar_producto_con_camara(
                    producto["nombre"],
                    producto["categoria"],
                    producto["marca"],
                    producto["presentacion"],
                    precio
                )
                info_box = QMessageBox(self)
                info_box.setWindowTitle("Resultado")
                info_box.setText(msg)
                info_box.setWindowFlag(Qt.WindowStaysOnTopHint)
                info_box.exec_()
        self.camera_thread.running = True
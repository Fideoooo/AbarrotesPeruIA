from PyQt5 import QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMessageBox, QAbstractItemView
from Backend.database import Database
from Diseno.marcas_ui import Ui_Form


class MarcasWindow(QtWidgets.QWidget):
    def __init__(self, empleado_id):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Configurar selección de la tabla (clic en cualquier celda selecciona la fila)
        self.ui.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tableView.setSelectionMode(QAbstractItemView.SingleSelection)

        # GUARDAMOS EL EMPLEADO PARA USARLO AL RETROCEDER
        self.empleado_id = empleado_id

        # Conectar BD
        self.db = Database()

        # Configurar modelo de tabla
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["ID", "Marca"])
        self.ui.tableView.setModel(self.model)

        # Cargar datos
        self.cargar_datos()

        # Estado inicial botones
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

        # Abajo deshabilitados
        self.ui.pushButton_4.setEnabled(False) # Agregar
        self.ui.pushButton_5.setEnabled(False) # Modificar

        # --- Evitar conexiones duplicadas: desconectar primero si estaban conectadas ---
        try:
            self.ui.pushButton.clicked.disconnect()
        except Exception:
            pass
        try:
            self.ui.pushButton_2.clicked.disconnect()
        except Exception:
            pass
        try:
            self.ui.pushButton_3.clicked.disconnect()
        except Exception:
            pass

        # Conexiones (conexiones limpias, sin duplicados)
        self.ui.pushButton.clicked.connect(self.nueva_marca)
        self.ui.pushButton_2.clicked.connect(self.editar_marca)
        self.ui.pushButton_3.clicked.connect(self.eliminar_marca)

    # ------------------ NUEVO ------------------
    def nueva_marca(self):
        self.limpiar_campos()

        # Arriba deshabilitados
        self.ui.pushButton.setEnabled(False)
        self.ui.pushButton_2.setEnabled(False)
        self.ui.pushButton_3.setEnabled(False)

        # Abajo → solo Agregar habilitado
        self.ui.pushButton_4.setEnabled(True)
        self.ui.pushButton_5.setEnabled(False)

        # Evitar conexiones múltiples al botón Agregar
        try:
            self.ui.pushButton_4.clicked.disconnect()
        except Exception:
            pass

        self.ui.pushButton_4.clicked.connect(self.agregar_marca)

    def agregar_marca(self):
        nombre = self.ui.lineEdit_nombre.text().strip()
        if not nombre:
            QMessageBox.warning(self, "Atención", "Ingrese el nombre de la marca.")
            return

        exito, mensaje = self.db.agregar_marca(nombre)

        if exito:
            QMessageBox.information(self, "Éxito", mensaje)
            self.cargar_datos()
            self.estado_inicial()
        else:
            QMessageBox.warning(self, "Error", mensaje)

    # ------------------ EDITAR ------------------
    def editar_marca(self):
        index = self.ui.tableView.currentIndex()
        if not index.isValid():
            QMessageBox.warning(self, "Atención", "Seleccione una marca para editar.")
            return

        fila = index.row()
        marca_id = self.model.item(fila, 0).text()
        nombre = self.model.item(fila, 1).text()

        self.ui.lineEdit_nombre.setText(nombre)
        self.marca_id_editando = marca_id

        # Arriba deshabilitados
        self.ui.pushButton.setEnabled(False)
        self.ui.pushButton_2.setEnabled(False)
        self.ui.pushButton_3.setEnabled(False)

        # Abajo → solo Modificar habilitado
        self.ui.pushButton_4.setEnabled(False)
        self.ui.pushButton_5.setEnabled(True)

        # Evitar múltiples conexiones al botón Modificar
        try:
            self.ui.pushButton_5.clicked.disconnect()
        except Exception:
            pass

        self.ui.pushButton_5.clicked.connect(self.modificar_marca)

    def modificar_marca(self):
        nombre = self.ui.lineEdit_nombre.text().strip()
        if not nombre:
            QMessageBox.warning(self, "Atención", "Ingrese el nombre de la marca.")
            return

        self.db.actualizar_marca(self.marca_id_editando, nombre)
        self.cargar_datos()
        self.estado_inicial()

    # ------------------ ELIMINAR ------------------
    def eliminar_marca(self):
        # Usamos selectedRows porque la tabla está en SelectRows
        seleccion = self.ui.tableView.selectionModel().selectedRows()
        if not seleccion:
            QMessageBox.warning(self, "Atención", "Seleccione una marca para eliminar.")
            return

        index = seleccion[0]
        # obtener MarcaID directamente desde el índice del modelo de la vista
        marca_id = index.sibling(index.row(), 0).data()

        confirm = QMessageBox.question(
            self,
            "Confirmar",
            "¿Está seguro de eliminar esta marca?",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirm == QMessageBox.Yes:
            exito, mensaje = self.db.eliminar_marca(marca_id)
            if exito:
                # Mostrar mensaje primero (para que no interfiera señales al recargar)
                QMessageBox.information(self, "Éxito", mensaje)

                # Bloquear señales al recargar la tabla (evita efectos colaterales)
                self.ui.tableView.blockSignals(True)
                self.cargar_datos()
                self.ui.tableView.clearSelection()
                self.ui.tableView.blockSignals(False)

                # Regresar al estado inicial (opcional, mantiene consistencia)
                self.estado_inicial()
            else:
                QMessageBox.warning(self, "Error", mensaje)

    # ------------------ UTILIDADES ------------------
    def cargar_datos(self):
        self.model.removeRows(0, self.model.rowCount())
        marcas = self.db.obtener_marcas()  # [(1, "Nike"), (2, "Adidas")]

        for marca in marcas:
            row = [
                QStandardItem(str(marca[0])),
                QStandardItem(str(marca[1]))
            ]
            self.model.appendRow(row)

    def limpiar_campos(self):
        self.ui.lineEdit_nombre.clear()

    def retroceder(self):
        from Backend.menu_inicio_backend import MenuInicioWindow
        self.menu_inicio = MenuInicioWindow(self.empleado_id)
        self.menu_inicio.show()
        self.close()
from PyQt5 import QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMessageBox, QAbstractItemView
from Backend.database import Database
from Diseno.categoria_ui import Ui_Form  # Asegúrate de que tu frontend se llame así


class CategoriasWindow(QtWidgets.QWidget):
    def __init__(self, empleado_id):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Guardamos el empleado_id
        self.empleado_id = empleado_id

        # Configurar selección de la tabla (clic en cualquier celda selecciona la fila)
        self.ui.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tableView.setSelectionMode(QAbstractItemView.SingleSelection)

        # Conectar BD
        self.db = Database()

        # Configurar modelo de tabla
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["ID", "Categoría"])
        self.ui.tableView.setModel(self.model)

        # Cargar datos
        self.cargar_datos()

        # Estado inicial botones
        self.estado_inicial()

        # ---------------- BOTONES RETROCEDER Y CERRAR ----------------
        if hasattr(self.ui, "btn_back"):
            self.ui.btn_back.clicked.connect(self.retroceder)
        if hasattr(self.ui, "btn_close"):
            self.ui.btn_close.clicked.connect(self.close)
        # -------------------------------------------------------------

    def estado_inicial(self):
        """Estado inicial de la interfaz y conexiones (evitar duplicados)"""
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

        # Conexiones limpias
        self.ui.pushButton.clicked.connect(self.nueva_categoria)
        self.ui.pushButton_2.clicked.connect(self.editar_categoria)
        self.ui.pushButton_3.clicked.connect(self.eliminar_categoria)

    # ------------------ NUEVO ------------------
    def nueva_categoria(self):
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

        self.ui.pushButton_4.clicked.connect(self.agregar_categoria)

    def agregar_categoria(self):
        nombre = self.ui.lineEdit.text().strip()
        if not nombre:
            QMessageBox.warning(self, "Atención", "Ingrese el nombre de la categoría.")
            return

        exito, mensaje = self.db.agregar_categoria(nombre)

        if exito:
            QMessageBox.information(self, "Éxito", mensaje)
            self.cargar_datos()
            self.estado_inicial()
        else:
            QMessageBox.warning(self, "Error", mensaje)

    # ------------------ EDITAR ------------------
    def editar_categoria(self):
        index = self.ui.tableView.currentIndex()
        if not index.isValid():
            QMessageBox.warning(self, "Atención", "Seleccione una categoría para editar.")
            return

        fila = index.row()
        categoria_id = self.model.item(fila, 0).text()
        nombre = self.model.item(fila, 1).text()

        self.ui.lineEdit.setText(nombre)
        self.categoria_id_editando = categoria_id

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

        self.ui.pushButton_5.clicked.connect(self.modificar_categoria)

    def modificar_categoria(self):
        nombre = self.ui.lineEdit.text().strip()
        if not nombre:
            QMessageBox.warning(self, "Atención", "Ingrese el nombre de la categoría.")
            return

        exito, mensaje = self.db.actualizar_categoria(self.categoria_id_editando, nombre)
        if exito:
            QMessageBox.information(self, "Éxito", mensaje)
            self.cargar_datos()
            self.estado_inicial()
        else:
            QMessageBox.warning(self, "Error", mensaje)

    # ------------------ ELIMINAR ------------------
    def eliminar_categoria(self):
        # Usamos selectedRows porque la tabla está en SelectRows
        seleccion = self.ui.tableView.selectionModel().selectedRows()
        if not seleccion:
            QMessageBox.warning(self, "Atención", "Seleccione una categoría para eliminar.")
            return

        index = seleccion[0]
        # obtener CategoriaID y nombre desde el índice de la vista
        try:
            categoria_id = index.sibling(index.row(), 0).data()
            nombre = index.sibling(index.row(), 1).data()
        except Exception:
            QMessageBox.warning(self, "Atención", "No se pudo leer la fila seleccionada.")
            return

        confirm = QMessageBox.question(
            self,
            "Confirmar",
            f"¿Está seguro de eliminar la categoría '{nombre}' (ID {categoria_id})?",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirm == QMessageBox.Yes:
            exito, mensaje = self.db.eliminar_categoria(categoria_id)
            if exito:
                # Mostrar info antes de recargar para evitar efectos después de recargar
                QMessageBox.information(self, "Éxito", mensaje)

                # Bloquear señales al recargar (evita warnings fantasma)
                self.ui.tableView.blockSignals(True)
                self.cargar_datos()
                self.ui.tableView.clearSelection()
                self.ui.tableView.blockSignals(False)

                # Reset visual / conexiones
                self.estado_inicial()
            else:
                QMessageBox.warning(self, "Error", mensaje)

    # ------------------ UTILIDADES ------------------
    def cargar_datos(self):
        self.model.removeRows(0, self.model.rowCount())
        categorias = self.db.obtener_categorias()  # [(1, "Bebidas"), (2, "Snacks")]

        for categoria in categorias:
            row = [
                QStandardItem(str(categoria[0])),
                QStandardItem(str(categoria[1]))
            ]
            self.model.appendRow(row)

    def limpiar_campos(self):
        self.ui.lineEdit.clear()

    def retroceder(self):
        from Backend.menu_inicio_backend import MenuInicioWindow
        self.menu_inicio = MenuInicioWindow(self.empleado_id)
        self.menu_inicio.show()
        self.close()
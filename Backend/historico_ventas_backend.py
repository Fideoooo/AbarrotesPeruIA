# historico_ventas_backend.py
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QMessageBox
from Diseno.historico_ventas_ui import Ui_Form
from Backend.database import Database

class HistoricoVentasWindow(QtWidgets.QWidget):
    def __init__(self, parent=None, empleado_id=None):
        super().__init__(parent, QtCore.Qt.Window)  # 👈 le decimos que sea ventana propia
        self.parent_window = parent
        self.empleado_id = empleado_id
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.db = Database()

        # --- IMPORTANTE ---
        # Forzamos que la ventana se muestre
        self.setWindowModality(QtCore.Qt.NonModal)  # no bloquea al padre
        self.show()

        # Botón retroceder
        self.ui.btn_back.clicked.connect(self.retroceder)

        # Cargar empleados al abrir
        self.cargar_empleados()

        # Modelo de la tabla
        self.model = QStandardItemModel()
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.ui.tableView.setEditTriggers(QtWidgets.QTableView.NoEditTriggers)

        # Configurar fechas por defecto
        hoy = QtCore.QDate.currentDate()
        self.ui.dateEdit.setDate(hoy.addDays(-30))
        self.ui.dateEdit_2.setDate(hoy)

        # Conectar botones
        self.ui.pushButton.clicked.connect(self.on_filtrar)        # Buscar
        self.ui.pushButton_2.clicked.connect(self.on_ver_detalle)  # Ver Detalle
        self.ui.btn_back.clicked.connect(self.retroceder)          # Retroceder (volver al padre)
        self.ui.btn_close.clicked.connect(self.on_close)           # Cerrar (si hay padre lo muestra)

        # Llenar empleados en combo
        self.cargar_empleados()

        # Cargar datos iniciales
        self.on_filtrar()

    def cargar_empleados(self):
        """Carga todos los empleados en el comboBox (robusto y con debug)."""
        # limpiar combo y añadir "Todos"
        self.ui.comboBox.clear()
        self.ui.comboBox.addItem("Todos", None)

        # obtener empleados desde DB
        empleados = self.db.obtener_empleados()
        print("DEBUG: obtener_empleados() ->", empleados)  # <-- mira esto en consola

        added = 0
        if not empleados:
            print("DEBUG: No se recibieron empleados desde la BD.")
        for emp in empleados:
            try:
                emp_id = None
                nombre = None

                # Si es dict
                if isinstance(emp, dict):
                    emp_id = emp.get("EmpleadoID") or emp.get("empleadoid") or emp.get("id")
                    nombre = emp.get("Nombre") or emp.get("nombre")
                else:
                    # Intentar desempaquetar (tupla o lista)
                    try:
                        emp_id, nombre = emp[0], emp[1]
                    except Exception:
                        # Intentar atributos (pyodbc.Row permite acceso por nombre como atributo)
                        emp_id = getattr(emp, "EmpleadoID", None) or getattr(emp, "EmpleadoId", None)
                        nombre = getattr(emp, "Nombre", None) or getattr(emp, "nombre", None)

                # Si no pudimos extraer nada, saltar y avisar
                if emp_id is None or nombre is None:
                    print(f"DEBUG: No se pudo extraer id/nombre de fila: {emp}")
                    continue

                # Añadir al combo (userData = emp_id)
                self.ui.comboBox.addItem(str(nombre), int(emp_id))
                added += 1
            except Exception as e:
                print("DEBUG: Error al procesar empleado:", e)
                continue

        print(f"DEBUG: Empleados añadidos al combo: {added}")

        # Si existe self.empleado_id (empleado logueado), seleccionarlo por defecto
        if getattr(self, "empleado_id", None) is not None:
            index = self.ui.comboBox.findData(self.empleado_id)
            if index != -1:
                self.ui.comboBox.setCurrentIndex(index)
            else:
                print(f"DEBUG: empleado_id {self.empleado_id} no encontrado en el combo.")

    def on_filtrar(self):
        """Filtra las ventas según fecha y empleado seleccionado"""
        fecha_ini = self.ui.dateEdit.date().toString("yyyy-MM-dd")
        fecha_fin = self.ui.dateEdit_2.date().toString("yyyy-MM-dd")
        empleado_id = self.ui.comboBox.currentData()

        ventas = self.db.obtener_ventas(fecha_ini, fecha_fin, empleado_id)

        self.model.clear()
        self.model.setHorizontalHeaderLabels(["ID", "Fecha", "Empleado", "Total"])

        for venta in ventas:
            row = [
                QStandardItem(str(venta[0])),  # VENTA ID
                QStandardItem(str(venta[1])),  # FECHA VENTA
                QStandardItem(str(venta[2])),  # EMPLEADO
                QStandardItem(f"{venta[3]:.2f}"),  # TOTAL
            ]
            self.model.appendRow(row)

    def retroceder(self):
        """Vuelve a la ventana padre (si existe), la asegura visible y trae al frente, luego cierra este formulario."""
        try:
            print("DEBUG: retroceder() llamado. parent_window:", self.parent_window)
            if getattr(self, "parent_window", None) is not None:
                pw = self.parent_window
                # Debug estado antes
                try:
                    print("DEBUG: parent isVisible before =", pw.isVisible(), "isEnabled =", pw.isEnabled())
                except Exception:
                    print("DEBUG: no se pudo consultar isVisible/isEnabled del parent")

                # Aseguramos que esté visible y en primer plano
                try:
                    pw.setVisible(True)
                    pw.showNormal()        # en caso esté minimizada
                    pw.raise_()            # trae al frente
                    pw.activateWindow()    # intenta darle foco
                except Exception as e:
                    print("DEBUG: Error al mostrar/activar parent:", e)

                # Si parece seguir invisible, forzamos una posición conocida (útil si quedó fuera de pantalla)
                try:
                    if not pw.isVisible():
                        pw.move(100, 100)
                        pw.show()
                except Exception:
                    pass

            # finalmente cerramos esta ventana
            self.close()

        except Exception as e:
            print("DEBUG: Exception en retroceder():", e)
            # Aun en error, cerramos para no dejar la app colgada
            try:
                self.close()
            except Exception:
                pass

    def on_close(self):
        """Cerrar: mostrar padre antes de cerrar para que la app no quede sin ventanas."""
        try:
            print("DEBUG: on_close() llamado. parent_window:", self.parent_window)
            if getattr(self, "parent_window", None) is not None:
                pw = self.parent_window
                try:
                    pw.setVisible(True)
                    pw.showNormal()
                    pw.raise_()
                    pw.activateWindow()
                except Exception as e:
                    print("DEBUG: Error al mostrar parent en on_close:", e)
        finally:
            self.close()

    def on_ver_detalle(self):
        """Muestra el detalle de la venta seleccionada"""
        selected = self.ui.tableView.currentIndex()
        if not selected.isValid():
            QMessageBox.warning(self, "Aviso", "Selecciona una venta primero")
            return

        venta_id = int(self.model.item(selected.row(), 0).text())
        detalles = self.db.obtener_detalle_venta(venta_id)

        # Mostrar detalle en un QMessageBox (puedes migrarlo a un QDialog más bonito)
        detalle_texto = "\n".join(
            [f"{d[0]} - {d[1]} x {d[2]:.2f} = {d[3]:.2f}" for d in detalles]
        )
        QMessageBox.information(self, "Detalle de Venta", detalle_texto or "Sin detalles")
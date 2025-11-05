from PyQt5 import QtCore, QtGui, QtWidgets
import sys, res

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1032, 639)
        Form.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(20, 20, 991, 601))
        self.frame.setStyleSheet("QPushButton {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color: rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"    color: rgba(255, 255, 255, 210);\n"
"}\n"
"QPushButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(105, 118, 132, 200);\n"
"}\n"
"\n"
"QComboBox {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color: rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QComboBox:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"    color: rgba(255, 255, 255, 210);\n"
"}\n"
"QComboBox:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(105, 118, 132, 200);\n"
"}\n"
"\n"
"QTableView {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color: rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QTableView:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"    color: rgba(255, 255, 255, 210);\n"
"}\n"
"QTableView:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(105, 118, 132, 200);\n"
"}\n"
"\n"
"QDateEdit {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color: rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QDateEdit:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"    color: rgba(255, 255, 255, 210);\n"
"}\n"
"QDateEdit:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(105, 118, 132, 200);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 20, 971, 571))
        self.label.setStyleSheet("border-image: url(:/images/background.png);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0.715909, stop:0 rgba(0, 0, 0, 9), stop:0.375 rgba(0, 0, 0, 50), stop: 0.835227 rgba(0, 0, 0, 75));\n"
"border-radius:20px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 951, 551))
        self.label_2.setStyleSheet("background-color: rgba(0, 0, 0, 100);\n"
"border-radius: 15px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.tableView = QtWidgets.QTableView(self.frame)
        self.tableView.setGeometry(QtCore.QRect(30, 180, 501, 391))
        self.tableView.setObjectName("tableView")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(50, 70, 101, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 70, 101, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(430, 70, 101, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(830, 240, 101, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(830, 340, 101, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
#AGREGAR CON CAM       
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(580, 70, 161, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
#-----
        self.lineEdit_nombre = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_nombre.setGeometry(QtCore.QRect(550, 300, 151, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_nombre.setFont(font)
        self.lineEdit_nombre.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom: 2px solid rgba(105, 118, 132, 255);\n"
"color:rgba(255, 255, 255, 230);\n"
"padding-bottom:7px;")
        self.lineEdit_nombre.setObjectName("lineEdit")
        self.comboBox_categoria = QtWidgets.QComboBox(self.frame)
        self.comboBox_categoria.setGeometry(QtCore.QRect(550, 210, 151, 22))
        self.comboBox_categoria.setObjectName("comboBox")
        self.comboBox_marca = QtWidgets.QComboBox(self.frame)
        self.comboBox_marca.setGeometry(QtCore.QRect(550, 260, 151, 22))
        self.comboBox_marca.setObjectName("comboBox_2")
        self.lineEdit_presentacion = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_presentacion.setGeometry(QtCore.QRect(550, 360, 151, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_presentacion.setFont(font)
        self.lineEdit_presentacion.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom: 2px solid rgba(105, 118, 132, 255);\n"
"color:rgba(255, 255, 255, 230);\n"
"padding-bottom:7px;")
        self.lineEdit_presentacion.setObjectName("lineEdit_2")
        self.dateEdit = QtWidgets.QDateEdit(self.frame)
        self.dateEdit.setGeometry(QtCore.QRect(550, 480, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.lineEdit_codigobarras = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_codigobarras.setGeometry(QtCore.QRect(550, 420, 151, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_codigobarras.setFont(font)
        self.lineEdit_codigobarras.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom: 2px solid rgba(105, 118, 132, 255);\n"
"color:rgba(255, 255, 255, 230);\n"
"padding-bottom:7px;")
        self.lineEdit_codigobarras.setObjectName("lineEdit_3")

        # ----------------- BOTONES RETROCEDER Y CERRAR -----------------
        self.btn_back = QtWidgets.QPushButton(self.frame)
        self.btn_back.setGeometry(QtCore.QRect(880, 30, 40, 40))
        self.btn_back.setText("⮌")  # También puedes usar "←"
        self.btn_back.setStyleSheet("""
            QPushButton {
                background-color: rgba(0,0,0,80);
                color: white;
                border-radius: 20px;
                font: bold 18px;
            }
            QPushButton:hover {
                background-color: rgba(234, 221, 186, 120);
            }
        """)
        self.btn_back.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(
            blurRadius=15, xOffset=2, yOffset=2, color=QtGui.QColor(0,0,0,150)
        ))

        self.btn_close = QtWidgets.QPushButton(self.frame)
        self.btn_close.setGeometry(QtCore.QRect(930, 30, 40, 40))
        self.btn_close.setText("✕")
        self.btn_close.setStyleSheet("""
            QPushButton {
                background-color: rgba(0,0,0,80);
                color: white;
                border-radius: 20px;
                font: bold 18px;
            }
            QPushButton:hover {
                background-color: rgba(255,0,0,150);
            }
        """)
        self.btn_close.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(
            blurRadius=15, xOffset=2, yOffset=2, color=QtGui.QColor(0,0,0,150)
        ))
        # ------------------------------------------------------


        # ----------------- NUEVO CAMPO PRECIO -----------------
        self.lineEdit_precio = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_precio.setGeometry(QtCore.QRect(550, 540, 151, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_precio.setFont(font)
        self.lineEdit_precio.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom: 2px solid rgba(105, 118, 132, 255);\n"
"color:rgba(255, 255, 255, 230);\n"
"padding-bottom:7px;")
        self.lineEdit_precio.setObjectName("lineEdit_precio")

        self.label_precio = QtWidgets.QLabel(self.frame)
        self.label_precio.setGeometry(QtCore.QRect(720, 540, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_precio.setFont(font)
        self.label_precio.setStyleSheet("color:rgba(255, 255, 255, 140);")
        self.label_precio.setObjectName("label_precio")
        self.label_precio.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(
            blurRadius=25, xOffset=0, yOffset=0,
            color=QtGui.QColor(234, 221, 186, 100)))
        # ------------------------------------------------------


        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(740, 50, 231, 161))
        self.label_3.setStyleSheet("border-image: url(:/images/Grupo_smar_logo.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(720, 210, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(255, 255, 255, 140);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(720, 260, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:rgba(255, 255, 255, 140);")
        self.label_5.setObjectName("label_5")
#PARA DARLE BRILLI BRILLI
        self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0, color=QtGui.QColor(234, 221, 186, 100)))
        self.label_4.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0, color=QtGui.QColor(234, 221, 186, 100)))
        self.label_5.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0, color=QtGui.QColor(234, 221, 186, 100)))
        self.pushButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3, color=QtGui.QColor(105, 118, 132, 100)))
        self.pushButton_2.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3, color=QtGui.QColor(105, 118, 132, 100)))
        self.pushButton_3.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3, color=QtGui.QColor(105, 118, 132, 100)))
        self.pushButton_4.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3, color=QtGui.QColor(105, 118, 132, 100)))
        self.pushButton_5.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3, color=QtGui.QColor(105, 118, 132, 100)))
        self.pushButton_6.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3, color=QtGui.QColor(105, 118, 132, 100)))
        self.tableView.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3, color=QtGui.QColor(105, 118, 132, 100)))
     

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Nuevo"))
        self.pushButton_2.setText(_translate("Form", "Editar"))
        self.pushButton_3.setText(_translate("Form", "Eliminar"))
        self.pushButton_4.setText(_translate("Form", "Agregar"))
        self.pushButton_5.setText(_translate("Form", "Modificar"))
        self.pushButton_6.setText(_translate("Form", "Agregar Producto (CAM)"))
        self.lineEdit_nombre.setPlaceholderText(_translate("Form", "Nombre"))
        self.lineEdit_presentacion.setPlaceholderText(_translate("Form", "Presentacion"))
        self.lineEdit_codigobarras.setPlaceholderText(_translate("Form", "Codigo Barras"))
        # ----------------- NUEVO CAMPO PRECIO -----------------

        self.lineEdit_precio.setPlaceholderText(_translate("Form", "Precio"))
        self.label_precio.setText(_translate("Form", "Precio"))
        # ----------------- NUEVO CAMPO PRECIO -----------------
        
        self.label_4.setText(_translate("Form", "Categoria"))
        self.label_5.setText(_translate("Form", "Marca"))

if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = Ui_Form()
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec_())
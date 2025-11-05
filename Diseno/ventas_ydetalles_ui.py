from PyQt5 import QtCore, QtGui, QtWidgets
import sys, res

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(997, 740)
        Form.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 10, 971, 711))
        self.frame.setStyleSheet(
    "QPushButton {\n"
    "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, "
    "stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
    "    color: rgba(255, 255, 255, 210);\n"
    "    border-radius: 5px;\n"
    "}\n"
    "QPushButton:hover {\n"
    "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, "
    "stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
    "    color: rgba(255, 255, 255, 210);\n"
    "}\n"
    "QPushButton:pressed {\n"
    "    padding-left: 5px;\n"
    "    padding-top: 5px;\n"
    "    background-color: rgba(105, 118, 132, 200);\n"
    "}\n"
    "\n"
    "QComboBox {\n"
    "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, "
    "stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
    "    color: rgba(255, 255, 255, 210);\n"
    "    border-radius: 5px;\n"
    "}\n"
    "QComboBox:hover {\n"
    "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, "
    "stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
    "    color: rgba(255, 255, 255, 210);\n"
    "}\n"
    "QComboBox:pressed {\n"
    "    padding-left: 5px;\n"
    "    padding-top: 5px;\n"
    "    background-color: rgba(105, 118, 132, 200);\n"
    "}\n"
    "\n"
    "QTableWidget {\n"
    "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, "
    "stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
    "    color: rgba(255, 255, 255, 210);\n"
    "    border-radius: 5px;\n"
    "}\n"
    "QTableWidget:hover {\n"
    "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, "
    "stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
    "    color: rgba(255, 255, 255, 210);\n"
    "}\n"
    "QTableWidget:pressed {\n"
    "    padding-left: 5px;\n"
    "    padding-top: 5px;\n"
    "    background-color: rgba(105, 118, 132, 200);\n"
    "}\n"
    "\n"
    "QSpinBox {\n"
    "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, "
    "stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
    "    color: rgba(255, 255, 255, 210);\n"
    "    border-radius: 5px;\n"
    "}\n"
    "QSpinBox:hover {\n"
    "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, "
    "stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
    "    color: rgba(255, 255, 255, 210);\n"
    "}\n"
    "QSpinBox:pressed {\n"
    "    padding-left: 5px;\n"
    "    padding-top: 5px;\n"
    "    background-color: rgba(105, 118, 132, 200);\n"
    "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 30, 941, 661))
        self.label.setStyleSheet("border-image: url(:/images/background.png);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0.715909, stop:0 rgba(0, 0, 0, 9), stop:0.375 rgba(0, 0, 0, 50), stop: 0.835227 rgba(0, 0, 0, 75));\n"
"border-radius:20px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 921, 601))
        self.label_2.setStyleSheet("background-color: rgba(0, 0, 0, 100);\n"
"border-radius: 15px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(40, 110, 281, 571))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(2)
        self.frame_2.setMidLineWidth(1)
        self.frame_2.setObjectName("frame_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(0, 20, 281, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setStyleSheet("color: white;\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(10, 90, 201, 20))
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: white;\n"
"")
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(self.frame_2)
        self.comboBox.setGeometry(QtCore.QRect(10, 120, 261, 22))
        self.comboBox.setObjectName("comboBox")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(10, 160, 201, 20))
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: white;\n"
"")
        self.label_5.setObjectName("label_5")
        self.spinBox = QtWidgets.QSpinBox(self.frame_2)
        self.spinBox.setGeometry(QtCore.QRect(10, 190, 261, 22))
        self.spinBox.setObjectName("spinBox")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(30, 240, 221, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 280, 221, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(30, 380, 221, 191))
        self.label_9.setStyleSheet("border-image: url(:/images/Grupo_smar_logo.png);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(330, 110, 601, 491))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setLineWidth(2)
        self.frame_3.setMidLineWidth(1)
        self.frame_3.setObjectName("frame_3")
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setGeometry(QtCore.QRect(10, 20, 581, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setStyleSheet("color: white;\n"
"")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(20, 420, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: white;\n"
"")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setGeometry(QtCore.QRect(460, 420, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: white;\n"
"")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_3)
        self.tableWidget.setGeometry(QtCore.QRect(10, 60, 581, 361))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 620, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(560, 620, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(760, 620, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(160, 40, 581, 41))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: white;\n"
"")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
#BOTONES CERRAR Y RETROCEDER
        self.backButton = QtWidgets.QPushButton(self.frame)
        self.backButton.setGeometry(QtCore.QRect(860, 20, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.backButton.setFont(font)
        self.backButton.setText("←")
        self.backButton.setObjectName("backButton")
        self.backButton.setStyleSheet(
            "QPushButton {\n"
            "    background-color: rgba(0,0,0,120);\n"
            "    color: white;\n"
            "    border-radius: 10px;\n"
            "}\n"
            "QPushButton:hover {\n"
            "    background-color: rgba(255,255,255,40);\n"
            "}\n"
            "QPushButton:pressed {\n"
            "    background-color: rgba(200,200,200,80);\n"
            "}"
        )
        self.backButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(
            blurRadius=20, xOffset=2, yOffset=2, color=QtGui.QColor(0, 0, 0, 150)
        ))

        # Botón Cerrar (✕) arriba a la derecha
        self.closeButton = QtWidgets.QPushButton(self.frame)
        self.closeButton.setGeometry(QtCore.QRect(910, 20, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.closeButton.setFont(font)
        self.closeButton.setText("✕")
        self.closeButton.setObjectName("closeButton")
        self.closeButton.setStyleSheet(
            "QPushButton {\n"
            "    background-color: rgba(255,0,0,180);\n"
            "    color: white;\n"
            "    border-radius: 10px;\n"
            "}\n"
            "QPushButton:hover {\n"
            "    background-color: rgba(255,0,0,230);\n"
            "}\n"
            "QPushButton:pressed {\n"
            "    background-color: rgba(200,0,0,200);\n"
            "}"
        )
        self.closeButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(
            blurRadius=20, xOffset=2, yOffset=2, color=QtGui.QColor(0, 0, 0, 150)
        ))


#EL BRILLI BRILLI
        self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0, color=QtGui.QColor(234, 221, 186, 100)))
        self.label_3.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0, color=QtGui.QColor(234, 221, 186, 100)))
        self.label_4.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0, color=QtGui.QColor(234, 221, 186, 100)))
        self.label_5.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0, color=QtGui.QColor(234, 221, 186, 100)))
        self.label_6.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0, color=QtGui.QColor(234, 221, 186, 100)))
        self.label_7.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0, color=QtGui.QColor(234, 221, 186, 100)))
        self.label_8.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0, color=QtGui.QColor(234, 221, 186, 100)))
        self.label_10.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0, color=QtGui.QColor(234, 221, 186, 100)))
        self.pushButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3, color=QtGui.QColor(105, 118, 132, 100)))
        self.pushButton_2.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3, color=QtGui.QColor(105, 118, 132, 100)))
        self.pushButton_3.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3, color=QtGui.QColor(105, 118, 132, 100)))
        self.pushButton_4.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3, color=QtGui.QColor(105, 118, 132, 100)))
        self.pushButton_5.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3, color=QtGui.QColor(105, 118, 132, 100)))
        self.tableWidget.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3, color=QtGui.QColor(105, 118, 132, 100)))
        self.spinBox.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3, color=QtGui.QColor(105, 118, 132, 100)))


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Nuevo Producto"))
        self.label_4.setText(_translate("Form", "Seleccionar Producto"))
        self.label_5.setText(_translate("Form", "Cantidad"))
        self.pushButton.setText(_translate("Form", "Agregar Producto"))
        self.pushButton_5.setText(_translate("Form", "Agregar Producto con CAM"))
        self.label_6.setText(_translate("Form", "Detalles de Venta"))
        self.label_7.setText(_translate("Form", "TOTAL:"))
        self.label_8.setText(_translate("Form", "0"))
        self.pushButton_2.setText(_translate("Form", "Finalizar Venta"))
        self.pushButton_3.setText(_translate("Form", "Cancelar"))
        self.pushButton_4.setText(_translate("Form", "Ver Ventas"))
        self.label_10.setText(_translate("Form", "VENTAS"))

if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = Ui_Form()
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec_())
        
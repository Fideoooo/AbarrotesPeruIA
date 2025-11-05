from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1090, 825)
        Form.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(20, 20, 1041, 781))
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
"    background-color: qlineargradient(\n"
"        spread:pad, \n"
"        x1:0, y1:0.505682, \n"
"        x2:1, y2:0.477, \n"
"        stop:0 rgba(20, 47, 78, 219), \n"
"        stop:1 rgba(85, 98, 112, 226)\n"
"    );\n"
"    color: rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"    padding: 2px 5px;\n"
"}\n"
"\n"
"QDateEdit:hover {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, \n"
"        x1:0, y1:0.505682, \n"
"        x2:1, y2:0.477, \n"
"        stop:0 rgba(40, 67, 98, 219), \n"
"        stop:1 rgba(105, 118, 132, 226)\n"
"    );\n"
"    color: rgba(255, 255, 255, 210);\n"
"}\n"
"\n"
"QDateEdit::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    background-color: rgba(105, 118, 132, 200);\n"
"    border-left: 1px solid rgba(255, 255, 255, 80);\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"QDateEdit::down-arrow {\n"
"    image: url(:/qt-project.org/styles/commonstyle/images/arrowdown-16.png);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"QComboBox {\n"
"    background-color: qlineargradient(\n"
"        spread:pad,\n"
"        x1:0, y1:0.505682,\n"
"        x2:1, y2:0.477,\n"
"        stop:0 rgba(20, 47, 78, 219),\n"
"        stop:1 rgba(85, 98, 112, 226)\n"
"    );\n"
"    color: rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"    padding: 2px 5px;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: qlineargradient(\n"
"        spread:pad,\n"
"        x1:0, y1:0.505682,\n"
"        x2:1, y2:0.477,\n"
"        stop:0 rgba(40, 67, 98, 219),\n"
"        stop:1 rgba(105, 118, 132, 226)\n"
"    );\n"
"    color: rgba(255, 255, 255, 210);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgba(40, 67, 98, 230);\n"
"    color: white;\n"
"    selection-background-color: rgba(105, 118, 132, 200);\n"
"    border-radius: 3px;\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 40, 991, 721))
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0.715909, stop:0 rgba(0, 0, 0, 9), stop:0.375 rgba(0, 0, 0, 50), stop: 0.835227 rgba(0, 0, 0, 75));\n"
"border-image: url(:/images/background.png);\n"
"border-radius:20px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 971, 681))
        self.label_2.setStyleSheet("background-color: rgba(0, 0, 0, 100);\n"
"border-radius: 15px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(250, 50, 481, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgba(255, 255, 255, 255);\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

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

        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(40, 120, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgba(255, 255, 255, 255);\n"
"\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(40, 170, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgba(255, 255, 255, 255);\n"
"\n"
"")
        self.label_5.setObjectName("label_5")
        self.dateEdit = QtWidgets.QDateEdit(self.frame)
        self.dateEdit.setGeometry(QtCore.QRect(120, 190, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(40, 220, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgba(255, 255, 255, 255);\n"
"\n"
"")
        self.label_6.setObjectName("label_6")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.frame)
        self.dateEdit_2.setGeometry(QtCore.QRect(120, 240, 110, 22))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(450, 190, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgba(255, 255, 255, 255);\n"
"")
        self.label_7.setObjectName("label_7")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(570, 190, 131, 22))
        self.comboBox.setObjectName("comboBox")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(440, 120, 431, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgba(255, 255, 255, 255);\n"
"\n"
"")
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(560, 230, 171, 41))
        self.pushButton.setObjectName("pushButton")
        self.tableView = QtWidgets.QTableView(self.frame)
        self.tableView.setGeometry(QtCore.QRect(50, 280, 921, 381))
        self.tableView.setObjectName("tableView")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(750, 680, 191, 61))
        self.pushButton_2.setObjectName("pushButton_2")

        ##BRILLI BRILLI
        self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0, color=QtGui.QColor(234, 221, 186, 100)))
        self.label_3.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0, color=QtGui.QColor(234, 221, 186, 100)))
        self.label_4.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0, color=QtGui.QColor(234, 221, 186, 100)))
        self.label_5.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0, color=QtGui.QColor(234, 221, 186, 100)))
        self.label_6.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0, color=QtGui.QColor(234, 221, 186, 100)))
        self.label_7.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0, color=QtGui.QColor(234, 221, 186, 100)))
        self.label_8.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0, color=QtGui.QColor(234, 221, 186, 100)))
        self.pushButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3, color=QtGui.QColor(105, 118, 132, 100)))
        self.pushButton_2.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3, color=QtGui.QColor(105, 118, 132, 100)))
        self.tableView.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3, color=QtGui.QColor(105, 118, 132, 100)))
        self.comboBox.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3, color=QtGui.QColor(105, 118, 132, 100)))
        self.dateEdit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3, color=QtGui.QColor(105, 118, 132, 100)))
        self.dateEdit_2.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3, color=QtGui.QColor(105, 118, 132, 100)))




        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Historico de Ventas"))
        self.label_4.setText(_translate("Form", "FILTRAR POR FECHA:"))
        self.label_5.setText(_translate("Form", "INICIO"))
        self.label_6.setText(_translate("Form", "FIN"))
        self.label_7.setText(_translate("Form", "Empleados:"))
        self.label_8.setText(_translate("Form", "FILTRAR POR EMPLEADO:"))
        self.pushButton.setText(_translate("Form", "Filtrar"))
        self.pushButton_2.setText(_translate("Form", "Ver Detalles de Venta"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

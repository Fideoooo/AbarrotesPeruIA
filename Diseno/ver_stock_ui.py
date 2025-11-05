from PyQt5 import QtCore, QtGui, QtWidgets
import sys, res

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(561, 532)
        Form.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(20, 10, 521, 501))
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
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 20, 501, 471))
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0.715909, stop:0 rgba(0, 0, 0, 9), stop:0.375 rgba(0, 0, 0, 50), stop: 0.835227 rgba(0, 0, 0, 75));\n"
"border-image: url(:/images/background.png);\n"
"border-radius:20px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 441, 341))
        self.label_2.setStyleSheet("background-color: rgba(0, 0, 0, 100);\n"
"border-radius: 15px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(40, 50, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgba(255, 255, 255, 255);\n"
"")
        self.label_3.setObjectName("label_3")


        # ----------------- BOTONES RETROCEDER Y CERRAR -----------------
        # Posicionados dentro del frame (arriba a la derecha)
        self.btn_cerrar = QtWidgets.QPushButton(self.frame)
        self.btn_cerrar.setGeometry(QtCore.QRect(470, 30, 30, 30))
        self.btn_cerrar.setText("✕")
        self.btn_cerrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cerrar.setStyleSheet("""
        QPushButton {
                background-color: rgba(255, 0, 0, 180);
                color: white;
                border: none;
                border-radius: 15px; /* Mitad del tamaño para hacerlo circular */
                font: bold 14px;
        }
        QPushButton:hover {
                background-color: rgba(255, 0, 0, 220);
        }
        """)
        self.btn_cerrar.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(
        blurRadius=15, xOffset=1, yOffset=1, color=QtGui.QColor(0,0,0,180)
        ))

        self.btn_retroceder = QtWidgets.QPushButton(self.frame)
        self.btn_retroceder.setGeometry(QtCore.QRect(430, 30, 30, 30))
        self.btn_retroceder.setText("⮌")  # ← o usa un icono si prefieres
        self.btn_retroceder.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_retroceder.setStyleSheet("""
        QPushButton {
                background-color: rgba(0, 0, 0, 100);
                color: white;
                border: none;
                border-radius: 15px;
                font: bold 14px;
        }
        QPushButton:hover {
                background-color: rgba(234, 221, 186, 180);
        }
        """)
        self.btn_retroceder.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(
        blurRadius=15, xOffset=1, yOffset=1, color=QtGui.QColor(0,0,0,180)
        ))
# ------------------------------------------------------
        self.tableView = QtWidgets.QTableView(self.frame)
        self.tableView.setGeometry(QtCore.QRect(50, 160, 421, 261))
        self.tableView.setObjectName("tableView")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(70, 100, 391, 41))
        self.widget.setObjectName("widget")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(50, 0, 341, 41))
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 10px;\n"
"    padding-left: 10px;\n"
"    background-color: rgba(255,255,255,0.1);\n"
"    color: white;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 1px solid #3daee9;\n"
"    background-color: rgba(255,255,255,0.2);\n"
"}\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.toolButton = QtWidgets.QToolButton(self.widget)
        self.toolButton.setGeometry(QtCore.QRect(0, 0, 41, 41))
        self.toolButton.setStyleSheet("QToolButton {\n"
"    border: none;\n"
"    background: transparent;\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icono lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setObjectName("toolButton")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(350, 437, 121, 41))
        self.pushButton.setObjectName("pushButton")

#PARA DARLE BRILLI BRILLI
        self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0, color=QtGui.QColor(234, 221, 186, 100)))
        self.label_3.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0, color=QtGui.QColor(234, 221, 186, 100)))
        self.pushButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3, color=QtGui.QColor(105, 118, 132, 100)))
        self.lineEdit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3, color=QtGui.QColor(105, 118, 132, 100)))


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Ver Stock"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Ingresa el nombre del producto"))
        self.toolButton.setText(_translate("Form", "..."))
        self.pushButton.setText(_translate("Form", "Agregar"))


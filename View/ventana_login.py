import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic, QtCore, QtWidgets
from View import Main_window
from server.conexion_sqlserver import conecciones
from controladores.Register import RegistrarInventario


class Main_login(QMainWindow):
    def __init__(self) -> None:
        super(Main_login, self).__init__()
        uic.loadUi("View/loginUi.ui", self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.conn = conecciones()
        self.reg = RegistrarInventario()

        #Creando conexion con ventana principal
        self.ventana_principal = Main_window()


        self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.label_3.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.btn_login.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        self.btn_register.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3)) # button_6
        self.btn_login.clicked.connect(self.abrir)

        self.widget_3.hide()
        self.btn_cambio.clicked.connect(self.changeForm) #button_7
        self.btn_register.clicked.connect(self.registrar)

    def changeForm(self):
        if self.btn_cambio.isChecked():
            self.widget_2.hide()
            self.widget_3.show()
            self.btn_cambio.setText("<")
        else:
            self.widget_2.show()
            self.widget_3.hide()
            self.btn_cambio.setText(">")

    def abrir(self):
        user = self.lnx_user.text()
        pw = self.lnx_password.text()


        cursor = self.conn.cursor()
        cursor.execute("select * from usuario where usuario='"+user+"' and password ='"+pw+"'")
        result = cursor.fetchone()
        if result:
            self.ventana_principal.show()
            self.hide()

        else:
            print("Contrseña incorrecta")

    def registrar(self):
        print("intentando registrar")
        nombre = self.lnx_1nombre.text()
        apellido = self.lnx_2nombre.text()
        user = self.lnx_usuario.text()
        cargo = self.cb_min.currentText()
        pw = self.lnx_password_2.text()
        pw_confirm = self.lnx_confirm_password.text()


        if pw == pw_confirm:
            print("mandando datos")
            self.reg.Insertar(cargo, nombre, apellido, user, pw)

        else:
            print("las contraseñas no coninciden")

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
        n_1 = self.lnx_1nombre.text()
        n_2 = self.lnx_2nombre.text()
        user = self.lnx_usuario.text()
        pw = self.lnx_password_2.text()
        pw_confirm = self.lnx_confirm_password.text()
        print("a")

        """
        abc = Symbol()
        lts = abc.vals()

        def cifrar(cadena, clave):
            text_cifrado = " "

            for letra in cadena:
                suma = lts.find(letra) + clave
                modulo = int(suma) % len(lts)
                text_cifrado = text_cifrado + str(lts[modulo])
            return text_cifrado

        #message = ""

        #message = input("Ingrese una frase: ")
        n = 7

        # new = message.replace('a', 'ñ')

        # print("PRUEBA" + new)

        resultado = cifrar(pw, n)
        #print("¡CLAVE!: " + resultado)
        # print("cifrar" + cifrar(message, n))
        # print("desifrado" + decifrar(resultado, n))

        key = Fernet.generate_key()
        objeto_cifrado = Fernet(key)
        texto_encriptado = objeto_cifrado.encrypt(str.encode(resultado))
        #print("Texto encriptado")
        #print(texto_encriptado)
        password = texto_encriptado.decode()
        """

        if pw == pw_confirm:
            print("mandando datos")
            self.reg.Insertar(n_1, n_2, user, pw)

        else:
            print("las contraseñas no coninciden")

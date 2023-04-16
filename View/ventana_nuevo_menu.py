import sys
import os
from datetime import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtWidgets
from modelos.tabla_inventario import ModeloPrincipal
from modelos.proveedores import ModeloProveedor
from modelos.tabla_cliente import ModeloCliente
from modelos.tabla_detalle import ModeloDetalle
from controladores.Register import RegistrarInventario
from controladores.cliente_register import RegistarCliente
from controladores.detalle_register import RegistarDetalle
from PyQt5.uic import loadUiType

# QComboBox

Ui_MainWindow, QMainWindow = loadUiType('nuevo_menu.ui')

class Main_window(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        self.modelo_principal = ModeloPrincipal()
        self.modelo_proveedor = ModeloProveedor()
        self.modelo_cliente = ModeloCliente()
        self.modelo_detalle = ModeloDetalle()
        self.registrar_usuario = RegistrarInventario()
        self.registrar_cliente = RegistarCliente()
        self.cliente_id = self.registrar_cliente.obtener_ultimo_id_cliente()
        self.fecha_actual = datetime.now()
        super().__init__()
        # Conectar interfaz grafica
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Conectar Botones con las paginas correspondientes
        self.btn_inventario.clicked.connect(self.pagina_inventario)
        self.btn_venta.clicked.connect(self.pagina_venta)
        self.btn_cliente.clicked.connect(self.pagina_cliente)
        self.btn_proveedor.clicked.connect(self.pagina_proveedor)
        self.btn_usuario.clicked.connect(self.pagina_usuario)
        self.btn_venta_nuevo.clicked.connect(self.pagina_venta_nuevo)

        # Inventario Ventana
        self.tabla_inv = self.tabla_inventario
        self.btn_listar.clicked.connect(lambda: self.modelo_principal.listar_productos(self.tabla_inv))
        self.btn_seleccionar.clicked.connect(lambda: self.modelo_principal.mostrar_producto(self.tabla_inv))
        self.btn_acutalizar.clicked.connect(lambda: self.modelo_principal.subir_productos(self.tabla_inv))
        self.btn_eliminar.clicked.connect(lambda: self.modelo_principal.eliminar_produc(self.tabla_inv))
        self.btn_crear_form.clicked.connect(lambda: self.modelo_principal.crearProducto(self.lnx_codigo_product.text(),
                                                                                        self.lnx_producto.text(),
                                                                                        self.lnx_existencias.text(),
                                                                                        self.lnx_precio_min.text(),
                                                                                        self.lnx_precio_may.text()))

        # Conectando los botones de la barra superior
        self.btn_restaurar.hide()
        self.btn_cerrar.clicked.connect(lambda: self.close())
        self.btn_minimizar.clicked.connect(self.minimizar)
        self.btn_restaurar.clicked.connect(self.restaurar)
        self.btn_maximizar.clicked.connect(self.maximizar)

    # Metodos de la barra de arriba
    def minimizar(self):
        self.showMinimized()

    def restaurar(self):
        self.showNormal()
        self.btn_restaurar.hide()
        self.btn_maximizar.show()

    def maximizar(self):
        self.showMaximized()
        self.btn_restaurar.show()
        self.btn_maximizar.hide()

    # Metodos pra conectar un boton con su pagina correspondiente
    def pagina_inventario(self):
        self.stackedWidget.setCurrentWidget(self.page_inventario)

    def pagina_venta(self):
        self.stackedWidget.setCurrentWidget(self.page_venta)

    def pagina_venta_nuevo(self):
        self.stackedWidget.setCurrentWidget(self.page_venta_nuevo)

    def pagina_cliente(self):
        self.stackedWidget.setCurrentWidget(self.page_cliente)

    def pagina_proveedor(self):
        self.stackedWidget.setCurrentWidget(self.page_proveedor)

    def pagina_usuario(self):
        self.stackedWidget.setCurrentWidget(self.page_usuario)


if __name__ == '__main__':
    # Crear la aplicación y la ventana principal
    app = QApplication(sys.argv)
    window = Main_window()
    window.show()

    sys.exit(app.exec_())

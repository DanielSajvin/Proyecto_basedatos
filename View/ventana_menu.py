import sys
import os
from datetime import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic, QtCore, QtWidgets
from modelos.tabla_inventario import ModeloPrincipal
from modelos.proveedores import ModeloProveedor
from modelos.tabla_cliente import ModeloCliente
from modelos.tabla_detalle import ModeloDetalle
from controladores.Register import RegistrarInventario
from controladores.cliente_register import RegistarCliente
from controladores.detalle_register import RegistarDetalle
from modelos.tabla_venta import ModeloVenta



class Main_window(QMainWindow):
    def __init__(self) -> None:
        self.modelo_principal = ModeloPrincipal()
        self.modelo_proveedor = ModeloProveedor()
        self.modelo_cliente = ModeloCliente()
        self.modelo_detalle = ModeloDetalle()
        self.registrar_usuario = RegistrarInventario()
        self.registrar_cliente = RegistarCliente()
        self.registrar_detalle = RegistarDetalle()
        self.listar_venta_tabla = ModeloVenta()
        self.cliente_id = self.registrar_cliente.obtener_ultimo_id_cliente()
        self.fecha_actual = datetime.now()

        super(Main_window, self).__init__()
        uic.loadUi("View/Menu_BD.ui", self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Mostar Usuario en curso

        self.cargo = self.registrar_usuario.obtener_cargo()
        self.mostrar_cargo.setText(str(self.cargo[0]))

        self.nombre = self.registrar_usuario.obtener_nombre()
        self.mostrar_nombre.setText(str(self.nombre[0]))

        self.apellido = self.registrar_usuario.obtener_apellido()
        self.mostrar_apellido.setText(str(self.apellido[0]))

        self.usuario_actual = self.registrar_usuario.obtener_usuario()
        self.mostrar_usuario.setText(str(self.usuario_actual[0]))
        #comentario 2 xd

        #self.usuario = self.registrar_usuario.getUsuario('1')
        #self.mostrar_cargo.setText(str(self.usuario[1]))
        #self.mostrar_nombre.setText(str(self.usuario[2]))
        #self.mostrar_apellido.setText(str(self.usuario[3]))
        #self.mostrar_usuario.setText(str(self.usuario[4]))

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


        # Ventas
        # form ventas
        self.btn_buscar.clicked.connect(self.obetener_dados_codigo)
        self.btn_visualizar_venta.clicked.connect(self.guardar_datos_venta)
        self.btn_guardar_venta.clicked.connect(self.mandar_datos_tabla_venta)

        # tabla ventas
        self.tabla_cliente_c = self.tabla_cliente
        self.btn_venta_v.clicked.connect(self.venta_tabla)
        self.btn_detalle_v.clicked.connect(self.venta_form)

        # Listar Venta
        self.tabla_venta_listar = self.table_form_venta
        self.btn_venta_v.clicked.connect(lambda: self.listar_venta_tabla.listar_venta(self.tabla_venta_listar))

        # Agregar datos a venta
        self.btn_agregar_venta.clicked.connect(lambda: self.listar_venta_tabla.crearventa(self.label_nombre.text(),
                                                                                          self.label_cantidad.text(),
                                                                                          self.label_costo.text(),
                                                                                          self.label_sub_total.text(),
                                                                                          self.lnx_anticipo.text(),
                                                                                          self.label_total.text(),
                                                                                          self.ultimo_id))

        # Cliente que existen en formulario de ventas
        self.btn_eliminar_cliente.clicked.connect(lambda: self.modelo_cliente.eliminar_produc(self.tabla_cliente_c))
        self.btn_guardar_venta.clicked.connect(lambda: self.modelo_cliente.crearcliente(self.lnx_nombre_v.text(),
                                                                                        self.lnc_nit_v.text(),
                                                                                        self.lnx_celular_v.text(),
                                                                                        self.lnx_email_v.text()))

        self.btn_crear.clicked.connect(self.crear)
        self.btn_listar.clicked.connect(self.tabla_inven)

        # Tabla y datos proveedor
        # listar datos de proveedor
        self.tabla_proveedor = self.tabla_listar_proveedor
        self.btn_listar_3.clicked.connect(lambda: self.modelo_proveedor.listar_proveedor(self.tabla_proveedor))
        self.registrar_proveedor.clicked.connect(lambda: self.modelo_proveedor.crearProovedor(
                                                 self.nombre_proveedor.text(),
                                                 self.producto_proveedor.text(),
                                                 self.cantidad_proveedor.text(),
                                                 self.total_proveedor.text()))

        self.btn_eliminar_3.clicked.connect(lambda: self.modelo_proveedor.eliminar_prov(self.tabla_proveedor))

        # Tabla y datos cliente
        # listar datos de cliente
        self.tabla_cliente = self.tabla_cliente
        self.btn_listar_4.clicked.connect(lambda: self.modelo_cliente.listar_cliente(self.tabla_cliente_c))
        self.registrar_cliente.clicked.connect(lambda: self.modelo_cliente.crearcliente(self.nombre_cliente.text(),
                                                                                        self.nit_cliente.text(),
                                                                                        self.celular_cliente.text(),
                                                                                        self.email_cliente.text()))


        # comentario xd
        # Conectando los botones de la barra superior
        self.bt_restaurar.hide()
        self.bt_cerrar.clicked.connect(lambda: self.close())
        self.bt_minimizar.clicked.connect(self.minimizar)
        self.bt_restaurar.clicked.connect(self.restaurar)
        self.bt_maximizar.clicked.connect(self.maximizar)

        # Conectando las paginas con su boton asignado

        self.btn_inventario.clicked.connect(self.inventario)
        self.btn_cliente.clicked.connect(self.cliente)
        self.btn_venta.clicked.connect(self.venta)
        self.btn_proveedor.clicked.connect(self.proveedor)
        self.btn_usuario.clicked.connect(self.usuario)
        #self.boton_registrarpr.clicked.connect(self.registrar_proveedor)
        self.btn_crear_3.clicked.connect(self.crear_proveedor)
        self.btn_listar_3.clicked.connect(self.listar_proveedor)
        self.btn_listar_4.clicked.connect(self.listar_cliente)
        self.btn_crear_4.clicked.connect(self.crear_cliente)

        # Tabla de detalles
        # id_detalle - producto - fecha - entregado - sub_total - total - id_tipo - usuario_id - cliete_id
        self.btn_finaliza_compra.clicked.connect(self.borrar_line_edit_venta)

        self.btn_guardar_venta.clicked.connect(lambda: self.modelo_detalle.creardetalle(
                                                                                        self.fecha_actual.date(),
                                                                                        "si",
                                                                                        1,
                                                                                        1,
                                                                                        self.cliente_id))

        self.btn_agregar_venta.clicked.connect(self.prueba_boton)

        # Ventas
        self.btn_agregar_venta.clicked.connect(self.restar_inventario)


        self.producto = self.label_nombre.text()
        self.fecha = self.fecha_actual.date()
        self.entregado = "Si"
        self.sub_total = self.label_sub_total.text()
        self.total = self.label_total.text()
        self.tipo_id = 1
        self.usuario_id = 1
        self.cliente_id = self.cliente_id




    def prueba_boton(self):
        print("tocando botoonnnn ----------------------------")

    def minimizar(self):
        self.showMinimized()

    def restaurar(self):
        self.showNormal()
        self.bt_restaurar.hide()
        self.bt_maximizar.show()

    def maximizar(self):
        self.showMaximized()
        self.bt_restaurar.show()
        self.bt_maximizar.hide()

    def ultimo_id(self):
        self.id_ultimo = self.registrar_detalle.obtener_ultimo_id()
        return self.id_ultimo


    def inventario(self):
        self.stackedWidget.setCurrentWidget(self.page_inventario)

    def cliente(self):
        self.stackedWidget.setCurrentWidget(self.page_clientes)

    def venta(self):
        self.stackedWidget.setCurrentWidget(self.page_venta)

    def proveedor(self):
        self.stackedWidget.setCurrentWidget(self.page_proveedor)

    def usuario(self):
        self.stackedWidget.setCurrentWidget(self.page_usuario)

    def crear_proveedor(self):
        self.stackedWidget_4.setCurrentWidget(self.page_form_prov)

    def listar_proveedor(self):
        self.stackedWidget_4.setCurrentWidget(self.page_tabla_prov)

    def listar_cliente(self):
        self.stackedWidget_5.setCurrentWidget(self.page_tabla_cliente)

    def crear_cliente(self):
        self.stackedWidget_5.setCurrentWidget(self.page_form_cliente)

    def crear(self):
        self.stackedWidget_2.setCurrentWidget(self.page_form_inv)

    def tabla_inven(self):
        self.stackedWidget_2.setCurrentWidget(self.page_tb_inv)

    def venta_tabla(self):
        self.stackedWidget_3.setCurrentWidget(self.page_tabla_venta)

    def venta_form(self):
        self.stackedWidget_3.setCurrentWidget(self.page_form_venta)

    def obetener_dados_codigo(self):
        # id_detalle - producto - fecha - entregado - sub_total - total - id_tipo - usuario_id - cliete_id
        precio_uni = ""
        cod = self.lnx_op_codigo.text()
        product = self.registrar_usuario.obtener_por_codigo(cod)
        if self.cb_min.currentText() == 'Minorista':
            precio_uni = product[4]
        elif self.cb_min.currentText() == 'Mayorista':
            precio_uni = product[5]
        costo = str(precio_uni)


        nombre = product[2]
        self.label_nombre.setText(str(nombre))
        self.label_costo.setText(str(costo))
        return precio_uni

    def guardar_datos_venta(self):
        # id_detalle - producto - fecha - entregado - sub_total - total - id_tipo - usuario_id - cliete_id
        cantidad = self.label_cantidad.text()
        anticipo = self.lnx_anticipo.text()
        anticipo = float(anticipo)


        precio_uni = self.obetener_dados_codigo()
        precio = precio_uni
        new_cantidad = float(cantidad)
        sub_total = new_cantidad * precio

        total = sub_total - anticipo

        self.label_sub_total.setText(str(sub_total))
        self.label_total.setText(str(total))

    def mandar_datos_tabla_venta(self):
        # id_detalle - producto - fecha - entregado - sub_total - total - id_tipo - usuario_id - cliete_id
        nombre = self.lnx_nombre_v.text()
        nit = self.lnc_nit_v.text()
        celular = self.lnc_nit_v.text()
        email = self.lnx_email_v.text()

    def borrar_line_edit_venta(self):
        self.lnx_nombre_v.clear()
        self.lnc_nit_v.clear()
        self.lnx_celular_v.clear()
        self.lnx_email_v.clear()
        self.lnx_op_codigo.clear()
        self.label_nombre.setText("")
        self.label_cantidad.clear()
        self.label_costo.setText("")
        self.lnx_anticipo.clear()
        self.label_sub_total.setText("")
        self.label_total.setText("")









    def restar_inventario(self):
        cod = self.lnx_op_codigo.text()
        cantidad = self.label_cantidad.text()
        cantidad = int(cantidad)
        print("mandando datos de cantidad")
        self.modelo_principal.modificar_existencias(cod, cantidad)



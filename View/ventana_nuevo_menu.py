import sys
import os
import datetime
import webbrowser
from datetime import datetime
from typing import TypeVar

import pdfrw
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
from modelos.tabla_venta import ModeloVenta
from modelos.tabla_pedido import ModeloPedido
from PyQt5.uic import loadUiType
from controladores.controlar_venta import BaseDatosInfo
from controladores.venta_registe import RegistrarVenta
import random
import string

# QComboBox

Ui_MainWindow, QMainWindow = loadUiType('View/nuevo_menu.ui')

T = TypeVar('T')
class Main_window_nuevo(QMainWindow, Ui_MainWindow):
    def __init__(self, user, main_login) -> None:
        _translate = QtCore.QCoreApplication.translate
        self.modelo_principal = ModeloPrincipal()
        self.modelo_proveedor = ModeloProveedor()
        self.modelo_cliente = ModeloCliente()
        self.modelo_detalle = ModeloDetalle()
        self.registrar_usuario = RegistrarInventario()
        self.listar_venta_tabla = ModeloVenta()
        self.registrar_detalle = RegistarDetalle()
        self.registrar_cliente_c = RegistarCliente()
        self.clietes_deben = self.registrar_cliente_c.clientes_deben()
        self.pedido = ModeloPedido()
        self.registrar_venta = RegistrarVenta()

        self.reg = RegistrarInventario()

        self.info = BaseDatosInfo()

        self.cliente_id = self.registrar_cliente_c.obtener_ultimo_id_cliente()
        # self.registrar_cliente.clientes_deben()
        self.login = main_login

        self.fecha_actual = datetime.now()



        #Tabla
        self.item: T = None

        super().__init__()

        self.user = user

        # Conectar interfaz grafica
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        #self.fecha_pedido.setText("")

        # Tabla
        # item = self.tabla_int.item(0, 0)
        # item.setText(_translate("MainWindow", str(self.info.base_datos(0, 0))))
        # for fil in range(0, 10):
        #     for colum in range(0, 6):
        #         item = self.tabla_int.item(fil, colum)
        #         item.setText(_translate("MainWindow", str(self.info.base_datos(fil, colum))))
        #         if (colum == 6):
        #             cantidad = int(self.info.base_datos(fil, colum - 1))
        #             precio = int(self.info.base_datos(fil, colum - 2))
        #             monto_total = cantidad * precio
        #             item.setText(_translate("MainWindow", str(monto_total) + '.00'))

        # bloqueando botones segun el cargo del usuario que ingrese al menu

        # el usuario que ingreso al menu
        self.usuario = self.reg.getUsusario_user(user)
        self.tipo_usuario = self.usuario[1]
        self.id_usuario = self.usuario[0]
        self.desabilitar()
        self.usuario_mostrar()

        self.id_ultimo = self.registrar_detalle.obtener_ultimo_id()

        # Conectar Botones con las paginas correspondientes
        self.btn_inventario.clicked.connect(self.pagina_inventario)
        self.btn_venta.clicked.connect(self.pagina_venta)
        self.btn_cliente.clicked.connect(self.pagina_cliente)
        self.btn_proveedor.clicked.connect(self.pagina_proveedor)
        self.btn_usuario.clicked.connect(self.pagina_usuario)
        self.btn_venta_nuevo.clicked.connect(self.pagina_venta_nuevo)
        self.btn_cotizacion.clicked.connect(self.pagina_cotizacion)

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
        # self.btn_guardar_venta.clicked.connect(self.mandar_datos_tabla_venta)

        # tabla ventas
        # self.tabla_cliente_c = self.tabla_cliente
        # self.btn_venta_v.clicked.connect(self.venta_tabla)
        # self.btn_detalle_v.clicked.connect(self.venta_form)

        # Cotizacion

        # Listar Venta
        self.tabla_venta_listar = self.table_form_venta
        self.btn_agregar_venta.clicked.connect(lambda: self.listar_venta_tabla.listar_venta(self.tabla_venta_listar))
        self.btn_listar_ventas.clicked.connect(lambda: self.listar_venta_tabla.listar_venta(self.tabla_venta_listar))

        # Agregar datos a venta
        self.btn_agregar_venta.clicked.connect(lambda: self.listar_venta_tabla.crearventa(self.label_nombre.text(),
                                                                                          self.label_cantidad.text(),
                                                                                          self.label_costo.text(),
                                                                                          self.label_sub_total.text(),
                                                                                          self.lnx_anticipo.text(),
                                                                                          self.label_total.text(),
                                                                                          self.registrar_detalle.obtener_ultimo_id()))
        self.tabla_cliente_c = self.tabla_cliente
        self.tabla_cliente = self.tabla_cliente
        self.tabla_clientes_deben = self.tabla_clientes_d
        self.tabla_nombres_cliente = self.tabla_cliente_v

        # print(f"estos son los clientes que deben: {self.clientes_deben}")
        self.bot_listar.clicked.connect(lambda: self.modelo_cliente.tabla_nombres(self.tabla_nombres_cliente))
        self.btn_listar_cd.clicked.connect(lambda: self.modelo_cliente.obtener_deben(self.tabla_clientes_deben))
        self.btn_deudas.clicked.connect(lambda: self.modelo_cliente.obtener_deben(self.tabla_clientes_deben))
        self.btn_actualizar_cd.clicked.connect(self.actulizar_deudas)
        self.btn_listar_4.clicked.connect(lambda: self.modelo_cliente.listar_cliente(self.tabla_cliente_c))
        self.registrar_cliente.clicked.connect(lambda: self.modelo_cliente.crearcliente(self.nombre_cliente.text(),
                                                                                        self.nit_cliente.text(),
                                                                                        self.celular_cliente.text(),
                                                                                        self.email_cliente.text(),
                                                                                        1))
        self.registrar_cliente.clicked.connect(self.limpiar_labels_cliente)
        self.btn_deshabilitar.clicked.connect(self.deshabilitar_cliente)

        # clientes deudas
        self.btn_deudas.clicked.connect(self.page_deudas)

        # Conecta la señal clicked() del calendario a la función date_selected
        self.calendario_pedido = self.calendario_pedido

        self.calendario_pedido.clicked.connect(self.obtener_fecha_seleccionada)


        self.btn_pedido.clicked.connect(lambda: self.modelo_detalle.creardetalle(
            self.fecha_seleccionada,
            "no",
            1,
            self.id_usuario,
            self.obtener_ciente))

        self.btn_agregar_venta.clicked.connect(lambda: self.modelo_detalle.creardetalle(
            self.fecha_actual.date(),
            "si",
            1,
            self.id_usuario,
            self.obtener_ciente))
        # Tabla y datos proveedor
        # listar datos de proveedor
        self.tabla_proveedor = self.tabla_listar_proveedor
        self.btn_listar_3.clicked.connect(lambda: self.modelo_proveedor.listar_proveedor(self.tabla_proveedor))
        self.registrar_proveedor.clicked.connect(lambda: self.modelo_proveedor.crearProovedor(
            self.nombre_proveedor.text(),
            self.producto_proveedor.text(),
            self.cantidad_proveedor.text(),
            self.total_proveedor.text()))
        self.registrar_proveedor.clicked.connect(self.limpiar_provedor)

        self.btn_eliminar_3.clicked.connect(lambda: self.modelo_proveedor.eliminar_prov(self.tabla_proveedor))

        # Conectando los botones de la barra superior
        self.btn_restaurar.hide()
        self.btn_cerrar.clicked.connect(lambda: self.close())
        self.btn_minimizar.clicked.connect(self.minimizar)
        self.btn_restaurar.clicked.connect(self.restaurar)
        self.btn_maximizar.clicked.connect(self.maximizar)

        # Elementos tabla transitoria
        self.lnx_op_codigo.text()
        self.label_nombre.text()
        self.cb_min.currentText()  # para el que despliega dos opciones

        # cerrar sesion en usuario
        self.btn_cerrar_sesion.clicked.connect(self.back_to_login)

        # Ventas (Abdo)
        self.tabla_transitoria_venta = self.boleta
        self.tabla_venta = self.boleta
        self.bot_agregar_2.clicked.connect(lambda: self.listar_venta_tabla.eliminar_produc(self.tabla_venta))
        # self.btn_limpiar.clicked.connect(lambda: self.listar_venta_tabla.limpiar_tabla_venta(self.tabla_venta))
        self.fecha.setText(str(self.fecha_actual.date()))
        self.bot_listar.clicked.connect(lambda: self.modelo_principal.listar_productos(self.tabla_int))
        self.btn_listar_tabla_v.clicked.connect(lambda: self.listar_venta_tabla.listar_venta_transitorio(self.tabla_transitoria_venta))
        # self.bot_agregar.clicked.connect(self.cotizar_venta_producto)
        self.bot_agregar.clicked.connect(self.obetener_dados_codigo)
        self.btn_calcular.clicked.connect(self.guardar_datos_venta)
        self.generar_venta.clicked.connect(self.generar_tabla_venta)
        self.btn_limpiar.clicked.connect(self.eliminar_tabla_transitoria)

        # Ventas (Angel)
        self.terminar.clicked.connect(self.guardad_venta_f)

        self.terminar.clicked.connect(self.guardar_datos_venta_f)

        self.fechapedido = str(self.calendarWidget.clicked.connect(self.obtener_fecha_seleccionada))


        # -------------------------------------------------------
        # -------------------------------------------------------
        # -------------------------------------------------------
        # ----------------------- Cambiar para que no salga la ubicacion de memoria --------------------------------
        self.fecha_pedido.setText(str(self.fechapedido))

        # -------------------- Generar cotizacion -------------------------------------------------------
        self.btn_reCotizar.clicked.connect(self.realizarCotizacion)


        # ----------------- Clientes en Ventas ---------------------
        self.btn_crear_cliente_v.clicked.connect(self.venta_cliente)
        self.btn_venta_c.clicked.connect(self.cliente_venta)

        #-----------------Mostrar Pedidos-------------------
        self.tabla_pedido = self.list_pedido
        self.btn_mospedido.clicked.connect(lambda: self.pedido.listar_pedido(self.tabla_pedido))

    def deshabilitar_cliente(self):
        id = self.id_deshabilitar.text()
        id = int(id)

        self.registrar_cliente_c.deshabilitar_clientes(id)

    def guardad_venta_f(self):
        cursor = self.registrar_venta.obtener_venta_transitoria()
        id = self.obtener_ciente()
        id_cliente = id[0]
        codigos = []

        # Recorrer los resultados de la consulta y agregar los valores a las listas
        for (id_venta, codigo, producto, cantidad, precio, sub_total, anticipo, total) in cursor:
            codigos.append(codigo)

        ventas = zip(codigos)
        for venta in ventas:
            id_invent = self.obtener_id_codigo_producto(*venta)

        pedido = self.fecha_pedido.text()

        if str(self.fecha_actual.date()) == pedido:

            self.modelo_detalle.creardetalle(
                self.fecha_actual.date(),
                "si",
                1,
                self.id_usuario,
                id_cliente,
                id_invent)

        else:
            self.modelo_detalle.creardetalle(
                self.fecha_seleccionada,
                "no",
                1,
                self.id_usuario,
                id_cliente,
                id_invent)

    def obtener_id_codigo_producto(self, cod):
        product = self.registrar_usuario.get_codigo(cod)
        id = product[0]
        return id

    def guardar_datos_venta_f(self):
        cursor = self.registrar_venta.obtener_venta_transitoria()
        id_ventas = []
        codigos = []
        productos = []
        cantidades = []
        precios = []
        sub_totales = []
        anticipos = []
        totales = []

        # Recorrer los resultados de la consulta y agregar los valores a las listas
        for (id_venta, codigo, producto, cantidad, precio, sub_total, anticipo, total) in cursor:
            id_ventas.append(id_venta)
            codigos.append(codigo)
            productos.append(producto)
            cantidades.append(cantidad)
            precios.append(precio)
            sub_totales.append(sub_total)
            anticipos.append(anticipo)
            totales.append(total)

        ventas = zip(id_ventas, codigos, productos, cantidades, precios, sub_totales, anticipos, totales)
        id_detalle = self.registrar_detalle.obtener_ultimo_id()
        for venta in ventas:
            self.listar_venta_tabla.transicion_vt_a_v(id_detalle, *venta)

        # Cerrar el cursor y la conexión a la base de datos
        #self.listar_venta_tabla.crearventa()
        #pass

    def venta_cliente(self):
        self.stackedWidget.setCurrentWidget(self.page_cliente)

    def cliente_venta(self):
        self.stackedWidget.setCurrentWidget(self.page_venta)

    def write_pdf(self, template, output, data_dict):
        ANNOT_KEY = '/Annots'
        ANNOT_FIELD_KEY = '/T'
        ANNOT_VAL_KEY = '/V'
        ANNOT_RECT_KEY = '/Rect'
        SUBTYPE_KEY = '/Subtype'
        WIDGET_SUBTYPE_KEY = '/Widget'

        def fill_pdf(input_pdf_path, output_pdf_path, data_dict):
            template_pdf = pdfrw.PdfReader(input_pdf_path)

            for page in template_pdf.pages:
                annotations = page[ANNOT_KEY]

                for annotation in annotations:
                    if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
                        if annotation[ANNOT_FIELD_KEY]:
                            key = annotation[ANNOT_FIELD_KEY][1:-1]

                            if key in data_dict.keys():
                                if type(data_dict[key]) == bool:
                                    if data_dict[key] == True:
                                        annotation.update(pdfrw.PdfDict(AS=pdfrw.PdfName('Yes')))

                                else:
                                    annotation.update(pdfrw.PdfDict(V='{}'.format(data_dict[key])))
                                    annotation.update(pdfrw.PdfDict(AP=''))

            template_pdf.Root.AcroForm.update(pdfrw.PdfDict(NeedAppearances=pdfrw.PdfObject('true')))
            pdfrw.PdfWriter().write(output_pdf_path, template_pdf)

        fill_pdf(template, output, data_dict)
        webbrowser.open_new(output)

    def realizarCotizacion(self):
        letras = string.ascii_uppercase
        cadena = ''.join(random.choice(letras) for i in range(3))
        numero = random.randint(0, 9)
        try:
            cot = cadena + str(numero)

            producto1 = self.nom_pro.text()
            fecha_hoy = self.fecha.text()
            # cantidad1 = self.spinBox.text()
            cantidad1 = self.spinBox.value()
            mayorista1 = self.p_unit_2.text()
            minorista1 = self.p_unit.text()
            total1 = self.monto_t.text()
            cnd_elem = self.info.elemtos_ventas()
            codigo1 = self.reg.get_code_by_product(self.boleta.item(cnd_elem - 3, 0).text())
            codigo2 = self.reg.get_code_by_product(self.boleta.item(cnd_elem - 2, 0).text())
            codigo3 = self.reg.get_code_by_product(self.boleta.item(cnd_elem - 1, 0).text())

            #region = self.pedir2.text()
            #print(region)
            #finca = self.pedir3.text()
            #estado = self.pedir4.text()
            #tipo = self.pedir1.currentText()

            if producto1 != '--Seleccionar--' and codigo1 != '--Seleccionar--':

                # cantidad = int(self.cantidad_line.text())
                cantidad = 3

                if cantidad > 0:
                    QMessageBox.about(self, 'Aviso', 'Se ha generado la cotización!')

                    data_dict = {
                        'Cotizacion': cot,
                        'Fecha': fecha_hoy,
                        'Cliente': '',
                        'Cod1': codigo1[0],
                        'Cod2': codigo2[0],
                        'Cod3': codigo3[0],
                        'Produ1': self.boleta.item(cnd_elem - 3, 0).text(),
                        'Produ2': self.boleta.item(cnd_elem - 2, 0).text(),
                        'Produ3': self.boleta.item(cnd_elem - 1, 0).text(),
                        'Can1': self.boleta.item(cnd_elem - 3, 1).text(),
                        'Can2': self.boleta.item(cnd_elem - 2, 1).text(),
                        'Can3': self.boleta.item(cnd_elem - 1, 1).text(),
                        'May1': self.boleta.item(cnd_elem - 3, 2).text(),
                        'May2': self.boleta.item(cnd_elem - 2, 2).text(),
                        'May3': self.boleta.item(cnd_elem - 1, 2).text(),
                        'Min1': '',
                        'Min2': '',
                        'Min3': '',
                        'Total1': self.boleta.item(cnd_elem - 3, 4).text(),
                        'Total2': self.boleta.item(cnd_elem - 2, 4).text(),
                        'Total3': self.boleta.item(cnd_elem - 1, 4).text()

                    }

                    self.write_pdf('View/CotizaciónCliente.pdf', 'cotizacion_final.pdf', data_dict)

                    #self.cantidad_line.clear()

                else:
                    raise Exception('Debe ser un valor mayor a 0')

            else:
                raise Exception('No se ha seleccionado uno de los parametros para la cotización.')

        except Exception as e:
            QMessageBox.critical(self, 'Error', str(e))

    # -------------------- Generar cotizacion -------------------------------------------------------

    def cotizar_venta_producto(self):
        for valor in range(0, 10):
            if str(valor) == self.cod_bus.text():
                product = self.reg.getProduct(valor)
                self.nom_pro.setText(product[2])
                self.p_unit.setText(str(product[4]))
                self.p_unit_2.setText(str(product[5]))
                self.Lab.setText(str(product[3]))
                cant = self.spinBox.text()
                monto_und = int(product[4]) * int(cant)
                if (int(cant) > 0):
                    self.monto_t.setText(str(monto_und) + ".00")
                else:
                    self.monto_t.setText(".00")

    def generar_tabla_venta(self):
        _translate = QtCore.QCoreApplication.translate
        codigo = self.cod_bus.text()
        producto = self.nom_pro.text()
        cantidad = self.spinBox.text()
        precio_und = self.p_unit.text()
        anticipo = self.vendedor.text()
        subtotal = int(cantidad) * float(precio_und)
        ant = self.vendedor.text()
        ant = int(ant)
        total = subtotal - ant
        # self.info.insertarVentaTransitoria(producto, cantidad, precio_und, anticipo, subtotal)
        self.registrar_venta.escribir_base_datos_transitoria(codigo, producto, cantidad,
                                                             precio_und, anticipo, subtotal, total)

        self.tabla_transitoria_venta = self.boleta
        self.listar_venta_tabla.listar_venta_transitorio(self.tabla_transitoria_venta)

        # cnd_elem = self.info.elemtos_ventas()  # Cantidad de elementos
        # print(cnd_elem)
        # self.item = self.boleta.item(cnd_elem - 1, 0)
        # self.item.setText(_translate("MainWindow", producto))
        #
        # self.item = self.boleta.item(cnd_elem - 1, 1)
        # self.item.setText(_translate("MainWindow", cantidad))
        #
        # self.item = self.boleta.item(cnd_elem - 1, 2)
        #
        # self.item.setText(_translate("MainWindow", precio_und))
        #
        # self.item = self.boleta.item(cnd_elem - 1, 3)
        # self.item.setText(_translate("MainWindow", str(anticipo)))
        #
        # self.item = self.boleta.item(cnd_elem - 1, 4)
        # self.item.setText(_translate("MainWindow", str(subtotal - int(anticipo))))
        #
        # self.total_general.setText(str(self.info.monto_total(cnd_elem) - int(anticipo)))

# ------------------------------------ELiminar datos de la tabla transitoria -------------------------------------

    def eliminar_tabla_transitoria(self):
        self.reg.delete_tabla()

    def back_to_login(self):
        # Cerrar la ventana actual
        self.close()
        self.login.show()
        # Mostrar la ventana de login nuevamente
        # login_window = Main_login()
        # login_window.show()

    def limpiar_provedor(self):
        self.nombre_proveedor.setText("")
        self.producto_proveedor.setText("")
        self.cantidad_proveedor.setText("")
        self.total_proveedor.setText("")

    def ulitmo_id(self):
        self.id_ultimo = self.registrar_detalle.obtener_ultimo_id()
        print(self.id_ultimo)
        return self.id_ultimo

    # metodo para dessabilitar segun el cargo
    def desabilitar(self):
        self.btn_venta_nuevo.setVisible(False)
        if self.tipo_usuario == "Empleado":
            self.btn_inventario.setVisible(False)
            self.btn_proveedor.setVisible(False)
            self.btn_cliente.setVisible(False)

    def usuario_mostrar(self):
        self.lnx_cargo_u.setEnabled(False)
        self.lnx_nombre_u.setEnabled(False)
        self.lnx_apellido_u.setEnabled(False)
        self.lnl_usuario_u.setEnabled(False)

        cargo = self.usuario[1]
        nombre = self.usuario[2]
        apellido = self.usuario[3]
        usuario = self.usuario[4]

        self.lnx_cargo_u.setText(str(cargo))
        self.lnx_nombre_u.setText(str(nombre))
        self.lnx_apellido_u.setText(str(apellido))
        self.lnl_usuario_u.setText(str(usuario))

    def minimizar(self):
        self.showMinimized()

    # Metodos de la barra de arriba
    def restaurar(self):
        self.showNormal()
        self.btn_restaurar.hide()
        self.btn_maximizar.show()

    def maximizar(self):
        self.showMaximized()
        self.btn_restaurar.show()
        self.btn_maximizar.hide()

    def actulizar_deudas(self):
        id = self.lnx_id_cd.text()
        pago = self.lnx_pago_cd.text()
        pago = float(pago)
        self.listar_venta_tabla.modificar_anticipo(id, pago)

        self.lnx_id_cd.setText("")
        self.lnx_pago_cd.setText("")

    def obtener_ciente(self):
        self.cliente_id_c = self.cliente.text()
        print(f"este es el nombre del cliente: {self.cliente_id_c}")
        self.id_cliente = self.registrar_cliente_c.get_c_nombre(self.cliente_id_c)
        return self.id_cliente
    # Metodos pra conectar un boton con su pagina correspondiente
    def pagina_cotizacion(self):
        self.stackedWidget.setCurrentWidget(self.page_cotizacion)

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

    def page_deudas(self):
        self.stackedWidget.setCurrentWidget(self.page_cliente_deben)

    def obtener_fecha_seleccionada(self, fecha_seleccionada):
        # Convertir la fecha seleccionada en un objeto QDate
        fecha = QDate(fecha_seleccionada)

        # Imprimir la fecha seleccionada en consola
        fecha_pedido = fecha.toString("yyyy-MM-dd")
        self.fecha_pedido.setText(fecha_pedido)

        # Convertir la fecha de QDate a date de datetime
        fecha_datetime = datetime(fecha.year(), fecha.month(), fecha.day()).date()

        # Almacenar la fecha seleccionada en una variable como date de datetime
        self.fecha_seleccionada = fecha_datetime

    def obetener_dados_codigo(self):
        # id_detalle - producto - fecha - entregado - sub_total - total - id_tipo - usuario_id - cliete_id
        precio_uni = ""
        cod = self.cod_bus.text()

        product = self.registrar_usuario.obtener_por_codigo(cod)
        print(product)
        if self.turno.currentText() == 'Minorista':
            precio_uni = product[4]
        elif self.turno.currentText() == 'Mayorista':
            precio_uni = product[5]

        costo = str(precio_uni)
        nombre = product[2]
        existencias = product[3]
        self.nom_pro.setText(str(nombre))
        self.p_unit.setText(str(costo))
        self.Lab.setText(str(existencias))
        return precio_uni

    def guardar_datos_venta(self):
        # id_detalle - producto - fecha - entregado - sub_total - total - id_tipo - usuario_id - cliete_id
        cantidad = self.spinBox.value()
        anticipo = self.vendedor.text()
        anticipo = float(anticipo)
        # print(f"anticipo:{anticipo}")

        precio_uni = self.obetener_dados_codigo()
        precio = precio_uni
        new_cantidad = float(cantidad)
        sub_total = new_cantidad * precio

        total = sub_total - anticipo

        self.lnx_sub_total.setText(str(sub_total))
        self.monto_t.setText(str(total))

    def mandar_datos_tabla_venta(self):
        # id_detalle - producto - fecha - entregado - sub_total - total - id_tipo - usuario_id - cliete_id
        nombre = self.lnx_nombre_v.text()
        nit = self.lnc_nit_v.text()
        celular = self.lnc_nit_v.text()
        email = self.lnx_email_v.text()

    def limpiar_labels_cliente(self):
        self.nombre_cliente.clear()
        self.nit_cliente.clear()
        self.celular_cliente.clear()
        self.email_cliente.clear()

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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Main_window_nuevo()
    ventana.show()
    sys.exit(app.exec_())

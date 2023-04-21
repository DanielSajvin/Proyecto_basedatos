import sys
import os
import datetime
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
from modelos.tabla_venta import ModeloVenta
from PyQt5.uic import loadUiType
from controladores.controlar_venta import BaseDatosInfo
from controladores.venta_registe import RegistrarVenta
# import webbrowser
# import pdfrw

# QComboBox

Ui_MainWindow, QMainWindow = loadUiType('View/nuevo_menu.ui')



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
        self.registrar_cliente = RegistarCliente()
        self.clietes_deben = self.registrar_cliente.clientes_deben()

        self.registrar_venta = RegistrarVenta()

        self.reg = RegistrarInventario()

        self.info = BaseDatosInfo()

        self.cliente_id = self.registrar_cliente.obtener_ultimo_id_cliente()
        #self.registrar_cliente.clientes_deben()
        self.login = main_login

        self.fecha_actual = datetime.now()

        super().__init__()

        self.user = user
        # Conectar interfaz grafica
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


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
        #self.btn_venta_v.clicked.connect(self.venta_tabla)
        #self.btn_detalle_v.clicked.connect(self.venta_form)

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

        # print(f"estos son los clientes que deben: {self.clientes_deben}")
        self.btn_listar_cd.clicked.connect(lambda: self.modelo_cliente.obtener_deben(self.tabla_clientes_deben))
        self.btn_deudas.clicked.connect(lambda: self.modelo_cliente.obtener_deben(self.tabla_clientes_deben))
        self.btn_actualizar_cd.clicked.connect(self.actulizar_deudas)
        self.btn_listar_4.clicked.connect(lambda: self.modelo_cliente.listar_cliente(self.tabla_cliente_c))
        self.registrar_cliente.clicked.connect(lambda: self.modelo_cliente.crearcliente(self.nombre_cliente.text(),
                                                                                         self.nit_cliente.text(),
                                                                                         self.celular_cliente.text(),
                                                                                         self.email_cliente.text()))

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
                                                                                        self.cliente_id))

        self.btn_agregar_venta.clicked.connect(lambda: self.modelo_detalle.creardetalle(
                                                                                        self.fecha_actual.date(),
                                                                                        "si",
                                                                                        1,
                                                                                        self.id_usuario,
                                                                                        self.cliente_id))
        #Tabla y datos proveedor
        #listar datos de proveedor
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
        self.cb_min.currentText()  #para el que despliega dos opciones

        # cerrar sesion en usuario
        self.btn_cerrar_sesion.clicked.connect(self.back_to_login)

        #Ventas (Abdo)
        self.fecha.setText(str(self.fecha_actual.date()))
        self.bot_listar.clicked.connect(lambda: self.modelo_principal.listar_productos(self.tabla_int))
        self.bot_agregar.clicked.connect(self.cotizar_venta_producto)
        self.generar_venta.clicked.connect(self.generar_tabla_venta)

        self.fechapedido = str(self.calendarWidget.clicked.connect(self.obtener_fecha_seleccionada))
        self.fecha_pedido.setText(str(self.fechapedido))




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
        # self.info.insertarVentaTransitoria(producto, cantidad, precio_und, anticipo, subtotal)
        self.registrar_venta.escribir_base_datos_transitoria(codigo, producto, cantidad, precio_und, anticipo, subtotal)

        cnd_elem = self.info.elemtos_ventas() #Cantidad de elementos
        print(cnd_elem)
        item = self.boleta.item(cnd_elem - 1, 0)
        item.setText(_translate("MainWindow", producto))

        item = self.boleta.item(cnd_elem - 1, 1)
        item.setText(_translate("MainWindow", cantidad))

        item = self.boleta.item(cnd_elem - 1, 2)
        print(item)
        item.setText(_translate("MainWindow", precio_und))

        item = self.boleta.item(cnd_elem - 1, 3)
        print(item)
        item.setText(_translate("MainWindow", str(anticipo)))

        item = self.boleta.item(cnd_elem - 1, 4)
        item.setText(_translate("MainWindow", str(subtotal - int(anticipo))))

        self.total_general.setText(str(self.info.monto_total(cnd_elem) - int(anticipo)))

    def back_to_login(self):
        # Cerrar la ventana actual
        self.close()
        self.login.show()
        # Mostrar la ventana de login nuevamente
        #login_window = Main_login()
        #login_window.show()

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
        cod = self.lnx_op_codigo.text()

        product = self.registrar_usuario.obtener_por_codigo(cod)
        print(product)
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
        print("Visualisando datos")
        cantidad = self.label_cantidad.text()
        anticipo = self.lnx_anticipo.text()
        anticipo = float(anticipo)
        print(f"anticipo:{anticipo}")

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
        try:
            region = self.region_box.currentText()
            finca = self.finca_box.currentText()
            estado = self.estado_box.currentText()
            tipo = self.tipo_box.currentText()

            if region != '--Seleccionar--' and finca != '--Seleccionar--' and estado != '--Seleccionar--' and tipo != '--Seleccionar--':

                cantidad = int(self.cantidad_line.text())

                if cantidad > 0:
                    QMessageBox.about(self, 'Aviso', 'Se ha generado la cotización!')

                    data_dict = {
                        'Fecha': date.today(),
                        'Numero': '0',
                        'Cliente': '',
                        'Nit': 'C/F',
                        'Direccion': 'Ciudad',
                        'Telefono': '',
                        'Correo': '',
                        'Producto': f"Café de {region}, finca {finca}, {estado}, {tipo}",
                        'Producto1': '',
                        'Producto3': '',
                        'Producto4': '',
                        'Producto5': '',
                        'Producto2': '',
                        'Precio1': '',
                        'Precio2': '',
                        'Precio3': '',
                        'Precio4': '',
                        'Precio5': '',
                        'Unidades': cantidad,
                        'Unidades1': '',
                        'Unidades2': '',
                        'Unidades3': '',
                        'Unidades4': '',
                        'Unidades5': '',
                        'Precio': '',
                        'Preciot': '',
                        'Preciot1': '',
                        'Preciot2': '',
                        'Preciot3': '',
                        'Preciot4': '',
                        'Totalp': '',
                        'Descuento': '',
                        'Total': ''
                    }

                    self.write_pdf('cotizacion.pdf', 'cotizacion_final.pdf', data_dict)

                    self.cantidad_line.clear()

                else:
                    raise Exception('Debe ser un valor mayor a 0')

            else:
                raise Exception('No se ha seleccionado uno de los parametros para la cotización.')

        except Exception as e:
            QMessageBox.critical(self, 'Error', str(e))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Main_window_nuevo()
    ventana.show()
    sys.exit(app.exec_())
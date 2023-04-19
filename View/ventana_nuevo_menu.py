import sys
import os
from datetime import datetime, date
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
# import webbrowser
# import pdfrw

# QComboBox

Ui_MainWindow, QMainWindow = loadUiType('nuevo_menu.ui')

class Main_window_nuevo(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        self.modelo_principal = ModeloPrincipal()
        self.modelo_proveedor = ModeloProveedor()
        self.modelo_cliente = ModeloCliente()
        self.modelo_detalle = ModeloDetalle()
        self.registrar_usuario = RegistrarInventario()
        self.listar_venta_tabla = ModeloVenta()
        self.registrar_detalle = RegistarDetalle()
        self.registrar_cliente = RegistarCliente()
        self.cliente_id = self.registrar_cliente.obtener_ultimo_id_cliente()

        self.fecha_actual = datetime.now()
        super().__init__()
        # Conectar interfaz grafica
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ultimo_id = self.registrar_detalle.obtener_ultimo_id()
        print(self.cliente_id)

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
                                                                                          self.ultimo_id))
        self.tabla_cliente_c = self.tabla_cliente
        self.tabla_cliente = self.tabla_cliente
        self.btn_listar_4.clicked.connect(lambda: self.modelo_cliente.listar_cliente(self.tabla_cliente_c))
        self.registrar_cliente.clicked.connect(lambda: self.modelo_cliente.crearcliente(self.nombre_cliente.text(),
                                                                                        self.nit_cliente.text(),
                                                                                        self.celular_cliente.text(),
                                                                                        self.email_cliente.text()))

        # clientes deudas
        self.btn_deudas.clicked.connect(self.page_deudas)

        # Tabla de detalles
        # id_detalle - producto - fecha - entregado - sub_total - total - id_tipo - usuario_id - cliete_id
        # self.btn_finaliza_compra.clicked.connect(self.borrar_line_edit_venta)

        # ------------------------------------------------------------------------------
        #self.calendar = self.calendario_pedido
        #self.calendar.selectionChanged.connect(self.fecha_seleccionada)

        #def fecha_seleccionada(self):
        #    fecha = self.calendar.selectedDate()
        #    print("Fecha seleccionada:", fecha.toString())

        self.calendar = self.calendario_pedido
        self.fecha_date = ""

        def date_selected():
            # Obtiene la fecha seleccionada
            selected_date = self.calendar.selectedDate()
            #day = selected_date.day()
            #month = selected_date.month()
            #year = selected_date.year()
            fecha_final = selected_date.strftime('%Y-%m-%d')
            #fecha_final = f"{year}-{month}-{day}"
            self.fecha_date = datetime.strptime(fecha_final, '%Y-%m-%d').date()

            #print(fecha_date)

        # Conecta la señal clicked() del calendario a la función date_selected
        self.calendar.clicked.connect(date_selected)



        # Obtiene la fecha seleccionada
        #selected_date = calendar.selectedDate()

        # Obtiene el día, mes y año de la fecha seleccionada
        #day = selected_date.day()
        #month = selected_date.month()
        #year = selected_date.year()
        #fecha_final = f"{year}-{month}-{day}"
        # print(type(fecha_final))



        # print("Fecha seleccionada:", fecha_final)
        # print(self.fecha_actual.date())
        #fecha_date = datetime.strptime(fecha_final, '%Y-%m-%d').date()
        # print(fecha_date)


        #fecha_str = '2022-04-18'
        #fecha_obj = datetime.strptime(fecha_str, '%Y-%m-%d')
        #print(type(fecha_obj))  # <class 'datetime.datetime'>
        #print(fecha_obj)  # 2022-04-18 00:00:00

        self.btn_pedido.clicked.connect(lambda: self.modelo_detalle.creardetalle(
                                                                                        self.fecha_date,
                                                                                        "no",
                                                                                        1,
                                                                                        1,
                                                                                        self.cliente_id))

        self.btn_agregar_venta.clicked.connect(lambda: self.modelo_detalle.creardetalle(
                                                                                        self.fecha_actual.date(),
                                                                                        "si",
                                                                                        1,
                                                                                        1,
                                                                                        self.cliente_id))


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

    def page_deudas(self):
        self.stackedWidget.setCurrentWidget(self.page_cliente_deben)

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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Main_window_nuevo()
    ventana.show()
    sys.exit(app.exec_())
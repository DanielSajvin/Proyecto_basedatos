from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from controladores.venta_registe import RegistrarVenta

class ModeloVenta():
    def __int__(self):
        self.venta = RegistrarVenta()

    def listar_venta(self, tabla):
        self.venta = RegistrarVenta()
        table = tabla

        venta = self.venta.\
            obtener_venta()
        table.setRowCount(0)
        for row_number, row_data in enumerate(venta):
            table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def listar_venta_transitorio(self, tabla):
        self.venta = RegistrarVenta()
        table = tabla

        venta = self.venta.\
            obtener_venta_transitoria()

        table.setRowCount(0)
        for row_number, row_data in enumerate(venta):
            table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def modificar_anticipo(self, codigo, modificar):
        self.venta = RegistrarVenta()
        product = self.venta.get_codigo(codigo)
        producto_acutal = product[5]

        nuevo_producto = producto_acutal + modificar
        self.venta.modificar_venta(codigo, nuevo_producto)

    def crearventa(self, producto, cantidad, precio_unitario, sub_total, anticipo, total, detalle_id):

        self.venta = RegistrarVenta()
        self.venta.insertarVenta(producto, cantidad, precio_unitario, sub_total, anticipo, total, detalle_id)


    def limpiar_tabla_venta(self, table):
        self.producto = RegistrarVenta()
        table = table
        if table.currentItem() != None:
            self.producto.limpiar_tabla()
        self.listar_venta(table)

    def eliminar_produc(self, table):
        self.venta = RegistrarVenta()
        table = table
        if table.currentItem() != None:
            cod = table.currentItem().text()

            product = self.venta.get_codigo_transitoria(cod)
            if product:
                self.venta.eliminarventa(cod)
        self.listar_venta_transitorio(table)

    def transicion_vt_a_v(self, id_detalle, id_ventas_tansitoria, codigos, productos, cantidades, precios, sub_totales,
                          anticipos, totales):
        self.venta = RegistrarVenta()

        self.venta.insertarVenta(productos, cantidades, precios, sub_totales, anticipos, totales, id_detalle)

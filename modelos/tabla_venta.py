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

    def crearventa(self, producto, cantidad, precio_unitario, sub_total, anticipo, total, detalle_id):

        self.venta = RegistrarVenta()
        if producto and cantidad and precio_unitario and sub_total and anticipo and total and detalle_id:
            self.venta.insertarVenta(producto, cantidad, precio_unitario, sub_total, anticipo, total, detalle_id)

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from controladores.pedido_controller import MostrarPedido

class ModeloPedido():
    def __int__(self):
        self.pedido = MostrarPedido()

    def listar_pedido(self, tabla):
        self.pedido = MostrarPedido()
        table = tabla

        venta = self.pedido.\
            obtener_pedido()
        table.setRowCount(0)
        for row_number, row_data in enumerate(venta):
            table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
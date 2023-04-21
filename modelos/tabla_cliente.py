from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from controladores.cliente_register import RegistarCliente

class ModeloCliente():
    def __int__(self):
        self.cliente = RegistarCliente()

    def listar_cliente(self, tabla):
        self.cliente = RegistarCliente()
        table = tabla
        clientes = self.cliente.\
            obtener_cliente()
        table.setRowCount(0)
        for row_number, row_data in enumerate(clientes):
            table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def crearcliente(self, nombre, nit, celular, email):
        self.cliente = RegistarCliente()
        if nombre and nit and celular and email:
            print("mandando datos")
            self.cliente.insertarCliente(nombre, nit, celular, email)

    def eliminar_produc(self, table):
        self.cliente = RegistarCliente()
        table = table
        if table.currentItem() != None:
            cod = table.currentItem().text()
            print(cod)
            product = self.cliente.getcliente(cod)
            print(product)
            if product:
                self.cliente.eliminarcliente(cod)
        self.listar_cliente(table)

    def obtener_deben(self, tabla):
        self.cliente = RegistarCliente()
        table = tabla
        clientes = self.cliente.\
            clientes_deben()
        table.setRowCount(0)
        print(f"esto hay en cliente: {clientes}")
        if clientes == None:
            print("no existen deudores")
        else:
            for row_number, row_data in enumerate(clientes):
                table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))


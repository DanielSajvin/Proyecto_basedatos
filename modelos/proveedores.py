from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from controladores.ProveedorController import RegistrarProveedor

class ModeloProveedor():
    def __init__(self):
        self.proveedor = RegistrarProveedor()

    def listar_proveedor(self, tabla):
        self.proveedor = RegistrarProveedor()
        table = tabla
        proveedores = self.proveedor.\
            obtener_proveedor()
        table.setRowCount(0)
        for row_number, row_data in enumerate(proveedores):
            table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def crearProovedor(self, nombre, producto, cantidad, total):
        self.proveedor = RegistrarProveedor()
        if nombre and producto and cantidad and total:
            print("mandando datos")
            self.proveedor.insertarProveedor(nombre, producto, cantidad, total)
    def eliminar_prov(self, table):
        self.proveedor = RegistrarProveedor()
        table = table
        if table.currentItem() != None:
            cod = table.currentItem().text()
            prov = self.proveedor.getProveedor(cod)
            if prov:
                self.proveedor.eliminarproveedor(cod)
        self.listar_proveedor(table)



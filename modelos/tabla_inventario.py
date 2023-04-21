from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from server.conexion_sqlserver import conecciones
from controladores.Register import RegistrarInventario


class ModeloPrincipal():
    def __int__(self, principal):
        self.producto = RegistrarInventario()
        self.principal = principal

    def modificar_existencias(self, codigo, modificar: int):
        self.producto = RegistrarInventario()
        product = self.producto.get_codigo(codigo)
        producto_acutal: int = product[3]

        nuevo_producto: int = producto_acutal - modificar
        self.producto.modificar_inventario(codigo, nuevo_producto)

    def listar_productos(self, tabla):
        self.producto = RegistrarInventario()
        table = tabla
        productos = self.producto.\
            obtener_producto()
        table.setRowCount(0)
        for row_number, row_data in enumerate(productos):
            table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def mostrar_producto(self, tabla):
        self.producto = RegistrarInventario()
        table = tabla
        if table.currentItem() != None:
            cod = table.currentItem().text()
            product = self.producto.getProduct(cod)
            if product:
                msg = QMessageBox()
                msg.setWindowTitle(product[1])
                msg.setText(product[1])

                msg.setIcon(QMessageBox.Information)

                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText(
                    f"ID: {product[0]} \nCodigo: {product[1]} \nProducto: {product[2]}"
                    f" \nExistencia {product[3]} \nPrecio Minorista {product[4]}"
                    f" \nPrecio Mayorista {product[5]}")

                x = msg.exec_()


    def subir_productos(self, tabla):
        self.producto = RegistrarInventario()
        table = tabla
        products = []
        fila = []
        for row_number in range(table.rowCount()):
            for column_number in range(table.columnCount()):
                if table.item(row_number, column_number) != None:
                    fila.append(table.item(row_number, column_number).text())
            if len(fila) > 0:
                products.append(fila)
            fila = []

        if len(products) > 0:
            for prod in products:
                self.producto.subirproducto(prod[0], prod[1], prod[2], prod[3], prod[4], prod[5])

        self.listar_productos(tabla)

    def eliminar_produc(self, table):
        self.producto = RegistrarInventario()
        table = table
        if table.currentItem() != None:
            cod = table.currentItem().text()
            product = self.producto.getProduct(cod)
            if product:
                self.producto.eliminarproducto(cod)
        self.listar_productos(table)

    def crearProducto(self, codigo, producto, existencia, precio_min, precio_may):
        self.producto = RegistrarInventario()
        if codigo and producto and existencia and precio_min and precio_may:
            print("mandando datos")
            self.producto.insertarProducto(codigo, producto, existencia, precio_min, precio_may)

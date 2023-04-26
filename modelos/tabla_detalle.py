from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from controladores.detalle_register import RegistarDetalle

class ModeloDetalle():
    def __int__(self):
        self.detalle = RegistarDetalle()

    def creardetalle(self, fecha, entregado, tipo_id, usuario_id, cliente_id):
        self.detalle = RegistarDetalle()
        if fecha and entregado and tipo_id and usuario_id and cliente_id:
            self.detalle.insertarDetalle(fecha, entregado, tipo_id, usuario_id, cliente_id)

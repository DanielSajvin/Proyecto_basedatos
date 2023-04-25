import sys
import os
from server.conexion_sqlserver import conecciones


class MostrarPedido:
    def __int__(self):
        self.conn = conecciones()

    def obtener_pedido(self):
        self.conn = conecciones()
        with self.conn.cursor() as cursor:
            sql = """SELECT c.id_cliente AS "No. Cliente", c.Nombre AS "Nombre Cliente", c.celular AS "No. Celular", d.fecha AS "Fecha Entrega", d.entregado FROM proyecto.cliente c
	                    LEFT JOIN detalle d 
		                ON c.id_cliente = d.Cliente_id_cliente WHERE d.entregado = 'no'"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

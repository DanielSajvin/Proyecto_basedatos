from server.conexion_sqlserver import conecciones

class RegistrarVenta:
    def __int__(self):
        self.conn = conecciones()

    def obtener_id(self):
        self.conn = conecciones()
        cursor = self.conn.cursor()
        cursor.execute("SELECT MAX(id_venta) FROM venta")

        count = cursor.fetchone()[0]
        count = count + 1
        return count

    def obtener_venta(self):
        self.conn = conecciones()
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM venta"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    def insertarVenta(self, producto, cantidad, precio_unitario, sub_total, anticipo, total, detalle_id):
        self.conn = conecciones()
        id = self.obtener_id()

        with self.conn.cursor() as cursor:
            sql = """INSERT INTO venta (id_venta,producto,cantidad,precio_unitario,sub_total, anticipo, total, detalle_id_detalle)
             VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql, (id, producto, cantidad, precio_unitario, sub_total, anticipo, total, detalle_id))
            self.conn.commit()

from server.conexion_sqlserver import conecciones

class RegistrarProveedor:
    def __int__(self):
        self.conn = conecciones()

    def obtener_proveedor(self):
        self.conn = conecciones()
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM proveedor"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    def insertarProveedor(self, nombre, producto, cantidad, total):
        self.conn = conecciones()
        id = self.obtener_id()

        with self.conn.cursor() as cursor:
            sql = """INSERT INTO proveedor (id_provedor,nombre,producto,cantidad,total) VALUES (%s,%s,%s,%s,%s)"""
            cursor.execute(sql, (id, nombre, producto, cantidad, total))
            self.conn.commit()

    def obtener_id(self):
        self.conn = conecciones()
        cursor = self.conn.cursor()
        cursor.execute("SELECT MAX(id_provedor) FROM proveedor")

        count = cursor.fetchone()[0]
        count = count + 1
        return count

    def getProveedor(self, cod):
        self.conn = conecciones()
        with self.conn.cursor() as cursor:
            sql = "SELECT * FROM proveedor WHERE id_provedor = '"+cod+"'"
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                return result

    def eliminarproveedor(self, id):
        self.conn = conecciones()
        with self.conn.cursor() as cursor:
            sql = "DELETE FROM `proyecto`.`proveedor` WHERE id_provedor = '"+id+"'"
            cursor.execute(sql)
            self.conn.commit()

    def obtener_id_transitoria(self):
        self.conn = conecciones()
        cursor = self.conn.cursor()
        cursor.execute("SELECT MAX(id_venta) FROM venta_transitoria")

        count = cursor.fetchone()[0]
        if count is None:
            count = 1
        else:
            count = count + 1

        return count

    def insertar_transitoria(self, codigo, producto, cantidad, precio, sub_total, anticipo, total):
        self.conn = conecciones()
        id = self.obtener_id_transitoria()

        with self.conn.cursor() as cursor:
            sql = """INSERT INTO venta_transitoria (id_venta,codigo,producto,cantidad,precio,sub_total,anticipo,total)
             VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql, (id, codigo, producto, cantidad, precio, sub_total, anticipo, total))
            self.conn.commit()

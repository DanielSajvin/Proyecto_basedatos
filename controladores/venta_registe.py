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
            sql = """INSERT INTO `proyecto`.`venta` (`id_venta`, `producto`, `cantidad`, `precio_unitario`, `sub_total`, `anticipo`, `total`, `detalle_id_detalle`)
             VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""

            try:
                cursor.execute(sql, (id, producto, cantidad, precio_unitario, sub_total, anticipo, total, detalle_id))
                self.conn.commit()
            except Exception as e:
                print(f"Error al insertar venta: {e}")

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

    def escribir_base_datos_transitoria(self, codigo, producto, cantidad, precio, anticipo, total):
        self.conn = conecciones()
        id = self.obtener_id_transitoria()
        with self.conn.cursor() as cursor:
            sql = """INSERT INTO `proyecto`.`venta_transitoria` (`id_venta`, `codigo`, `producto`, `cantidad`, `precio`, `anticipo`, `total`)
            VALUES (%s, %s, %s, %s, %s, %s, %s)"""  # Corregir comillas simples a comillas invertidas
            try:
                cursor.execute(sql, (id, codigo, producto, cantidad, precio, anticipo, total))
                self.conn.commit()
            except Exception as e:
                print(f"Error al insertar venta: {e}")


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

    def get_codigo(self, cod):
        self.conn = conecciones()
        with self.conn.cursor() as cursor:
            sql = "SELECT * FROM venta WHERE id_venta = '"+cod+"'"
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                return result

    def get_venta_producto(self, producto):
        self.conn = conecciones()
        with self.conn.cursor() as cursor:
            sql = "SELECT * FROM venta_transitoria WHERE producto = '"+producto+"'"
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                return result

    def obtener_venta(self):
        self.conn = conecciones()
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM venta"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    def obtener_venta_transitoria(self):
        self.conn = conecciones()
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM venta_transitoria"""
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

    def modificar_venta(self, codigo, anticipo):
        with self.conn.cursor() as cursor:
            sql = """UPDATE venta SET anticipo = %s WHERE id_venta = %s """
            cursor.execute(sql, (anticipo, codigo))
            self.conn.commit()

    def limpiar_tabla(self):
        with self.conn.cursor() as cursor:
            sql = """TRUNCATE TABLE venta_transitoria"""
            cursor.execute(sql)
            self.conn.commit()

    def eliminarventa(self, id):
        self.conn = conecciones()
        with self.conn.cursor() as cursor:
            sql = "DELETE FROM `proyecto`.`venta_transitoria` WHERE id_venta = '"+id+"'"
            cursor.execute(sql)
            self.conn.commit()

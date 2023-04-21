from server.conexion_sqlserver import conecciones

class BaseDatosInfo:
    def __int__(self):
        self.conn = conecciones()

    def obtener_id(self):
        self.conn = conecciones()
        cursor = self.conn.cursor()
        cursor.execute("SELECT MAX(id_venta) FROM venta_transitoria")

        count = cursor.fetchone()[0]
        if count is None:
            count = 1
        else:
            count = count + 1
        return count


    def eliminar_filas_venta(self):
        self.conn = conecciones()
        c = self.conn.cursor()
        c.execute('DELETE  FROM venta ')
        self.conn.commit()


    def base_datos(self, fila, columna):
        self.conn = conecciones()
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM inventario')
        rows = cursor.fetchall()
        return rows[fila][columna]


    def base_ventas(self,fila, columna):
        self.conn = conecciones()
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM venta_transitoria')
        rows = cursor.fetchall()
        return rows[fila][columna]


    def escribir_base_datos(self, producto, cantidad, unidades, precio_und, importe):
        self.conn = conecciones()
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO venta values (\'" + producto + "\',\'" + cantidad + "\',\'" + unidades + "\',\'" + precio_und + "\',\'" + importe + "')")
        self.conn.commit()
        cursor.close()
        self.conn.close()

    def escribir_base_datos_transitoria(self, codigo, producto, cantidad, precio, anticipo, total):
        self.conn = conecciones()
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO venta_transitoria values (\'" + codigo + "\',\'" + producto + "\',\'" + cantidad + "\',\'" + str(precio) + "\',\'" + anticipo + "\',\'" + str(total) + "')")
        self.conn.commit()
        cursor.close()
        self.conn.close()

    def insertarVentaTransitoria(self, producto, cantidad, precio, anticipo, total):
        self.conn = conecciones()
        id = self.obtener_id()
        with self.conn.cursor() as cursor:
            sql = """INSERT INTO `proyecto`.`venta_transitoria` (`id_venta`, `producto`, `cantidad`, `precio`, `anticipo`, `total`)
              VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""

            try:
                cursor.execute(sql, (id, producto, cantidad, precio, anticipo, total))
                self.conn.commit()
            except Exception as e:
                print(f"Error al insertar venta: {e}")
        return f"Se ha insertado en la tabla"


    def lista_ventas(self, vendedor, cliente, tipo_pago, fecha_venta, monto_total):
        self.conn = conecciones()
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO venta_dia values (\'" + vendedor + "\',\'" + cliente + "\',\'" + tipo_pago + "\',\'" + fecha_venta + "\',\'" + monto_total + "')")
        self.conn.commit()
        cursor.close()
        self.conn.close()


    def monto_total(self,catd_elem):
        monto_total_venta = 0
        for valor in range(0, catd_elem):
            monto_total_venta = int(self.base_ventas(valor, 4)) + monto_total_venta
        # print(monto_total_venta)
        # print(monto_total_venta)
        return monto_total_venta


    def elemtos_ventas(self,):
        self.conn = conecciones()
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM venta_transitoria')
        rows = cursor.fetchall()
        catd_elem = len(rows)
        return catd_elem

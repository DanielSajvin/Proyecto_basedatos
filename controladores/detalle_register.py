from server.conexion_sqlserver import conecciones

class RegistarDetalle:
    def __int__(self):
        self.conn = conecciones()

    def obtener_ultimo_id(self):
        self.conn = conecciones()
        cursor = self.conn.cursor()
        cursor.execute("SELECT MAX(id_detalle) FROM detalle")

        count = cursor.fetchone()[0]
        print(count)
        return count

    def obtener_id(self):
        self.conn = conecciones()
        cursor = self.conn.cursor()
        cursor.execute("SELECT MAX(id_detalle) FROM detalle")

        count = cursor.fetchone()[0]
        if count == None:
            count = 1

        else:
            count = count + 1
        return count

    def insertarDetalle(self, fecha, entregado, tipo_id, usuario_id, cliente_id, inventario_id):
        self.conn = conecciones()
        id = self.obtener_id()

        with self.conn.cursor() as cursor:
            sql = """INSERT INTO detalle (id_detalle, fecha,entregado,Tipo_id_tipo, Usuario_id_usuario,
             Cliente_id_cliente, inventario_Id_inventario)
             VALUES (%s,%s,%s,%s,%s,%s,%s)"""

            cursor.execute(sql, (id, fecha, entregado, tipo_id, usuario_id, cliente_id, inventario_id))
            #cursor.execute(sql, (1, "camis", "2023-05-21", "si", 150, 125, 1, 1, 1))
            self.conn.commit()


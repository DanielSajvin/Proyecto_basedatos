from server.conexion_sqlserver import conecciones

class RegistarCliente:
    def __int__(self):
        self.conn = conecciones()

    def obtener_id(self):
        self.conn = conecciones()
        cursor = self.conn.cursor()
        cursor.execute("SELECT MAX(id_cliente) FROM cliente")

        count = cursor.fetchone()[0]
        count = count + 1
        return count

    def obtener_ultimo_id_cliente(self):
        self.conn = conecciones()
        cursor = self.conn.cursor()
        cursor.execute("SELECT MAX(id_cliente) FROM cliente")

        count = cursor.fetchone()[0]

        return count

    def obtener_cliente(self):
        self.conn = conecciones()
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM cliente"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    def insertarCliente(self, nombre, nit, celular, email):
        self.conn = conecciones()
        id = self.obtener_id()

        with self.conn.cursor() as cursor:
            sql = """INSERT INTO cliente (id_cliente,nombre,nit,celular,email) VALUES (%s,%s,%s,%s,%s)"""
            cursor.execute(sql, (id, nombre, nit, celular, email))
            self.conn.commit()

    def getcliente(self, cod):
        self.conn = conecciones()
        with self.conn.cursor() as cursor:
            sql = "SELECT * FROM cliente WHERE id_cliente = '"+cod+"'"
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                return result

    def eliminarcliente(self, id):
        self.conn = conecciones()
        with self.conn.cursor() as cursor:
            sql = "DELETE FROM `proyecto`.`cliente` WHERE id_cliente = '"+id+"'"
            cursor.execute(sql)
            self.conn.commit()

    def clientes_deben(self):
        self.conn = conecciones()
        self.no = "no"
        with self.conn.cursor() as cursor:
            sql = "SELECT v.id_venta, c.nombre, c.email, c.celular, d.fecha, v.sub_total, (v.sub_total - v.anticipo) AS diferencia" \
                  " FROM proyecto.cliente c left join detalle d on c.id_cliente = d.Cliente_id_cliente " \
                  "left join venta v on d.id_detalle = v.detalle_id_detalle where d.entregado = '"+self.no+"' and v.anticipo != v.total "

            cursor.execute(sql)
            result = cursor.fetchall()
            if result:
                return result



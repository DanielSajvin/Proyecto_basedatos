from server.conexion_sqlserver import conecciones

class RegistarCliente:
    def __int__(self):
        self.conn = conecciones()

    def obtener_id(self):
        self.conn = conecciones()
        cursor = self.conn.cursor()
        cursor.execute("SELECT MAX(id_cliente) FROM cliente")

        count = cursor.fetchone()[0]
        if count == None:
            count = 1

        else:
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
        num = 1
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM cliente where activo = 1"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    def insertarCliente(self, nombre, nit, celular, email, activo):
        self.conn = conecciones()
        id = self.obtener_id()

        with self.conn.cursor() as cursor:
            sql = """INSERT INTO cliente (id_cliente,nombre,nit,celular,email, activo) VALUES (%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql, (id, nombre, nit, celular, email, activo))
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

    def clientes_nombre(self):
        self.conn = conecciones()
        with self.conn.cursor() as cursor:
            sql = "SELECT c.nombre FROM proyecto.cliente c;"


            cursor.execute(sql)
            result = cursor.fetchall()
            if result:
                return result

    def get_c_nombre(self, nombre):
        self.conn = conecciones()
        with self.conn.cursor() as cursor:
            sql = "SELECT c.id_cliente FROM cliente c WHERE nombre = '"+nombre+"'"
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                return result

    def deshabilitar_clientes(self, id):
        self.conn = conecciones()
        numero = 0
        with self.conn.cursor() as cursor:
            sql = """UPDATE cliente SET activo = %s WHERE id_cliente = %s """
            cursor.execute(sql, (numero, id))
            self.conn.commit()



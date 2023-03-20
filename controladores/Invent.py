from server.conexion_sqlserver import conecciones

class Reistrar_invent:
    def __int__(self):
        self.conn = conecciones()


    def obtener_producto(self):
        self.conn = conecciones()
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM inventario"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    def getProduct(self, cod):
        self.conn = conecciones()
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM inventario WHERE codigo_producto = %s"""
            cursor.execute(sql, cod)
            result = cursor.fetchone()
            if result:
                return result

    def updateProduct(self, Codigo, Describcion, Cantidad, Existencia, Costo, Publico):
        self.conn = conecciones()
        with self.conn.cursor() as cursor:
            sql = """UPDATE inventario SET codigo_producto = %s, producto = %s, existencia = %s,
            precio_minorista = %s, precio_mayorista = %s WHERE Codigo = %s """
            cursor.execute(sql, (Describcion, Cantidad, Existencia, Costo, Publico, Codigo))
            self.conn.commit()

    def updateProduct(self, puesto, nombre, apellido, usuario, password):
        self.conn = conecciones()
        with self.conn.cursor() as cursor:
            sql = """UPDATE usuario SET cargo = %s, nombre = %s, apellido = %s,
            usuario = %s, password = %s WHERE codigo = %s """
            cursor.execute(sql, (puesto, nombre, apellido, usuario, password))
            self.conn.commit()

    def eliminar_producto(self, cod):
        with self.conn.cursor() as cursor:
            sql = """DELETE FROM inventario WHERE Codigo = %s"""
            cursor.execute(sql, cod)
            self.conn.commit()

    def eliminar_usuario(self, cod):
        with self.conn.cursor() as cursor:
            sql = """DELETE FROM usuario WHERE codigo = %s"""
            cursor.execute(sql, cod)
            self.conn.commit()

    def insertProduct(self, id, codigo, prodycto, existencia, precio_min, precio_may):
        print("datos recibidos")
        with self.conn.cursor() as cursor:
            sql = """INSERT INTO inventario (Id_invetario,codigo_producto,producto,existencia,precio_minorista,precio_mayorista)
             VALUES (%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql, (id, codigo, prodycto, existencia, precio_min, precio_may))
            self.conn.commit()

    def modificar_inventario(self, codigo, numero):
        with self.conn.cursor() as cursor:
            sql = """UPDATE inventario SET Existencias = %s WHERE Codigo = %s """
            cursor.execute(sql, (numero, codigo))
            self.conn.commit()

    # Para obtener proveedores
    def getProveedor(self):
        sql = """SELECT * FROM provedor"""
        cursor.execute(sql)
        result = cursor.fetchall()
        return result



    def Insertar(self, n_1, n_2, us, pw):
        with self.conn.cursor() as cursor:
            sql = """INSERT INTO usuario (id_usuario,cargo,nombre,apellido,usuario,password) VALUES (%s,%s,%s,%s,%s)"""

            cursor.execute(sql, (id, n_1, n_2, us, pw))
            self.conn.commit()

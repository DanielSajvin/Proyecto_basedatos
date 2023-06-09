import sys
import os
from server.conexion_sqlserver import conecciones

class RegistrarInventario:
    def __int__(self):
        self.conn = conecciones()


    def obtener_cargo(self):
        self.conn = conecciones()
        cursor = self.conn.cursor()
        sql = "SELECT cargo FROM usuario"
        cursor.execute(sql)
        resultados = []
        for cargo in cursor:
            resultados.append(cargo[0])
        return resultados

    def obtener_nombre(self):
        self.conn = conecciones()
        cursor = self.conn.cursor()
        sql = "SELECT nombre FROM usuario"
        cursor.execute(sql)
        resultados = []
        for cargo in cursor:
            resultados.append(cargo[0])
        return resultados

    def obtener_apellido(self):
        self.conn = conecciones()
        cursor = self.conn.cursor()
        sql = "SELECT apellido FROM usuario"
        cursor.execute(sql)
        resultados = []
        for cargo in cursor:
            resultados.append(cargo[0])
        return resultados

    def obtener_usuario(self):
        self.conn = conecciones()
        cursor = self.conn.cursor()
        sql = "SELECT usuario FROM usuario"
        cursor.execute(sql)
        resultados = []
        for cargo in cursor:
            resultados.append(cargo[0])
        return resultados

    def getUsuario(self, cod):
        self.conn = conecciones()
        with self.conn.cursor() as cursor:
            sql = "SELECT * FROM usuario WHERE id_usuario = '"+cod+"'"
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                return result

    def getUsusario_user(self, usario): #obtener los datos de ususario por su nombre de usuario
        self.conn = conecciones()
        with self.conn.cursor() as cursor:
            sql = "SELECT * FROM usuario WHERE usuario = '"+usario+"'"
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                return result

    def obtener_key(self):
        self.conn = conecciones()
        cursor = self.conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM usuario")

        count = cursor.fetchone()[0]
        count = count + 1
        return count

    def obtener_id_inventario(self):
        self.conn = conecciones()
        cursor = self.conn.cursor()
        cursor.execute("SELECT MAX(Id_inventario) FROM inventario")

        count = cursor.fetchone()[0]
        if count == None:
            count = 1

        else:
            count = count + 1
        return count




    def obtener_id(self):
        self.conn = conecciones()
        cursor = self.conn.cursor()
        cursor.execute("SELECT MAX(id_usuario) FROM usuario")

        count = cursor.fetchone()[0]
        if count == None:
            count = 1
        else:
            count = count + 1
        return count

    def Insertar(self, cargo, n_1, n_2, us, pw):
        self.conn = conecciones()
        id = self.obtener_id()

        with self.conn.cursor() as cursor:
            sql = """INSERT INTO usuario (id_usuario,cargo,nombre,apellido,usuario,password) VALUES (%s,%s,%s,%s,%s,%s)"""

            cursor.execute(sql, (id, cargo, n_1, n_2, us, pw))

            self.conn.commit()

    def obtener_producto(self):
        self.conn = conecciones()
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM inventario"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    def get_codigo(self, cod):
        self.conn = conecciones()
        with self.conn.cursor() as cursor:
            sql = "SELECT * FROM inventario WHERE codigo_producto = '"+cod+"'"
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                return result

    def get_code_by_product(self, product):
        self.conn = conecciones()
        with self.conn.cursor() as cursor:
            sql = "SELECT Id_inventario FROM inventario WHERE producto = '"+product+"'"
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                return result

    def delete_tabla(self):
        self.conn = conecciones()
        with self.conn.cursor() as cursor:
            sql = "DELETE FROM `proyecto`.`venta_transitoria`"
            cursor.execute(sql)
            self.conn.commit()

    def getProduct(self, cod):
        self.conn = conecciones()
        with self.conn.cursor() as cursor:
            sql = "SELECT * FROM inventario WHERE Id_inventario = " + str(cod)
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                return result


    def obtener_por_codigo(self, cod):
        self.conn = conecciones()
        with self.conn.cursor() as cursor:
            sql = "SELECT * FROM inventario WHERE codigo_producto = '"+cod+"'"
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                return result

    def subirproducto(self, Id, codigo, producto, Existencia, precio_min, precio_may):
        self.conn = conecciones()
        with self.conn.cursor() as cursor:
            sql = """UPDATE inventario SET codigo_producto = %s, producto = %s, existencia = %s,
            precio_minorista = %s, precio_mayorista = %s WHERE Id_inventario = %s """
            cursor.execute(sql, (codigo, producto, Existencia, precio_min, precio_may, Id))
            self.conn.commit()


    def eliminarproducto(self, id):
        self.conn = conecciones()
        with self.conn.cursor() as cursor:
            sql = "DELETE FROM `proyecto`.`inventario` WHERE Id_inventario = '"+id+"'"
            cursor.execute(sql)
            self.conn.commit()

    def insertarProducto(self, codigo, producto, existencia, precio_min, precio_may):
        self.conn = conecciones()
        id = self.obtener_id_inventario()

        with self.conn.cursor() as cursor:
            sql = """INSERT INTO inventario (Id_inventario,codigo_producto,producto,existencia,precio_minorista,precio_mayorista) VALUES (%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql, (id, codigo, producto, existencia, precio_min, precio_may))
            self.conn.commit()


    def modificar_inventario(self, codigo, numero):
        with self.conn.cursor() as cursor:
            sql = """UPDATE inventario SET existencia = %s WHERE codigo_producto = %s """
            cursor.execute(sql, (numero, codigo))
            self.conn.commit()

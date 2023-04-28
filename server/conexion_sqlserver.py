import mysql.connector

# Establecemos Coneccion con nuestro host
# Conn empieza la coneccion
''


def conecciones():
    #db = mysql.connector.connect(host="localhost", user="root", password="admin123", db="proyecto", port=3306)
    #db = mysql.connector.connect(host="localhost", user="root", password="dieguito1211", db="proyecto", port=3306)
    db = mysql.connector.connect(host="192.168.170.249", user="usuario  ", password="url.2023", db="proyecto", port=3306)

    return db


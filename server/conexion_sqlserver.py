import mysql.connector


# Establecemos Coneccion con nuestro host
# Conn empieza la coneccion
''
def conecciones():
    print("Conectando....")

    db = mysql.connector.connect(host="localhost", user="root", password="admin123", db="proyecto", port=3306)

    print('Database is Connected!')
    return db




import mysql.connector
from mysql.connector import errorcode
import sys


### Conexión a la base de datos ======================================================
def define():
    return mysql.connector.connect(
        user='root',
        password='tu contraseña',
        host='tu dirección host',
        port='3306',
        database='Conferencia'
    )


### probar la conexión de la base =============================================
def connect():
    try:
       cnx =  define()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Credenciales incorrectas", file=sys.stderr)
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("No existe la base de datos", file=sys.stderr)
        else:
            print(err, file=sys.stderr)
        return False
    else:
        cnx.close()
        return True
from dbestudiante import dbestudiante
from mysql.connector import Error

## Obtener todos los estudiantes actuales
def obtenerEstudiantes():
    # crear conexión con la base de datos
    cnx = dbestudiante.define()
    cursor = cnx.cursor() # objeto que ejecuta la consulta

    # consulta en lenguaje SQL
    query = (
        "select * from Estudiante"
    )

    try:
        # ejecutar la consulta
        cursor.execute(query)
        rows = cursor.fetchall() # obtener respuesta de la consulta
        
        # cerrar conexión para reducir la carga de sesiones en la base  de datos
        cursor.close()
        cnx.close()

        # dar formato a la data
        data =[]
        for row in rows:
           dato={
               'carnet':row[0],
               'nombre':row[1]
            } 
           data.append(dato)

        return {'msg': data, 'code':200} 
    except Error as err:
        print(err)
        return {'msg':"{}".format(err),'code':500}


# Insertar un usuario en la base de datos
def insertarEstudiante(body):
    # crear conexión con la base de datos
    cnx = dbestudiante.define()
    cursor = cnx.cursor() # objeto que ejecuta la consulta

    # consulta en lenguaje SQL
    query = (
        "insert into Estudiante values (%(carnet)s, %(nombre)s)"
    )

    try:
        # ejecuta la consulta|sentencia
        cursor.execute(query, body)
        # guarda cambios en la base de datos
        cnx.commit() # si no se realiza éste paso, no se guardan los datos y bloqueamos la base
        cursor.close()
        cnx.close()

        return {'msg':'Estudiante registrado', 'code':201}
    except Error as err:
        print(err)
        return {'msg':"{}".format(err),'code':500}


# Eliminar un usuario en la base de datos
def eliminarEstudiante(body):
    # crear conexión con la base de datos
    cnx = dbestudiante.define()
    cursor = cnx.cursor() # objeto que ejecuta la consulta

    # consulta en lenguaje SQL
    query = (
        "delete from Estudiante where carnet = %(carnet)s"
    )

    try:
        # ejecuta la consulta|sentencia
        cursor.execute(query, body)
        # guarda cambios en la base de datos
        cnx.commit() # si no se realiza éste paso, no se guardan los datos y bloqueamos la base
        cursor.close()
        cnx.close()

        return {'msg':'Estudiante eliminado', 'code':201}
    except Error as err:
        print(err)
        return {'msg':"{}".format(err),'code':500}
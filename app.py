import mysql.connector
print('Iniciando')
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='blog',
    port=3306
)
def crearUsuario(nombre,email,contrasenna):
    cursor=db.cursor()
    cursor.execute('''
        insert into usuarios(nombre,email,contrasena)
        values (%s,%s,%s)''',
        (nombre,
        email,
        contrasenna))

    # Creacion, Modificacion, eliminacion de datos
    db.commit()

    #cerrar cursor
    cursor.close()
crearUsuario('fernando','yob@gmail.com','12212121')

cursor =db.cursor()

cursor.execute('select *from usuarios')
usuarios = cursor.fetchall() 
print(usuarios)

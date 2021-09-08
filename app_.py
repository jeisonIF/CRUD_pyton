'''
pip install colorama

'''
import mysql.connector
from colorama import init, Fore
import os
opcion = 1
newUser = {}
menu = '''      
Manipulacion de usuarios        
        Muenu
        1. Crear usuario
        2. Leer usuarios
        3. Actualizar un usuario por identificador
        4. Eliminar un usuario por identificador
        5. Salir
'''
grupo = '''
Grupo:
    Eduardo plata
    Jeison Mavisoy
'''
usuarios = ''
db = mysql.connector.connect(
    host='localhost',
    user='jeison',
    password='sele',
    database='crud_usuarios',
    port=3306
    )

#_______________________________________________________
def ingresoValidar(info):
                
    dato =""
    bandera = 1
                
    while bandera!=0:
        dato = input('Ingrese '+info+': ')
        if not dato:
            print("Porfavor ingrese")        
        else:
            print("Se registro "+info)
            return dato

#_______________________________________________________
def crearUsuario(usuario):
    #print(usuario)
    #dato = ['mama','meme','mimi']
    cursor=db.cursor()
    cursor.execute('''
        insert into usuarios(nombre,email,contrasena)
        values (%s,%s,%s)''',
        (usuario['nombre'],
        usuario['email'],
        usuario['contrasena']))
    ''' cursor.execute('        insert into usuarios(nombre,email,contrasena)        values (%s,%s,%s)',        (dato)) '''
    db.commit()
    cursor.close()

#_______________________________________________________
def listarUsuarios():
    usuarios = []
    cursor=db.cursor()
    cursor.execute('''
        SELECT * FROM usuarios;''')
    usuarios =cursor.fetchall()
    db.commit()
    cursor.close()
    
    print (format('Usuarios Registrados',"^58"))        
    print ("{:<5} {:<10} {:<30} {:<10}".format('ID','Nombre','Email','Contraseña'))
    for usuario in usuarios:
        print ("{:<5} {:<10} {:<30} {:<10}".format(usuario[0],usuario[1],usuario[2],usuario[3]))  
             
#_______________________________________________________
def listarUsuariosUnico(ID,consulta):
    #___________________________________________________
    def mostrar(usuario):
        print ("{:<5} {:<10} {:<30} {:<10}".format('ID','Nombre','Email','Contraseña'))
        print ("{:<5} {:<10} {:<30} {:<10}".format(usuario['id'],usuario['nombre'],usuario['email'],usuario['contrasena']))
        
    #___________________________________________________
    def eliminar(usuario):
            cursor=db.cursor()
            cursor.execute('''
                        DELETE	FROM usuarios WHERE id_usuarios='''+str(usuario['id'])+''';''')
            usuarios =cursor.fetchall()
            db.commit()
            cursor.close()
            os.system ("cls")
            
            print (format('Usuario Eliminado',"^48"))        
            mostrar(usuario)
            
    #___________________________________________________
    def updateuser(usuario):
        sentencia = []
        values = []
        infoUser ={
                'nombre' : '',
                'email' : '',
                'contrasena' : ''
                }
        nombre = ''
        email = ''
        password = ''
        opc = 0
        menu = '''
                    Menu de opciones
                1.      Nombre
                2.      Email
                3.      Contraseña
                4.      Salir
                '''
        
        while opc!=4:
                
                try:
                        opc = int(input(menu + ' Que desea editar:  '))
                except ValueError:
                        print('intente nuevamente\nSe retornara a menu principal')
                else:
                        if opc == 1:
                                nombre = input('Ingrese nombre: ')
                                if (usuario['nombre']).lower()!=nombre.lower() and nombre.lower() !='' :
                                    sentencia.append("nombre = '"+nombre+"'")
                        elif opc == 2:
                                email = input('Ingrese Email: ')
                                if (usuario['email']).lower()!=email.lower() and email.lower() !='' :
                                    sentencia.append("email = '"+email+"'")
                        elif opc == 3:
                                password = input('Ingrese Contraseña: ')
                                if (usuario['contrasena']).lower()!=password.lower() and password.lower() !='' :
                                    sentencia.append("contrasena = '"+password+"'")
                        elif opc == 4:
                                print('Vlidando informacion!!')
                            
                                break
        if len(sentencia) >0:
            print(usuario['id'])
            cursor=db.cursor()
            
            cursor.execute('''UPDATE usuarios SET '''+",".join(sentencia)+''' WHERE id_usuarios= '''+str(usuario['id']))
            cursor.execute('''SELECT * FROM usuarios WHERE id_usuarios ='''+str(usuario['id'])+''';''')
            
            user =cursor.fetchall()
            infoUser ={
                'id':user[0][0],
                'nombre' : user[0][1],
                'email' : user[0][2],
                'contrasena' : user[0][3]
                }
            db.commit()
            cursor.close()
            
            os.system('cls')
            print (format('Informacion de Usuario',"^58"))
            mostrar(usuario)
            print (format('Informacion  nueva delUsuario',"^58"))
            mostrar(infoUser)
        else:
            print('Se actualizo el usuario correctamente')
    #______________________________________-    
         
        
    usuarios = []
    cursor=db.cursor()
    cursor.execute('''SELECT * FROM usuarios WHERE id_usuarios ='''+str(ID)+''';''')
    usuarios =cursor.fetchall()
    db.commit()
    cursor.close()
    
    
    if len(usuarios)>0:
        infoUser ={
                'id':usuarios[0][0],
                'nombre' : usuarios[0][1],
                'email' : usuarios[0][2],
                'contrasena' : usuarios[0][3]
                }
        if consulta =='update':
            print (format('Informacion de Usuario',"^58"))
            mostrar(infoUser)
            updateuser(infoUser)    
                    
        else:
                eliminar(infoUser)
                
    else:
        print(Fore.RED +'No se encontro registro\nIntente Nuevamente', end="!!"+Fore.RESET)
        
    

#_______________________________________________________
while opcion !=5:
        print(menu)
        try:
                opcion = int(input('Seleccione: '))
                os.system ("cls")
                
        except ValueError:
                print(Fore.RED +'Seleccione una opcion valida', end="!!"+Fore.RESET)
        else:
                
                if  opcion> 0 and opcion < 6:
                        if opcion == 1:
                                print('Ingreso de usuarios')
                                newUser ={
                                    'nombre' : ingresoValidar('nombre'),
                                    'email' : ingresoValidar('email'),
                                    'contrasena' : ingresoValidar('contrasena')
                                }
                                crearUsuario(newUser)
                                
                        elif opcion == 2:
                                listarUsuarios()
                               
                        elif opcion == 3:
                                #editar usuario
                                try:
                                    update = int(input('Ingrese id de usuario a Actualizar: '))

                                except ValueError:
                                    print(Fore.RED +'Ingrese un Id valido', end="!!"+Fore.RESET+'\n')
                                else:
                                    listarUsuariosUnico(update,'update')
                                
                        elif opcion == 4:
                                #print('Eliminar usuarios')
                                
                                try:
                                    delete = int(input('Ingrese id de usuario a Eliminar: '))
                                except ValueError:
                                    print(Fore.RED +'Ingrese un Id valido', end="!!"+Fore.RESET+'\n')
                                else:
                                    listarUsuariosUnico(delete,'delete')

                        elif opcion == 5:
                                print('Fin de la ejecucion')
                                os.system ("cls") 
                                print(grupo)
                                break
                else:
                        print(Fore.RED +'Seleccione una opcion valida', end="!!"+Fore.RESET)
                        os.system ("cls") 
                        

opc = 0
menu = '''
            Menu de opciones
        1.      Nombre
        2.       Email
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
                        print('Editando nombre')
                elif opc == 2:
                        print('Editando email')
                elif opc == 3:
                        print('Editando contraseña')
                elif opc == 4:
                        print('salir')
                        break
        




''' from colorama import init, Fore

init()
print(Fore.RED+"Texto color rojo")

print(Style.RESET_ALL + "Texto con valores por defecto")
print(Fore.WHITE+Back.BLUE+"Texto blanco sobre azul"+Back.RESET)
print("Texto blanco sobre fondo negro")
ID ='222' '''
print('''
        SELECT * FROM usuarios WHERE id_usuarios = ?;'''
        )


''' d = [ ["Mark", 12, 95],
     ["Jay", 11, 88],
     ["Jack", 14, 90]]
print("jeisonnnn")     
print ("{:<8} {:<15} {:<10}".format('Name','Age','Percent'))

for v in d:
    name, age, perc = v
    print ("{:<8} {:<15} {:<10}".format( v[0], v[1], v[2])) '''
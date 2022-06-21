                                 #Proyecto: Comandos de Python
                        #Objetivo: Conocer un poco de los comando básicos de Python
                                #Estudiantes: Fiorela, Tatiana, Christian

#Control de errores
try:
#Creación del diccionario.
    comandos={
"print":"Para imprimir expresiones en la pantalla",
"input":"Permite obtener una expresión del usuario y se asigna a una variable",
"def" : "Permite crear una funcion",                                                    
"none": "Denota falta de valor",
"str": "Utilizado para guardar texto",
"for": "Código que se ejecuta repetidas veces hasta que se deje de cumplir una condición",
"del": "Permite eliminar objetos",
"int": "Permite almacenar valores numéricos entero",
"float": "Permite almacenar valores decimales"}

#Menú principal
    while True:
        menu = int(input("1-Para conocer sobre algún comando de Python\n2-Para agregar un nuevo comando al diccionario\n3-Mostrar la lista de comandos\n4-Salir\nIngresa el numero de la opción que desees: "))
#Primero opcion, para conocer un comando en especifico
        if menu == 1:
            comandoss = str(input("Cual comando desea conocer?: \n -print \n -input \n -def \n -none \n -str \n -for \n -del \n -int \n -float\n Escriba el nombre del comando que desea conocer: "))
            for key,value in comandos.items():                                      
                if key==comandoss:
                    print(key, "->", value)
                    break
            else:
                print("Este dato no está en nuestro diccionario, ingrese 2 para agregar una nueva función o característica. ")
#Segunda opcion, para ingresar un comando nuevo
        elif menu == 2:
            insertar= str(input("Ingrese el nombre de un nuevo comando: "))
            insertar2 = str(input("Ingrese la definición de la nueva función: "))
            comandos.update ({insertar : insertar2})
#Tercera opción, mostrar el diccionario
        elif menu == 3:
            for key, value in comandos.items():
                print(key, "->", value)
                print ("______________________________________________________________________________")
#Cuarta y ultima opción, salir
        elif menu == 4:
            print ("Ta bien, hasta luego!")
            break
        else:
            print ("¡¡¡ Ingresa solo numeros enteros del 1 al 4 !!!")

except ValueError:
    print ("¡¡¡ Valor invalido, escribe numeros !!!")
except: 
    print ("¡¡¡ Cometiste un error, intenta de nuevo")
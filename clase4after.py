#      01234->5
#Lunes -> Python | Martes -> After Class | Otro -> no hay clases

# dia = input("¿Que dia es hoy?: ")

# if (dia == "lunes"):
#     print("Hoy tengo clase de Python")
# elif (dia == "martes" ):
#     print("Hoy tenes After Class")
# else:
#     print("No hay clases") ctrl + }
#
nombre = input("Ingresa tu nombre: ")
if(nombre == "" ):
    print(nombre)
else:
    print("Hola", nombre)




# match dia:
#     case "lunes":
#         print("Hoy tengo clase de Python")
#     case "martes":
#         print("Hoy tenes After Class")
#     case "miercoles":
#         print("No hay clases")
#     case "jueves":
#         print("No hay clases")
#     case "viernes":
#         print("No hay clases")
#     case _:
#         print("No ingresaste un dia")



# numero = int(input("Ingresa un nro del 1 al 5: "))

# # # Estructura Match
# match numero:
#     case 1:
#         print ("Es 1")
#     case 2:
#         print ("Es 2")
#     case 3:
#         print ("Es 3")
#     case 4:
#         print ("Es 4")
#     case 5: 
#         print ("Es 5")
#     case _:
#         print ("No cumpliste la consigna")
##################### AFTER CLASS ############################
# @            012345678910--14
# texto = "    jAN NETH@gmail@com"
texto = input("Ingrese mail: ")
texto = texto.strip() #elimina espacion inicio/fin
posicion=texto.find("@") #nro
if(texto.find("@")>-1): #true
    print("El mail es valido") #8
    if(texto[posicion+1:].find("@")>-1): # 8>8
        print("El mail es valido")
else:
    print("El mail no es valido")


# print(texto.upper())

#  nombre[inicio:fin]
# print(texto[0:8])


# nombre = input("Ingresa tu nombre: ") #la primera letra de cada palabra a mayúsculas y el resto en minúsculas.
#         Janneth

# print (nombre.title())

# CREACION DE MODULOS PROPIOS
# import modulo #solo escribir nombre
# from modulo import * # para utilizar una funcion en especifico
# import modulo as md #Cambiando a apodo
# print(md.despedir("Ana"))
# print(md.saludar("Juan"))
# from datetime import datetime
# import random as rd # nombreModulo.funcion
# from random import * # funcion
# frutas = ["banana","mandarina", "frutilla"]
# print(rd.uniform(1.5 , 3.7)) #elegir nro aleatorio flotante
# print(rd.random())
# muestra = rd.sample(range(100), 5) # (elementos, cantidad) 
# print(muestra)


# print(random.random()) #Nro entre 0 y 1
# print(random.randint(1, 5)) #Nro entero entre los solicitados (a,b)
# print(random.choice(frutas)) #elegir un elemento de la lista fruta(lista)
# print(frutas)
# random.shuffle(frutas) #Mezcla los elementos de la lista
# print(frutas)



# fecha_hora_actual = datetime.now()
# print("Fecha y hora actual:", fecha_hora_actual)
# print("Solo la fecha:", fecha_hora_actual.strftime("%Y-%m-%d"))
# print("Solo la hora:", fecha_hora_actual.strftime("%H:%M:%S"))
# print("Fecha legible:", fecha_hora_actual.strftime("%d de %B de %Y"))


# from colorama import Fore, Back, init
# init() #Inicializa colorama Back->Fondo | Fore->Texto
# print(Fore.GREEN + "Texto en verde")
# print(Back.RED + "Fondo rojo" + Back.RESET)
# print(Fore.BLUE + Back.YELLOW + "Texto azul en fondo amarillo")

archivo = open("datos.txt", "w") # ruta al archivo, modo
archivo.write("Hola, este es un archivo de prueba de clase 11.\n")
archivo.write("Segunda línea del archivo.\n")
archivo.close()

archivo = open("datos.txt", "a")
archivo.write("Tercera línea del archivo.\n")
archivo.close()

archivo = open("datos.txt", "r")
# contenido = archivo.read()
lineas = archivo.readlines()
# print(lineas)
for linea in lineas:
    print(linea.strip())
print(lineas)
archivo.close() 


archivo = open("nombres.txt", "w")
archivo.write("María\n")
archivo.write("Carlos\n")
archivo.write("Lucía\n")
archivo.close()

archivo = open("nombres.txt", "r+")
archivo.write("Jose\n")
archivo.write("Marta\n")
archivo.close()

archivo = open("nombres.txt", "a")
archivo.write("Pedro\n")
archivo.write("Tomas\n")
archivo.close()

archivo = open("nombres.txt", "r")
# contenido = archivo.read()
lineas = archivo.readlines()
print(lineas)
print("Contenido del archivo:")
for linea in lineas:
    print(linea.strip())
archivo.close()


archivo = open("./CLASE 11/productos.txt", "r") # ruta al archivo, modo
lineas = archivo.readlines()
for linea in lineas:
    print(linea.strip())
print(lineas)
archivo.close() 


# AFTER CLASS
import moduloConFuncionesBasicas as md
from moduloConFuncionesBasicas import *

# print(suma(4,6))
# print(resta(5,2))
# print(saludar("Juan"))
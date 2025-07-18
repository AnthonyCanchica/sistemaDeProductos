productos = ["manzanas", "piñas", "bananas", "uvas"]
texto ="HOLA"
# for i in productos: 
#     print("Producto disponible:", i)

############# 0         1          2        3      4        5          6   -> 7
frutas = ["manzana", "banana", "naranja", "pera", "kiwi", "pomelo", "granada"]
# for i in range(0,len(frutas),2): #3
#     print(f"Fruta {i}: {frutas[i]}") #f-string
    # print("frutas", i)

    # print(i)

# range(inicio, fin, paso)    

# print(range(3)) 

# for i in range(6, 10, 2): #  1, 3,5,7, 9
#     print(i)

# ingresos = [40000, 55000, 60000, 45000, 70000, 50000]
# count = 0

# for ingreso in ingresos:
#     if ingreso > 50000:
#         count += 1

# # print(f"Cantidad de ingresos superiores a $50000: {count}")

# usuarios = ["Ana", "Luis", "Andrés", "María", "Alejandro", "Lucía"]
# letra_buscada = "A"

# for nombre in usuarios:
#     if nombre.startswith(letra_buscada):
#         print(f"Nombre que empieza con '{letra_buscada}': {nombre}")

# LISTAS Y TUPLAS - Clase 7

############# 0         1          2        3      4        5          6   -> 7
frutas = ["manzana", "banana", "naranja", "pera", "kiwi", "banana","pomelo", "granada"]
# print(frutas[3])
frutas.append("limon") #agregar al final
frutas.remove("banana")
# 
# print(frutas)

tuplaFruta = ("", "banana", "   ", "pera", "kiwi", "banana","pomelo", "granada")

# tuplaFruta[3] = "limon"

# print(tuplaFruta.index("manzana"))


# ############## AFTER CLASS #####################

# nombre = input("Ingresa nombre: ")
# while nombre == "":
# while nombre == "": #Jann
#     print("Nombre en blanco")
#     nombre = input("Ingresa nuevamente su nombre: ")

# print("Hola", nombre)
#  indice    0        1       2        3        4       5   -> 6
nombres = ["Julia", "Jann", "Pedro", "Kevin", "   " , "Lupe"]

# cantidad = len(nombres)
# contador = 0

# while  contador<cantidad: #true
#     nombreOK = nombres[contador].strip()
#     if(nombreOK == ""): # "    " == ""
#         print("Esta vacio")
#     else:
#         print(nombres[contador])
#     contador +=1 #contador = contador + 1

nombres = ["Julia", "Jann", "Pedro", "Kevin", "   " , "Lupe", "FeDerico"]
#range()
for i in range(0,len(nombres)):
    nombreOK = nombres[i].strip()
    if(nombreOK == "Jann"): # 
        print("lo encontre")
    else:
        print(f"Cliente {i+1}: {nombreOK}")
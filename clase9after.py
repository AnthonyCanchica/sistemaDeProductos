# print ("MENÚ")
# print ("1. Agregar producto\n2. Mostrar productos\n3. Buscar producto\n4. Eliminar producto\n5. Salir")
# opcion=input("Elegi tu opcion") #
# productos = [["tomate","verdura",150],["limon","fruta",100]] #lista con sublistas
prueba=[]
productos = {"tomate":150, "madarina":100,"naranja":150} #lista con un diccionario
print("Si ingresa FIN salis del programa")
producto = input ("Ingresa el nombre del producto") #clave
precio = input ("Ingresa el precio") # valor

#     dict [clave] = valor
#agregando un nuevo par de datos clave:valor a un diccionario
productos[producto] = precio
#agregando el diccionario a una lista
prueba.append(productos)


print(prueba)

# AGREGANDO LISTA DENTRO DE UNA LISTA / Se lo conoce como Sub lista
# nombre = input("Ingresa nombre de producto")
# categoria = input("Ingresa categoria")
# precio = int(input("Ingresa precio"))


# productos.append([nombre,categoria,precio])
# print(productos)



# EJEMPLO BASICO DE MENÚ CON OPCIONES
# while opcion != "5":
# # Alguna accion va a estar realizando
#     if(opcion=="1"):
#         print("Agregando producto")
#     elif(opcion == "2"):
#         print("Mostras productos")
#     else:
#         print("Otra accion")

#     print ("1. Agregar producto\n2. Mostrar productos\n3. Buscar producto\n4. Eliminar producto\n5. Salir")
#     opcion=input("Elegi tu opcion") 

# print("Salio/toco nro 5")
#################################################
# UN EJEMPLO DE COMO RECORRER UNA LISTA CON DICCIONARIOS
listaDict = [{"nombre":"Juan","edad":30},{"nombre":"Pedro","edad":40},{"nombre":"Martin","edad":20}]

for i in listaDict:
    # print(i)
    for clave,valor in i.items():
        
        print(f"{clave}:{valor}")

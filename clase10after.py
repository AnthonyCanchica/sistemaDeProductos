print ("MENÚ")
print ("1. Agregar producto\n2. Mostrar productos\n3. Buscar producto\n4. Eliminar producto\n5. Salir")
opcion=input("Elegi tu opcion") # 0 ,  1 
productos = [["tomate","verdura", 200],["limon","fruta",400]] #lista con sublistas

# EJEMPLO BASICO DE MENÚ CON OPCIONES
while opcion != "5":
# Alguna accion va a estar realizando
    if(opcion=="1"):#agregar
        nombre = input("Ingresa Nombre")
        categoria = input ("Ingresa categoria") #clave
        precio = input ("Ingresa el precio") # valor
        otro = []
        otro.append(nombre)
        otro.append(categoria)
        otro.append(precio)
        print(otro)
        productos.append(otro)
        print(productos)
    elif(opcion == "2"):#mostrar
        for i in range(0,len(productos)):
            producto = productos[i]
            print(f"Producto {i+1}: {producto[0]} - {producto[2]}$")
    elif(opcion == "4"): #eliminar
        for i in range(0,len(productos)):
            producto = productos[i]
            print(f"Producto {i+1}: {producto[0]} - {producto[2]}$")

        eliminar=int(input("Ingresa un nro para eliminar")) #1
        for i in productos:
        # POR INDICE / REMOVE
            indice = (productos.index(i))+1 #metodo index
            # print(indice) ahi va a mostrar
            if(indice == eliminar):
             # productos.remove(i) #se pasa el dato
                productos.pop(indice-1) #se pasa la posicion

        print("Producto eliminado")
    else:
        print("Otra accion")

    print ("1. Agregar producto\n2. Mostrar productos\n3. Buscar producto\n4. Eliminar producto\n5. Salir")
    opcion=input("Elegi tu opcion") 

print("Salio/toco nro 5")
#################################################
# UN EJEMPLO DE COMO RECORRER UNA LISTA CON DICCIONARIOS
listaDict = [{"nombre":"Juan","edad":30},{"nombre":"Pedro","edad":40},{"nombre":"Martin","edad":20}]


# for i in listaDict:
#     # print(i)
#     for clave,valor in i.items():
#         # print("hola")
#         print(f"{clave}:{valor}")

#################################################

# productos[eliminar]
# print(productos[eliminar])
 
# print(productos)

# prueba=[]
# productos = {"tomate":150, "madarina":100,"naranja":150} #lista con un diccionario
# print("Si ingresa FIN salis del programa")


# #     dict [clave] = valor
# #agregando un nuevo par de datos clave:valor a un diccionario
# productos[producto] = precio
# #agregando el diccionario a una lista
# prueba.append(productos)

##############################
# AGREGANDO LISTA DENTRO DE UNA LISTA / Se lo conoce como Sub lista
# nombre = input("Ingresa nombre de producto")
# categoria = input("Ingresa categoria")
# precio = int(input("Ingresa precio"))

# productos.append([nombre,categoria,precio])
# print(productos)


print ("MENÚ")
print ("1. Agregar Producto\n2. Mostrar Productos\n3. Buscar Producto\n4. Eliminar Producto\n5. Salir")
opcion=int(input("Selecciona un numero de la lista: "))
productos = []

while opcion != "5":
# Alguna accion va a estar realizando
    if(opcion=="1"):#agregar
        nombre = input("Ingresa Nombre: ")
        categoria = input ("Ingresa Categoria: ") #clave
        precio = int(input ("Ingresa el Precio: ")) # valor
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
            print(f"Producto {i+1}: {producto[1]} - {producto[2]}$")
    elif(opcion == "4"): #eliminar
        for i in range(0,len(productos)):
            producto = productos[i]
            print(f"Producto {i+1}: {producto[1]} - {producto[2]}$")

        eliminar=int(input("Eliminar por numero del elmento: ")) #1
        for i in productos:
            indice = (productos.index(i))+1 #metodo index
            # print(indice) ahi va a mostrar
            if(indice == eliminar):
             # productos.remove(i) #se pasa el dato
                productos.pop(indice-1) #se pasa la posicion

        print("Producto eliminado: ")
    elif (opcion == "3"): #Buscar
        # Buscar -> Eliminar | palabra
        buscando = input ("Ingresa producto a buscar: ")
        for i in range(0,len(productos)):
            producto = productos[i]
            if (buscando == producto[0]):
                print(f"Producto encontrado {producto[0]}")
                print(f"Producto {i+1}: {producto[0]} - {producto[1]} {producto[2]}$")
                # productos.remove(producto) #Eliminar con remove
                # print(productos)
            # productos.pop(i) #eliminado con pop
            else:
                print("No Encontro el Producto")
    else:
        print("Seleccione una opcion de la lista")

    print ("1. Agregar Producto\n2. Mostrar Productos\n3. Buscar Producto\n4. Eliminar Producto\n5. Salir")
    opcion=input("Selecciona un numero de la lista: ") 

print("Salio/Toco Nro 5")
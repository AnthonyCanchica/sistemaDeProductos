# lista = [valor,valor,valor]
# tupla = (valor,valor,valor)
# dict = {clave:valor , clave:valor , } // key:value 
mi_diccionario = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Buenos Aires"
}

productos = {
    # nombre:precio
   "manzana": 150,
   "banana": 120,
   "naranja": 180
}
# mi_diccionario["profesión"] = "Ingeniera"
productos["mango"] = 250 #adicion 
productos["manzana"] = 500
# print(productos.popitem())
# print(productos)

frutas = ["banana","mandarina", "frutilla"]
# for i in frutas:
#     print(i)
# print (productos)
# print(productos.items())
# # # recorrer diccionarios
# for clave, valor in productos.items():
#     print(f"{clave}: {valor}")

# Diccionario anidados
estudiantes = {
    "Ana": {"edad": 22, "carrera": "Informática"},
    "Juan": {"edad": 24, "carrera": "Diseño"}
}

# print(estudiantes["Ana"]["carrera"])
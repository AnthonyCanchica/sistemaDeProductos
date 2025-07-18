# import sqlite3
# from colorama import Fore, Back, init
# init() #Inicializa colorama Back->Fondo | Fore->Texto
# print(Fore.GREEN + "Texto en verde")
# print(Back.RED + "Fondo rojo" + Back.RESET)
# print(Fore.BLUE + Back.YELLOW + "Texto azul en fondo amarillo")
import sqlite3
import mimodulo

mibdd= "Bases/productos.db"

# CREACION DE TABLA
def creando_tabla(variable): # variable="inventario.db"
    conexion = sqlite3.connect(variable)
    # print("Conexion realizada")
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        categoria TEXT NOT NULL,
        precio INTEGER NOT NULL)           
    ''')
    conexion.close()

mimodulo.actualizar(mibdd)

# actualizar(mibdd)

# AGREGANDO PRODUCTO / Falta conexion, cursor, commit y close
# cursor.execute("""
#     INSERT INTO productos (nombre, categoria, precio)
#     VALUES (?, ?, ?)
#     """, ("Lapiz","Libreria", 25.50))

# SELECCIONAMOS PARA VER LOS DATOS / Falta conexion, cursor y close
def mostrar ():
    conexion = sqlite3.connect("Bases/productos.db")
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM productos')
    productos = cursor.fetchall()
    print(productos)
    for producto in productos:
        print(f"ID: {producto[0]}, Nombre: {producto[1]}, Categoria: {producto[2]} Precio: ${producto[3]:.2f}")

    conexion.close()

mostrar()

# def actualizar(ruta):
#     try:
#         conexion = sqlite3.connect(ruta)
#         cursor = conexion.cursor()
#         conexion.execute("BEGIN TRANSACTION")
#         # Operaciones SQL
#             # CODIGO 
#         nuevo_precio = 2500
#         id_producto = int(input("Que producto queres modificar? Ingresa ID: "))
#         cursor.execute('UPDATE productos SET precio = ? WHERE id = ?', (nuevo_precio, id_producto))
#         conexion.commit()

#     except sqlite3.Error as e:
#         print(f"Error: {e}")
#         conexion.rollback()
#     finally:
#         conexion.close()



def eliminando ():
    conexion = sqlite3.connect("Bases/productos.db")
    cursor = conexion.cursor()
    nombre_producto = "Lapiz"
    cursor.execute("DELETE FROM productos WHERE nombre = ?", (nombre_producto,))
    conexion.commit()
    conexion.close()
























# Contenido de clase 12
# try:
#     archivo = open("datos.txt", "r")
#     contenido = archivo.read()
#     print("Contenido del archivo:")
#     print(contenido)
#     archivo.close()
# except FileNotFoundError:
#     print("Error: El archivo 'datos.txt' no existe.")
#     print("Verificá el nombre o la ubicación del archivo.")
import sqlite3

conexion = sqlite3.connect("productos.db")
cursor = conexion.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    precio FLOAT NOT NULL)
''')

opcion = input("Vas a agregar un producto, si presionas 5 o otro para salis")

while opcion == "5":
    nombreP = input("Ingresa Nombre del Producto: ")
    precioP = int(input("Ingresa Precio del Producto: "))
    cursor.execute('''
    INSERT INTO productos (nombre, precio)
    VALUES (?, ?)
    ''', (nombreP, precioP))
    conexion.commit()
    opcion = input("Vas a agregar un producto, si presionas 5 o otro para salis")


# nombre_producto = "Lápiz"
# cursor.execute("""
#                DELETE FROM productos WHERE nombre = ? 
#                """, (nombre_producto))


cursor.execute('SELECT * FROM productos')
productos = cursor.fetchall()
# print(productos)
for producto in productos:
    print(f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: ${producto[2]:.2f}")

# conexion.commit()

# conexion.commit()

conexion.close()
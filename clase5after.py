# variable tipo String | str
#tamaño= 012345678-------16 -> posiciones
# @            012345678910--14
# texto = "    jAN NETH@gmail@com"
# texto = input("Ingrese mail: ")
# texto = texto.strip() #elimina espacion inicio/fin
# posicion=texto.find("@") #nro
# if(texto.find("@")>-1): #true
#     print("El mail es valido") #8
#     if(texto[posicion+1:].find("@")>-1): # 8>8
#         print("El mail es invalido")
# else:
#     print("El mail es invalido")


    


# texto[0]="J"
# print(texto.find("@"))
# print(texto.replace("ANNETH", "anneth"))
# print(texto[0])



# print(texto.upper())

#  nombre[inicio:fin]
# print(texto[0:8])

# nombre = "Ana"
# edad = 30
# print("Nombre "+ nombre + " tiene "+ edad)
# print(f"Hola, {nombre}. Tienes {edad} años.")
# Salida: Hola, Ana. Tienes 30 años.

# nombre = input("Ingresa tu nombre: ") #la primera letra de cada palabra a mayúsculas y el resto en minúsculas.
#         Janneth

# print (nombre.title())

# CLASE 5 - BUCLE WHILE


# contador = 1 #cont
# while contador <= 3:
#    print(f"Este es el intento número {contador}.")
#    contador += 1 #contador = contador + 1

# nombre = ""

# while nombre == "":
#     nombre = input("Ingresá tu nombre: ").strip() # strip():elimina espacios al inicio y al fin
#     if nombre == "":
#        print("El nombre no puede estar vacío. Intentá de nuevo.")

# print(f"¡Hola, {nombre}! Gracias por ingresar tu nombre.")




# LISTA -> [], modificar valores
# Lista de números
numero = 200
# indice ->0 , 1 , 2 , 3 , 4
numeros = [10, 20, 30, -40, 50]
cantidad= len(numeros)
# Len -> cantidad total de caracteres/valores
texto = "HOLA"

contador = 0



# BREAK Y CONTINUE -> VER
# numero = 0
# print("Ingresá números positivos para sumarlos. Ingresá 0 para terminar.")
# suma = 0
# while True:
#    # Solicitamos al usuario un número
#    numero = int(input("Ingresá un número: "))
#    # Verificamos si el número es negativo
#    if numero < 0:
#        print("El número es negativo, se ignora. Intentá de nuevo.")
#        continue  #omite sola esa senctencia
#    if numero == 0:
#        break     #corta bucle while
#    suma += numero

# print(f"La suma es: {suma}")

productos = ["manzanas", "piñas", "bananas", "uvas"]
texto ="HOLA"
for i in texto: 
    print("Producto disponible:", i)


##################### AFTER CLASS ############################
contador = 1
sueldoTotal= 0
while contador <= 6:
    sueldoMes = float(input(f"Ingresa tu sueldo del mes {contador}: "))
    while(sueldoMes<0):
        print("El valor no es valido") 
        sueldoMes = float(input(f"Ingresa tu sueldo del mes {contador}: "))
        if(sueldoMes>0):
            # sueldoTotal = sueldoTotal + sueldoMes
            break
    sueldoTotal=sueldoTotal+sueldoMes
    contador +=1

print(f"El sueldo es: {sueldoTotal}")


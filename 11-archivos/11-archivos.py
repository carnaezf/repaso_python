"""
Objetivos de la clase:
    1. Conectar un archivo de texto desde Python.
    2. Leer y escribir en archivos.
    3. Realizar operaciones dentro de los archivos.
    4. Utilizar manejo de excepciones con "try" y "except".

Modos Comunes de Apertura de Archivos:
    "r": Lectura (Por defecto).
    "w": Escritura (Borra el contenido del archivo si es que existe).
    "a": Añadir al final del archivo.
    "b": Modo binario.
    "t": Modo texto.

Métodos Comunes para Manejo de Archivos:
    - read(): Leer todo el contenido del archivo.
    - readline(): Leer una sola línea del archivo.
    - readlines(): Leer todas las líneas del archivo y devolverlas como una lista.
"""

# Abrir y cerrar archivos

# Ejemplo de cómo abrir un archivo para lectura
archivo = open("11-archivos/texto/ejemplo.txt", "r")
print(archivo)  # Muestra información sobre el archivo abierto
archivo.close()  # Cierra el archivo

# Leer un archivo línea por línea
archivo = open("11-archivos/texto/ejemplo.txt", "r")
for linea in archivo:
    print(linea.strip())  # strip() elimina los espacios en blanco al principio y al final
archivo.close()  # Cierra el archivo

# Escribir en un archivo
archivo = open("11-archivos/texto/ejemplo-2.txt", "w")
archivo.write("Primera linea\n")  # Escribe la primera línea en el archivo
archivo.write("Segunda linea\n")  # Escribe la segunda línea en el archivo
archivo.close()  # Cierra el archivo

# Añadir una línea a un archivo existente
archivo = open("11-archivos/texto/ejemplo-2.txt", "a")
archivo.write("Tercera linea\n")  # Añade una tercera línea al final del archivo
archivo.close()  # Cierra el archivo

# Manejo de excepciones al abrir un archivo inexistente
try:
    archivo = open("archivo-que-no-existe.txt", "r")
    contenido = archivo.read()  # Intenta leer el contenido del archivo
    print(contenido)
except FileNotFoundError:
    print("El archivo no existe.")  # Mensaje de error si el archivo no existe
finally:
    archivo.close()  # Asegura que el archivo se cierre

# Manejo de excepciones al abrir un archivo existente
try:
    archivo = open("texto/ejemplo-2.txt", "r")
    contenido = archivo.read()  # Lee el contenido del archivo
    print(contenido)
except FileNotFoundError:
    print("El archivo no existe.")  # Mensaje de error si el archivo no existe
finally:
    archivo.close()  # Asegura que el archivo se cierre

# Ejemplos prácticos

# Contador de líneas en un archivo
archivo = open("11-archivos/texto/ejemplo.txt", "r")
contador = 0
for linea in archivo:
    contador += 1  # Incrementa el contador por cada línea leída
    print(contador, linea.strip())  # Muestra el número de línea y el contenido de la línea
print(f"Numero de lineas: {contador}")  # Muestra el número total de líneas
archivo.close()  # Cierra el archivo

# Contador de palabras en un archivo
archivo = open("11-archivos/texto/ejemplo.txt", "r")
contenido = archivo.read()  # Lee todo el contenido del archivo
palabras = contenido.split()  # Divide el contenido en palabras
print(palabras)  # Muestra las palabras
print(f"Numero de palabras: {len(palabras)}")  # Muestra el número total de palabras
archivo.close()  # Cierra el archivo











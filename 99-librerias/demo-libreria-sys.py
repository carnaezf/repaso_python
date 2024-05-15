import sys

# sys.argv es una lista que contiene los argumentos de la línea de comandos
# El primer elemento (sys.argv[0]) es el nombre del archivo que se está ejecutando
nombre_archivo = sys.argv[0]

# El segundo elemento (sys.argv[1]) es el primer argumento pasado al script
# Este script asume que al menos un argumento ha sido proporcionado
primer_argumento = sys.argv[1]

# Imprime el nombre del archivo en ejecución
print("Nombre del archivo:", nombre_archivo)

# Imprime el primer argumento proporcionado en la línea de comandos
print("Primer argumento:", primer_argumento)


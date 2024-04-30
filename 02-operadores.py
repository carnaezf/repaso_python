# Operadores Aritméticos

# Suma
print(3 + 4)  # Imprime 7

# Resta
print(3 - 4)  # Imprime -1

# Multiplicación
print(3 * 4)  # Imprime 12

# División
print(43 / 4)  # Imprime 10.75

# División entera
print(43 // 4)  # Imprime 10

# Potencia
print(2 ** 3)  # Imprime 8

# Combinación de operadores
print(2 ** 3 + 3 - 7 / 1)  # Imprime 6.0

# Operaciones con cadenas de texto

# Concatenación de cadenas
print("Hola " + "Python " + "¿Como estas?")  # Imprime "Hola Python ¿Como estas?"

# Función len() para obtener la longitud de una cadena
print(len("123456"))  # Imprime 6

# Operaciones mixtas con cadenas de texto

# Repetición de cadenas
print("Hola " * 5)  # Imprime "Hola Hola Hola Hola Hola "
print("Hola " * (2 ** 4))  # Imprime "Hola " repetido 16 veces

# Trabajando con tipos de datos mixtos

# Definición de una variable tipo float y multiplicación
my_float = 2.5 * 2
print(type(my_float))  # Imprime <class 'float'>
print(my_float)  # Imprime 5.0

# Conversión de tipo y repetición de cadena
print("hola " * int(my_float))  # Imprime "hola " repetido 5 veces

# Operadores de comparación

# Comparación de enteros
print(3 > 4)  # Imprime False
print(3 < 4)  # Imprime True
print(3 >= 4)  # Imprime False
print(3 <= 4)  # Imprime True
print(3 == 4)  # Imprime False
print(3 != 4)  # Imprime True

# Operaciones con cadenas de texto en comparaciones
print("Programando" > "Python")  # Imprime True (comparación lexicográfica)
print("aaaa" >= "abaa")  # Imprime False (comparación lexicográfica)

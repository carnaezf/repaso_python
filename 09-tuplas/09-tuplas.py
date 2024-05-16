# Tuplas en Python

# Las tuplas son estructuras de datos similares a las listas, pero son inmutables, 
# lo que significa que una vez creadas, sus elementos no pueden ser modificados. 
# Se utilizan cuando necesitas almacenar una colección de elementos que no deben cambiar.

# Definición de una tupla
# Usamos paréntesis para definir una tupla
tupla_ej = ("Abril", 2021)
tupla_ej_2 = ("Abril", 2021, "Mayo", 1, True, 1.0)

# Imprimir el contenido de las tuplas
print("Contenido de tupla_ej:", tupla_ej)
print("Contenido de tupla_ej_2:", tupla_ej_2)

# Desempaquetado de una tupla
# Cada valor de la tupla se asigna a las variables month y year respectivamente
print("----")
month, year = tupla_ej
print("Mes:", month)
print("Año:", year)

# Desempaquetado de una cadena
# Similarmente, podemos desempaquetar cada carácter de una cadena en variables individuales
print("----")
language = "Python"
p, y, t, h, o, n = language
print(p)
print(y)
print(t)
print(h)
print(o)
print(n)

# Intentar modificar un elemento de una tupla
# Las tuplas son inmutables, por lo que intentar modificar uno de sus elementos genera un error
print("----")
tupla = (1, 2, 3)  # Tupla original

try:
    tupla[0] = 4  # Esto generará un TypeError
except TypeError as e:
    print(f"Error: {e}")  # Capturamos e imprimimos el error

print("El programa continúa")

# Para "modificar" una tupla, necesitamos crear una nueva tupla con los cambios deseados
nueva_tupla = (4,) + tupla[1:]  # Creamos una nueva tupla con el primer elemento modificado

print("Tupla original:", tupla)
print("Nueva tupla:", nueva_tupla)

# Conclusión: Las tuplas son útiles para almacenar datos que no deben cambiar a lo largo del programa. 
# Aunque no se pueden modificar directamente, podemos crear nuevas tuplas basadas en las existentes.










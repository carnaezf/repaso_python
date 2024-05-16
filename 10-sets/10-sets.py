# Sets en Python

# Los sets son estructuras de datos que permiten almacenar elementos únicos.
# Son útiles cuando necesitamos eliminar duplicados de una colección de elementos.

# Definición de un set
# En este ejemplo, se observa que hay valores repetidos.
muchos_animales = {'Gato', 'Perro', 'Tortuga', 
                   'Gato', 'Perro', 'Tortuga', 
                   'Gato', 'Perro', 'Tortuga', 
                   'Gato', 'Perro', 'Tortuga', 
                   'Hurón', 'Hamster', 'Erizo de Tierra'}

# Al imprimir, solo se mostrarán valores únicos.
print(muchos_animales)  # {'Perro', 'Erizo de Tierra', 'Hamster', 'Gato', 'Hurón', 'Tortuga'}

# Crear un set vacío
my_set = set()
print("Tipo de my_set:", type(my_set))  # <class 'set'>

# Crear un set usando llaves
animales = {"Gato", "Perro", "Hurón", "Hamster", "Erizo de Tierra"}
print("Animales:", animales)

# Ejemplo práctico con sets: Análisis de texto para palabras únicas
texto = "El perro y el gato son amigos. El perro es leal y el gato es independiente"

# Dividir el texto en palabras
palabras = texto.split()
print("Palabras en el texto:", palabras)

# Crear un set de palabras únicas
palabras_unicas = set(palabras)
print("Palabras únicas en el texto:", palabras_unicas)

print("-------")

# Métodos comunes de los sets

# Añadir un elemento al set
animales.add("Tortuga")
print("Animales después de añadir 'Tortuga':", animales)

# Intentar eliminar un elemento que no está en el set
# Esto causará un error si el elemento no está presente
# animales.remove("Puma")  # Descommentar esta línea para ver el error

# Usar discard para eliminar un elemento sin causar error si el elemento no existe
animales.discard('Ballena')
print("Animales después de intentar descartar 'Ballena':", animales)

# Eliminar y devolver un elemento del set
animal_eliminado = animales.pop()
print("Animal eliminado:", animal_eliminado)
print("Animales después de pop():", animales)

# Limpiar todos los elementos del set
animales.clear()
print("Animales después de clear():", animales)

print("-------")

# Convertir un diccionario a una lista de tuplas (pares clave-valor)
prueba_diccionario = {"k1": 5, "k2": 7}
mi_lista = list(prueba_diccionario.items())  # [('k1', 5), ('k2', 7)]
print("Lista de pares clave-valor:", mi_lista)

# Convertir una lista de tuplas de nuevo a un diccionario
prueba_lista = [('k1', 5), ('k2', 7)]
mi_diccionario = dict(prueba_lista)
print("Diccionario convertido de la lista:", mi_diccionario)

print("-------")

# Mostrar métodos disponibles para strings
print("Métodos disponibles para strings:", dir("a"))

print("----")

# Bonus
# Intentar sumar una lista de strings causará un error
# Usar map para convertir los elementos a enteros antes de sumarlos
var = ["1", "2", "3"]
print("Suma de var:", sum(map(int, var)))  # 6










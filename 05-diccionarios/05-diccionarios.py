# Listas:
# En Python, las listas pueden contener elementos de diferentes tipos.
# Ejemplo de lista con solo strings:
animales = ['gato', 'perro', 'raton']

# Iterar sobre la lista y mostrar el tipo de cada elemento
for animal in animales:
    print(type(animal))

# Añadir un nuevo elemento a la lista
animales.append('hamster')
print(animales)  # Imprime: ['gato', 'perro', 'raton', 'hamster']

print('--------')

# Las listas pueden contener elementos de distintos tipos de datos.
lista_heterogenea = [1, "gato", 3.0, False]

# Iterar sobre la lista heterogénea y mostrar el tipo de cada elemento
for elemento in lista_heterogenea:
    print(type(elemento))

# Para crear una lista utilizaremos la siguiente sintaxis:
# Elementos de la lista son todo lo que esté dentro de los corchetes [], separados por coma.
print('--------')

# Ejemplo de lista con diferentes estructuras de datos
estructuras = [{"clave": "valor"}, (), []]
for estructura in estructuras:
    print(type(estructura))

print('--------')
print("Se muestra en pantalla")

# Ejemplo de lista con números
lista = [1, 2, 3]
print(lista)

# Ejemplo de lista con strings
string_numbers = ["uno", "dos", "tres"]
print(string_numbers)  # Imprime: ['uno', 'dos', 'tres']

print('--------')
# Acceso a elementos de la lista por índice
print(string_numbers[0])  # Imprime: uno
print(string_numbers[1])  # Imprime: dos
print(string_numbers[2])  # Imprime: tres

print('--------')

# Ejemplo de lista con colores
colores = ["verde", "rojo", "rosa", "azul"]
print(colores[0])  # Imprime: verde
print(colores[1])  # Imprime: rojo
print(colores[3])  # Imprime: azul

print('--------')
# Acceso a elementos de la lista usando índices negativos
a = [1, 2, 3, 4, 5]
print(a[-1])  # Imprime: 5
print(a[-2])  # Imprime: 4
print(a[-3])  # Imprime: 3
print(a[-4])  # Imprime: 2
print(a[-5])  # Imprime: 1
# print(a[-6]) # IndexError: fuera de rango, ya que no hay un sexto elemento desde el final

# Añadir elementos a la lista de colores
colores.append("celeste")
print(colores)  # Imprime: ['verde', 'rojo', 'rosa', 'azul', 'celeste']

print('--------')
# Eliminar el cuarto elemento (índice 4) de la lista
elimina = colores.pop(4)
print(colores)  # Imprime: ['verde', 'rojo', 'rosa', 'azul']
print(elimina)  # Imprime: celeste

print('--------')
# Ejemplo de lista con nuevos colores
colores = ['rojo', 'rosa']

# Verificar si un elemento está en la lista
print("rojo" in colores)  # Imprime: True
print("turquesa" in colores)  # Imprime: False

print('--------')
# Ejemplo de listas de números y animales
numeros = [100, 20, 70, 500]
animales = ["perro", "gato", "hurón", "erizo"]

# Invertir el orden de los elementos en la lista
numeros.reverse()
animales.reverse()
print(numeros)  # Imprime: [500, 70, 20, 100]
print(animales)  # Imprime: ['erizo', 'hurón', 'gato', 'perro']

print('--------')
# Ordenar los elementos en la lista en orden ascendente
animales.sort()
numeros.sort()
print(animales)  # Imprime: ['erizo', 'gato', 'hurón', 'perro']
print(numeros)  # Imprime: [20, 70, 100, 500]

# Ordenar una lista temporalmente en orden descendente
print(sorted([3, 6, 7, 4, 1], reverse=True))  # Imprime: [7, 6, 4, 3, 1]

# Obtener el índice de un elemento en la lista
print(animales.index('erizo'))  # Imprime: 0

print('--------')
# Definimos dos listas de animales
animales = ['Gato', 'Perro', 'Tortuga']
animales_2 = ['Hurón', 'Hamster', 'Erizo de Tierra']

# Concatenar las listas
mascotas = animales + animales_2
print("Concatenado listas:", mascotas)
# Veamos algunas características
print(animales)  # Imprime: ['Gato', 'Perro', 'Tortuga']
print(len(animales))  # Imprime: 3
print(animales_2)  # Imprime: ['Hurón', 'Hamster', 'Erizo de Tierra']
print(len(animales_2))  # Imprime: 3
print(mascotas)  # Imprime: ['Gato', 'Perro', 'Tortuga', 'Hurón', 'Hamster', 'Erizo de Tierra']
print(len(mascotas))  # Imprime: 6

# Multiplicar una lista para crear una lista repetida
nuevos_numeros = [1, 2, 3] * 4
print(nuevos_numeros)  # Imprime: [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]

# Clase II
# Diccionarios en Python

# Los diccionarios son estructuras de datos que almacenan pares clave-valor.
# A continuación, se muestran algunos métodos útiles para trabajar con diccionarios.

# Definición de un diccionario
computador = {
    'notebook': 489990, 
    'tablet': 120000, 
    'cargador': 12400
}

# Método keys()
# Este método devuelve una vista de todas las claves en el diccionario.
# print(type(computador.keys()))  # Muestra el tipo de objeto devuelto por el método keys()
claves = computador.keys()

# Convertir la vista a una lista
lista_claves = list(claves)
print("Lista de claves:", lista_claves)  # Imprime: ['notebook', 'tablet', 'cargador']

print("---------")

# Método values()
# Este método devuelve una vista de todos los valores en el diccionario.
valores = computador.values()
print("Valores:", valores)  # Muestra la vista de los valores

# Convertir la vista a una lista
lista_valores = list(valores)
print("Lista de valores:", lista_valores)  # Imprime: [489990, 120000, 12400]

print("---------")

# Método items()
# Este método devuelve una vista de todos los pares clave-valor en el diccionario.
pares = computador.items()
print("Pares clave-valor:", pares)  # Muestra la vista de los pares clave-valor

# Convertir la vista a una lista
lista_pares = list(pares)
print("Lista de pares clave-valor:", lista_pares)  
# Imprime: [('notebook', 489990), ('tablet', 120000), ('cargador', 12400)]

# Acceder a elementos específicos en la lista de pares clave-valor
print("Primer par:", lista_pares[0])  # Imprime: ('notebook', 489990)
print("Segundo par:", lista_pares[1])  # Imprime: ('tablet', 120000)
print("Tercer par:", lista_pares[2])  # Imprime: ('cargador', 12400)

print("---------")

# Método get()
# Este método devuelve el valor de una clave especificada.
# Si la clave no existe, devuelve un valor predeterminado.
print(computador.get('iphone', "IPHONE NO ENCONTRADO"))  # Imprime: IPHONE NO ENCONTRADO
print(computador.get('notebook', "IPHONE NO ENCONTRADO"))  # Imprime: 489990

print("---------")
























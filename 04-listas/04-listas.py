# Listas

# Crear una lista vacía utilizando corchetes
mi_lista = []
print(mi_lista)  # Imprimirá una lista vacía: []

# Crear una lista vacía utilizando el constructor list()
mi_otra_lista = list()
print(mi_otra_lista)  # Imprimirá una lista vacía: []

# Mostrar el tipo de datos de las listas, que será 'list'
print(type(mi_lista))  # Imprimirá: <class 'list'>
print(type(mi_otra_lista))  # Imprimirá: <class 'list'>

# Crear una lista con números enteros
my_list = [45, 20, 63, 78, 45]
print(my_list)  # Imprimirá: [45, 20, 63, 78, 45]

# Crear una lista con diferentes tipos de elementos
elementos = [4444, 2.0, 5, 5]
print(elementos)  # Imprimirá: [4444, 2.0, 5, 5]
print(type(elementos))  # Imprimirá: <class 'list'>

# Cambiar el primer elemento de la lista 'elementos'
elementos[0] = 77
print(elementos)  # Imprimirá: [77, 2.0, 5, 5]

# Añadir un elemento al final de la lista 'elementos'
elementos.append(100)
print(elementos)  # Imprimirá: [77, 2.0, 5, 5, 100]

# Insertar un elemento en una posición específica (posición 2)
elementos.insert(2, "Insertar")
print(elementos)  # Imprimirá: [77, 2.0, 'Insertar', 5, 5, 100]

# Crear una copia de la lista 'elementos'
mi_nueva_lista = elementos.copy()
print(mi_nueva_lista)  # Imprimirá una copia de 'elementos'

# Añadir un elemento al final de 'mi_nueva_lista'
mi_nueva_lista.append("Ultimo")
print(mi_nueva_lista)  # Ver los cambios en 'mi_nueva_lista'
print(elementos)  # Ver que 'elementos' no cambió

# Limpiar todos los elementos de 'mi_nueva_lista'
mi_nueva_lista.clear()
print(mi_nueva_lista)  # Imprimirá: []

# Ordenar la lista 'elementos'
elementos = [4444, 2.0, 5, 5]
print(elementos)  # Imprimirá: [4444, 2.0, 5, 5]
elementos.sort()
print(elementos)  # Imprimirá: [2.0, 5, 5, 4444]


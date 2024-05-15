# Lista vacía inicializada
mi_lista = []
# Lista con nombres de frutas
frutas = ["manzana", "banana", "cereza"]

# Acceso a elementos: Acceder al segundo elemento de la lista 'frutas'
print(frutas[1])  # Imprime 'banana'

# Añadir elementos: Agregar 'naranja' al final de la lista
frutas.append("naranja")
print(frutas)  # Imprime la lista actualizada con 'naranja'

# Eliminar elementos: Eliminar 'banana' de la lista
frutas.remove("banana")
print(frutas)  # Imprime la lista después de eliminar 'banana'

# Iterar sobre la lista y imprimir cada fruta
for fruta in frutas:
    print(fruta)

print("------------")

# Diccionarios
# Diccionario vacío inicializado
mi_diccionario = {}
print(mi_diccionario)  # Imprime diccionario vacío

# Creación de un diccionario con información de una persona
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Coquimbo"
}
print(persona)  # Imprime el diccionario 'persona'

# Acceso a los elementos del diccionario por clave
print(persona['nombre'])  # Imprime 'Juan'
print(persona['edad'])    # Imprime 30
print(persona['ciudad'])  # Imprime 'Coquimbo'

# Modificar elementos: Cambiar la ciudad de 'Coquimbo' a 'Santiago'
persona['ciudad'] = "Santiago"
print(persona)  # Imprime el diccionario actualizado

# Añadir un nuevo par clave-valor al diccionario
persona['telefono'] = "98774121"
print(persona)  # Imprime el diccionario con el nuevo par añadido

# Eliminar el par clave-valor 'telefono'
del persona["telefono"]
print(persona)  # Imprime el diccionario después de eliminar el teléfono

# Iterar sobre las claves del diccionario e imprimir cada una
for x in persona:
    print(x)

print("------------")
# Iterar sobre los valores del diccionario e imprimir cada uno
for valor in persona.values():
    print(valor)

print("------------")
# Iterar sobre pares clave-valor del diccionario e imprimir cada uno
for clave, valor in persona.items():
    print(clave, valor)  # Imprime la clave y el valor

print("------------")
# Creación de una lista mediante comprensión de lista con números del 1 al 5
lista = [n for n in range(1, 6)]
print(lista)  # Imprime la lista creada

print("------------")
# Creación de una lista de números pares del 1 al 100 usando un bucle for
pares = [numero for numero in range(1, 101) if numero % 2 == 0]
print(pares)  # Imprime la lista de números pares
print("------------")
# Diccionario anidado con información de usuarios
diccionario_anidado = {
    "usuario_1": {
        "nombre": "Juan",
        "edad": 30,
        "ciudad": "Coquimbo"
    },
    "usuario_2": {
        "nombre": "Pedro",
        "edad": 41,
        "ciudad": "Calama"
    }
}
print(diccionario_anidado)  # Imprime el diccionario anidado

# Acceso a datos anidados: nombre del usuario_1
nombre_usuario1 = diccionario_anidado["usuario_1"]["nombre"]
print(nombre_usuario1)  # Imprime 'Juan'

print("------------")
# Imprime la edad del usuario_2
print(diccionario_anidado["usuario_2"]['edad'])

# Añadir una nueva clave-valor a usuario_1
diccionario_anidado["usuario_1"]["profesion"] = "Programador"
print(diccionario_anidado)  # Imprime el diccionario actualizado

print("------------")
# Diccionario de comprensión: Cuadrados de los números del 1 al 5
cuadrados_dict = {i: i ** 2 for i in range(1, 6)}
print(cuadrados_dict)  # Imprime el diccionario de cuadrados

print("------------")
# Diccionario delos números pares del 1 al 10
cuadrados_pares_dict = {i: i ** 2 for i in range(1, 11) if i % 2 == 0}
print(cuadrados_pares_dict)  # Imprime el diccionario de cuadrados de números pares

print("------------")
# Diccionario de comprensión para contar las ocurrencias de cada letra en una palabra
word = 'letterssssss'
letters_counts = {letter: word.count(letter) for letter in word}
print(letters_counts)  # Imprime las cuentas de cada letra en la palabra 'letterssssss'

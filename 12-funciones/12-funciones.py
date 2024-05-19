saluda = "Hola"  # Definición de una variable global

# Función sin parámetros que imprime un mensaje
def my_function():
    print("Esto es una funcion")

# Llamada a la función cuatro veces
my_function()
my_function()
my_function()
my_function()

# Función con parámetros que imprime la suma de dos valores
def sum_two_values(first_value: int, second_value: int):
    print(first_value + second_value)

# Ejemplos de uso de la función sum_two_values
sum_two_values(5, 7)  # Suma de dos enteros
sum_two_values(5414, 5452123)  # Suma de dos enteros grandes
sum_two_values(1.4, 5.2)  # Suma de dos flotantes
# sum_two_values("2", "7")  # Comentado porque causaría un error de tipo
# print("2" + 7 )  # Comentado porque causaría un error de tipo

print("-------")
my_result = sum_two_values(1, 5)  # No retorna nada, por lo tanto my_result es None
print(my_result)  # Imprime None
print("-------")

# Función que retorna la suma de dos valores
def sum_two_values_with_return(first_value: int, second_value: int):
    my_sum = first_value + second_value
    return my_sum

# Uso de la función con retorno
my_result = sum_two_values_with_return(10, 10)  # Esta vez retorna la suma
print(my_result)  # Imprime 20

# Función que imprime el nombre y apellido proporcionados
def print_name(name, surname):
    print(f"{name} {surname}")

# Llamada a la función usando parámetros con nombre
print_name(surname="Arnaez", name="Cesar")

print("-------")

# Función con parámetro por defecto
def print_name_with_default(name, surname, alias="Sin alias"):
    print(f"{name} {surname} {alias}")

# Ejemplos de uso de la función con y sin parámetro por defecto
print_name_with_default("Veronica", "Flores")  # Usa el alias por defecto
print_name_with_default("Luis", "Sanchez", "Lucho")  # Proporciona un alias personalizado

# Funciones que imprimen el cuadrado de un número específico
def dos_elevado_2():
    print(2**2)

def tres_elevado_2():
    print(3**2)

def cuatro_elevado_2():
    print(4**2)

# Llamada a las funciones de elevación
dos_elevado_2()  # Imprime 4
tres_elevado_2()  # Imprime 9
cuatro_elevado_2()  # Imprime 16

print("-------")

# Función general para elevar al cuadrado un número
def elevado_2(x):
    print(x**2)

# Ejemplos de uso de la función elevado_2
elevado_2(2)  # Imprime 4
elevado_2(3)  # Imprime 9
elevado_2(4)  # Imprime 16

print("-------")

# Función que eleva un número base a un exponente especificado
def elevar(base, exponente):
    print(base**exponente)

# Ejemplos de uso de la función elevar
elevar(2, 2)  # Imprime 4
elevar(3, 3)  # Imprime 27

# Uso de la función len() para obtener la longitud de una cadena y una lista
cadena = "Cadena"
lista = [1, 2, 3, 4, 5]
print(len(cadena))  # Imprime la longitud de la cadena
print(len(lista))  # Imprime la longitud de la lista

print("-------")

# Función con retorno prematuro
def prueba_return():
    a = "Esta línea se va a imprimir"
    b = "Esta línea no se va a imprimir"
    return a  # Punto de salida
    print(b)  # Nunca se ejecutará

print(prueba_return())  # Imprime "Esta línea se va a imprimir"

print("-------")
print("-------")
print("-------")

print(saluda)  # Imprime "Hola"

# Función que retorna el cuadrado y el cubo de un número
def cuadrado_cubo(base):
    cuadrado = base**2
    cubo = base**3
    return cuadrado, cubo  # Retorna una tupla con el cuadrado y el cubo

print(cuadrado_cubo(2))  # Imprime (4, 8)

print("-------")

# Listas de prueba
lista_numeros = [1, 2, 3, 4, 5]
lista_string = ['a', 'b', 'c', 'd', 'e']

# Función que acepta una lista y una función, y retorna los tipos de elementos en la lista y el resultado de aplicar la función a la lista
def sumar_contar_tipos(lista, funcion):
    tipos = [type(elemento) for elemento in lista]
    opcion = funcion(lista)
    return tipos, opcion

# Ejemplos de uso de la función sumar_contar_tipos
tipo, conteo = sumar_contar_tipos(lista_string, len)  # Usa len como función
print(tipo)  # Imprime los tipos de los elementos en lista_string
print(conteo)  # Imprime la longitud de lista_string

tipo, suma = sumar_contar_tipos(lista_numeros, sum)  # Usa sum como función
print(tipo)  # Imprime los tipos de los elementos en lista_numeros
print(suma)  # Imprime la suma de los elementos en lista_numeros

# Repetición de la definición de sum_two_values_with_return
def sum_two_values_with_return(first_value: int, second_value: int):
    my_sum = first_value + second_value
    return my_sum
# print(my_sum) No existe globalmente

# Ejemplo de uso del método items() en diccionarios
# Este método devuelve una vista de todos los pares clave-valor en el diccionario.
# pares = computador.items()
# print("Pares clave-valor:", pares)  # Muestra la vista de los pares clave-valor

# Convertir la vista a una lista
# lista_pares = list(pares)
# print("Lista de pares clave-valor:", lista_pares)  # Imprime: [('notebook', 489990), ('tablet', 120000), ('cargador', 12400)]

# Acceder a elementos específicos en la lista de pares clave-valor
# print("Primer par:", lista_pares[0])  # Imprime: ('notebook', 489990)
# print("Segundo par:", lista_pares[1])  # Imprime: ('tablet', 120000)
# print("Tercer par:", lista_pares[2])  # Imprime: ('cargador', 12400)

# args y kwargs


def f(*args):
    """
    Acepta un número variable de argumentos posicionales y los retorna como una tupla.

    Parámetros:
    *args: Argumentos posicionales variables.

    Retorna:
    tuple: Una tupla que contiene todos los argumentos posicionales.
    """
    return args

# Llamada a la función con diferentes tipos de argumentos
output = f(1, [2, 3], 'hola', {'clave': [4]})

# Imprime el tipo del objeto retornado, que será una tupla
print(type(output))  # <class 'tuple'>

# Imprime el contenido de la tupla
print(output)  # (1, [2, 3], 'hola', {'clave': [4]})

# https://www.programaenpython.com/avanzado/args-y-kwargs-en-python/

print("---")

def f(**kwargs):
    return kwargs

output = f(valor = 1, texto = 'hola', lista_nombres = [4,5,6,7])
print(type(output))
print(output)
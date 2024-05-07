# Variables

# Creación de una variable tipo string (cadena de texto)
mi_variable_string = "Mi      variable string"
print("Este es un string: ", mi_variable_string)  # Muestra el contenido de la variable string

# Creación de una variable tipo integer (entero)
mi_variable_integer = 5
print("Este es un integer", mi_variable_integer)  # Muestra el valor entero

# Conversión de un integer a string
my_variable_integer_a_string = str(45)  # Convierte el número 45 en cadena de texto
print(my_variable_integer_a_string)  # Muestra la cadena "45"

# Creación de una variable tipo booleana (boolean)
mi_variable_booleana = False
print(mi_variable_booleana)  # Muestra el valor booleano False

# Concatenación de variables en un print
print(mi_variable_string, mi_variable_integer, my_variable_integer_a_string)  # Muestra las tres variables en una sola línea

# Uso de la función len() para contar caracteres en un string
print(len(mi_variable_string))  # Muestra el número de caracteres en mi_variable_string, incluyendo espacios

# Asignación múltiple de variables
name, apellido, pais = "Eduardo", "Farias", "Chile"  # Asigna valores a tres variables simultáneamente
print("Me llamo", name, apellido, "y vivo en", pais)  # Muestra los valores de las variables name, apellido y pais

# Tipado estático en Python (opcional, soportado por Python 3.6 en adelante)
direccion: str = 5  # Declaración de tipo con anotación, asigna el entero 5 a una variable que se sugiere debe ser un string
print(direccion)  # Muestra el valor de la variable direccion

# La sección comentada de input está destinada a recoger datos del usuario, desbloquela para experimentar su funcionamiento
# input_name = input('¿Cuál es tu nombre?')
# input_surname = input('¿Cuál es tu apellido?')
# print(input_name)
# print(input_surname)

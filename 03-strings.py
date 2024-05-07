####### Strings ######

# Definir variables utilizando la convención snake_case
my_string = 'Mi String'
my_other_string = 'Mi otro String'

# La función 'len()' devuelve la longitud de una cadena
print(len(my_string))

# Formatear strings usando f-string, una forma moderna y legible de incorporar variables en strings
name, surname, age = "Juan", "Russo", 35

# Concatenar strings usando el operador '+', y convertir números a strings con 'str()'
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))

# Formato más limpio usando f-string, que automáticamente convierte las variables a strings
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Slicing / División de cadenas
language = 'python'

# P   Y   T   H   O   N
# 0   1   2   3   4   5
# -6  -5  -4  -3  -2  -1

# Tomar partes de una cadena usando índices: start:stop:step
language_slice = language[0:6:2]  # Toma cada segundo carácter desde el inicio hasta el final
print(language_slice)

# Ingreso de datos del usuario
correo = input('Ingrese correo electrónico: ')

# Función para obtener el nombre de usuario de una dirección de correo electrónico
def obtener_nombre_usuario(correo_electronico):
    # Buscar la posición del carácter '@'
    indice_arroba = correo_electronico.find("@")
    # Si '@' no está presente, lanzar un error
    if indice_arroba == -1:
        raise ValueError("Correo electrónico no válido: no se encontró el carácter '@'")
    # Tomar la porción de la cadena desde el inicio hasta el carácter '@'
    nombre_usuario = correo_electronico[:indice_arroba]
    return nombre_usuario

# Uso de la función para obtener y mostrar el nombre de usuario
nombre_usuario = obtener_nombre_usuario(correo)
print(f"Nombre de usuario: {nombre_usuario}")





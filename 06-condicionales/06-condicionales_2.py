# Conditional Steps - Pasos condicionales

# Definimos una variable 'numero' y le asignamos el valor 5
numero = 5

# Usamos una condición para verificar si 'numero' es menor que 10
if numero < 10:
    print('Es menor')  # Si la condición es verdadera, imprime 'Es menor'

# Usamos otra condición para verificar si 'numero' es mayor que 20
if numero > 20:
   print('Es mayor')  # Esta condición es falsa, por lo tanto no imprime nada

# Imprime el mensaje al finalizar las condiciones
print('Final del programa')

# Serie de condiciones para verificar distintos casos con 'numero'
if numero == 5:
    print('Igual a 5')  # Verifica si 'numero' es igual a 5
if numero > 4:
   print('Mayor que 4')  # Verifica si 'numero' es mayor que 4
if numero >= 5:
    print('Mayor o igual a 5')  # Verifica si 'numero' es mayor o igual a 5
if numero < 6:
    print('Menor que 6')  # Verifica si 'numero' es menor que 6

# Verifica si 'numero' es menor o igual a 5
if numero <= 5:
    print('Menor o igual a 5')
# Verifica si 'numero' no es igual a 6
if numero != 6:
    print('No es igual 6')

# Definimos una variable 'x' y le asignamos el valor 5
x = 5
print('Antes de 5')
# Condición que verifica si 'x' es igual a 5
if x == 5:
    print('Es 5')  # Como 'x' es 5, imprime 'Es 5'
    print('Aun es 5')  # También imprime 'Aun es 5'
    print('Esta tambien es 5')  # Y esta línea también se imprime
print('Despues de 5')

print('Antes de 6')
# Condición que verifica si 'x' es igual a 6
if x == 6:
    print('Es 6')  # No se imprime porque 'x' no es 6
    print('Aun es 6')  # No se imprime
    print('Esta tambien es 6')  # No se imprime
print('Despues de 6')  # Se imprime porque está fuera del bloque condicional
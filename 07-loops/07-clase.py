# Este script demuestra el uso de bucles en Python para diferentes propósitos

cadena = "Hola-Mundo"  # Define una cadena de caracteres

# Uso de un bucle for para iterar sobre cada caracter en la cadena
index = 0  # Inicializa el índice
for item in cadena:
    print(index, item)  # Imprime el índice y el caracter
    index += 1  # Incrementa el índice

# Uso de un bucle while para realizar un número fijo de iteraciones
estado = True  # Condición inicial para el bucle while
iteracion = 1  # Contador de iteraciones
while estado:  # El bucle se ejecuta mientras estado sea True
    print(f"Este es la iteracion: {iteracion}")  # Imprime el número de iteración
    iteracion += 1  # Incrementa el contador de iteraciones
    if iteracion > 3:  # Condición para terminar el bucle
        estado = False  # Establece estado a False para salir del bucle

print('El bucle ha terminado')  # Mensaje al finalizar el bucle

# Bucle while que decrementa un contador partiendo desde 100
i = 100  # Inicio del contador
while i > 0:
    print(f"Esta es la repeticion numero: {i}")  # Imprime el valor del contador
    i -= 2  # Decrementa el contador en 2

# Bucle while que nunca se ejecuta porque la condición inicial es falsa
i = 0  # Inicio del contador
while i > 100:  # Esta condición es falsa inicialmente
    print(f"Esta es la repeticion numero: {i}")  # Imprime el valor del contador
    i += 2  # Incrementa el contador en 2

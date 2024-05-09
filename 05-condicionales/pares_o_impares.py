"""
Este programa  determina si un numero es par o no de un número ingresado 
por el usuario.

Proceso del programa:
1. Solicita al usuario que ingrese un número entero. Si el número ingresado es cero, el programa solicita
   al usuario que ingrese un nuevo número hasta que sea diferente de cero.
2. Una vez ingresado un número válido, el programa evalúa si el número es par o impar.
3. Imprime el resultado indicando si el número es par o impar.
4. Maneja cualquier error que ocurra si el usuario no ingresa un número entero, proporcionando un mensaje
   de error adecuado y solicitando una nueva entrada.
5. Finaliza con un mensaje que indica el fin del programa.

El programa utiliza estructuras de control de flujo como 'try-except' para manejar excepciones, y 'if-else'
para determinar la paridad del número ingresado. También implementa un bucle 'while' para garantizar que el usuario
no pueda proceder con un cero como entrada.
"""

# Paso 1: Solicitar al usuario que ingrese un número
try:
    valor = int(input("Ingresa el valor a probar: "))

    # Paso 2: Verificar si el valor ingresado es cero y pedir otro número en ese caso
    while valor == 0: 
        print("Este número es cero, inténtalo nuevamente.")
        valor = int(input("Ingresa el valor a probar: "))

    # Paso 3: Determinar si el número es par o impar
    if valor % 2 == 0:
        print("Este número es par")
    else:
        print("Este es un número impar")

# Captura de errores en caso de que la entrada no sea un entero válido
except ValueError:
    print("Revisar los datos ingresados, por favor ingrese un número entero.")

# Mensaje final del programa
print("Fin del programa")



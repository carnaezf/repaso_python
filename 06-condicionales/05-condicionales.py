# Bloque IF
condicion = 1
if condicion:
    # Ejecutar un codigo
    print('Este bloque se ejecuto')
# Esta linea esta fuera fuera del bloque
print('Este script finaliza acá')


# edad = int(input("¿Qué edad tienes?"))

# if edad > 18:
#     print("Eres mayor de edad")
# elif edad == 18:
#     print("Tienes 18 años")
# else: 
#     print("Eres menor de edad")
# print('Finaliza el programa')


"""
Supongamos que queremos escribir un programa que evalue
la calificacion de un studiante:
 90 o igual a puntos: Excelente
 70 o igual a puntos: Buena
 50 o igual a puntos: Suficiente
 ninguna de esta condiciones: Insuficiente
"""
calificacion = 30

# Usaremos IF para vericicar la condicion
if calificacion >= 90:
    # Este bloque se ejecuta si la calificacion > 90.
    print("Excelente")
elif calificacion >= 70:
    # Este bloque se ejecuta si la calificacion > 90.
    print("Buena")
elif calificacion >= 50:
    # Este bloque se ejecuta si la calificacion > 90.
    print("Suficiente")
else:
    # Este bloque se ejecuta so las condiciones anteriores no se cumplen
    print("Insuficiente")
    print(1+1)
    print(True)

# Final del programa
print("Evaluacion completa")


























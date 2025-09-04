"""
Realizar un programa que permita mostrar una pirámide de números. 
Por ejemplo: si se ingresa el numero 5, la salida del programa será la siguiente:

1
12
123
1234
12345
"""

cantidad_iteraciones_str = input('Dime la cantidad de pisos de la piramide: ')
cantidad_iteraciones = int(cantidad_iteraciones_str)

cadena_inicial = ''
for numero_actual in range(cantidad_iteraciones): # 5
    numero_imprimible = numero_actual + 1
    cadena_inicial = f'{cadena_inicial}{numero_imprimible}'
    print(cadena_inicial)

cantidad_iteraciones_str = input('Dime la cantidad de pisos de la piramide: ')
cantidad_iteraciones = int(cantidad_iteraciones_str)

cadena_inicial = ''
for numero_actual in range(1, cantidad_iteraciones + 1, 1):
    cadena_inicial = f'{cadena_inicial}{numero_actual}'
    print(cadena_inicial)

print(numero_actual)
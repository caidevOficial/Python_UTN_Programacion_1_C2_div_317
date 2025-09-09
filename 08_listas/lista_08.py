
import random as rd

def crear_lista_con_tantos_numeros(numero: int):
    lista_numeros = []

    for indice in range(numero):
        nuevo_numero = rd.randint(1, 10)
        lista_numeros.append(nuevo_numero)
    return lista_numeros
    
"""
Escribir una función que reciba como parámetros una 
lista de enteros y muestre la/las posiciones 
en donde se encuentra el valor máximo hallado.
"""

def buscar_numero_mayor(lista_numeros: list) -> int:

    numero_mayor = None

    for indice in range(len(lista_numeros)):
        
        numero_actual = lista_numeros[indice]
        if numero_mayor == None or numero_mayor < numero_actual:
            numero_mayor = numero_actual
    
    return numero_mayor

def buscar_indices_mayores(lista_numeros: list) -> list:
    numero_mayor = buscar_numero_mayor(lista_numeros)
    lista_indices_mayores = []

    for indice in range(len(lista_numeros)):
        numero_actual = lista_numeros[indice]
        if numero_actual == numero_mayor:
            lista_indices_mayores.append(indice)
    return lista_indices_mayores


# ======================================

cantidad_elementos = input('Lista de X elementos: ')
cantidad_elementos = int(cantidad_elementos)

lista_num = crear_lista_con_tantos_numeros(cantidad_elementos)
indices_num_maximo = buscar_indices_mayores(lista_num)

print(f'Lista: {lista_num}')
print(f'Lista indices num mayores: {indices_num_maximo}')

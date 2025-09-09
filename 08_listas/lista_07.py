"""
Desarrollar una función que permita 
crear un array de números con la cantidad de 
elementos que establezca el parámetro recibido.
"""

def crear_lista_con_tantos_numeros(numero: int):
    lista_numeros = []

    for indice in range(numero):
        nuevo_numero = indice + 1
        lista_numeros.append(nuevo_numero)

    return lista_numeros


numero_str = input('Cuantos numeros para la lista: ')
numero = int(numero_str)
numeros = crear_lista_con_tantos_numeros(numero)
print(f'Cantidad elementos: {len(numeros)} -> {numeros}')
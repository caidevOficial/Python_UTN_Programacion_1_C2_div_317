"""
Implementar una función llamada reemplazar_nombres que reciba los siguientes parámetros:
- Una lista de nombres (lista_nombres).
- Un nombre a buscar en la lista (nombre_antiguo).
- Un nombre de reemplazo (nombre_nuevo).

La función debe realizar las siguientes acciones:
Reemplazar todas las apariciones de nombre_antiguo en lista_nombres por nombre_nuevo.
Retornar la cantidad total de reemplazos realizados.
"""

def reemplazar_nombre(lista_nombres: list, valor_nuevo: str, indice: int):
    lista_nombres[indice] = valor_nuevo

def reemplazar_nombres(lista_nombres: list, nombre_viejo: str, nombre_nuevo: str) -> int:
    cantidad_cambios = 0

    for indice in range(len(lista_nombres)):
        elemento_actual = lista_nombres[indice]
        if elemento_actual == nombre_viejo:
            reemplazar_nombre(lista_nombres, nombre_nuevo, indice)
            cantidad_cambios += 1
    return cantidad_cambios



lista_nombres = [
    "homero", "marge", "lisa", "maggie", "el muchacho","lisa","lisa","lisa","lisa","lisa" 
]

lista_num_a = [
    1,2,3,4,5,6
]

lista_num_b = [
    4,5,6,7,8,9,10
]


nombre_viejo = input('Que nombre de la lista quiere reemplazar? ')
nombre_nuevo = input('Con que lo quiere reemplazar? ')

cambios = reemplazar_nombres(lista_nombres, nombre_viejo=nombre_viejo, nombre_nuevo=nombre_nuevo)
print(f'Se realizaron {cambios} cambios!')
print(lista_nombres)
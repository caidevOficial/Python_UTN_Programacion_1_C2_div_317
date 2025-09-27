
def buscar_indices_de_elementos(precios: list, promedio: float) -> list:
    indices_encontrados = []
    for indice_elemento in range(len(precios)):
        if precios[indice_elemento] < promedio:
            indices_encontrados.append(indice_elemento)
    return indices_encontrados


def tu_funcion(nombre_lista: str, marcas: list, modelos: list, cantidades: list,precios: list,indice: int):
    match nombre_lista:
        case 'marca':
            elemento = marcas[indice]
            return elemento
        case 'modelo':
            elemento = modelos[indice]
            return elemento
        case 'cantidad':
            elemento = cantidades[indice]
            return elemento
        case 'precio':
            elemento = precios[indice]
            return elemento

def obtener_elemento_de_indice(lista_autos: list, indice: int) -> any:
    return lista_autos[indice]


# ejemplo de llamado a la funcion
from utn_fra.datasets import (
    lista_autos_cantidades, lista_autos_marcas,
    lista_autos_modelos, lista_autos_precios
)
promedio = 15321.22 # promedio de ejemplo

indices = buscar_indices_de_elementos(lista_autos_precios, promedio)

for indice in indices:
    marca = obtener_elemento_de_indice(lista_autos_marcas, indice)
    modelo = obtener_elemento_de_indice(lista_autos_modelos, indice)
    precio = obtener_elemento_de_indice(lista_autos_precios, indice)
    cantidad = obtener_elemento_de_indice(lista_autos_cantidades, indice)

    print(f'FOUND -> {marca}, {modelo}, ${precio}, {cantidad} un.')

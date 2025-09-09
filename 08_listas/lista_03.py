


def suma_de_lista(lista_numeros: list):
    suma = 0
    cantidad = len(lista_numeros)
    for indice in range(cantidad):
        suma += lista_numeros[indice]
    
    # for numero in lista_numeros:
    #     suma += numero

    return suma


def obtener_promedio_lista(lista_numeros: list):
    suma = suma_de_lista(lista_numeros)
    cantidad_elementos = len(lista_numeros)

    promedio = suma / cantidad_elementos

    return promedio



mi_lista_de_numeros = [
    10,2,5,9,4,20,35,50,42
]

suma = suma_de_lista(mi_lista_de_numeros)
promedio = obtener_promedio_lista(mi_lista_de_numeros)

print(f'La suma numerica de elementos es: {suma}')
print(f'El promedio numerico de elementos es: {promedio}')
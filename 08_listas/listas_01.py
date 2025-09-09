mi_lista_de_numeros = []
# mi_lista_de_numeros = list()

mi_lista_de_numeros = [
    10,2,5,9,4,20,35,50,42
]

cantidad = len(mi_lista_de_numeros)
for indice in range(cantidad):

    elemento = mi_lista_de_numeros[indice]
    print(f'Indice n° {indice} -> elemento: {elemento}')
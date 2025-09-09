mi_lista_de_numeros = []
# mi_lista_de_numeros = list()

mi_lista_de_numeros = [
    10,2,5,9,4,20,35,50,42
]

suma_total = 0
cantidad = len(mi_lista_de_numeros)
for indice in range(cantidad):

    elemento = mi_lista_de_numeros[indice]
    suma_total += elemento

    print(f'Indice n° {indice} -> elemento: {elemento}')

print(f'La suma total es: {suma_total}')
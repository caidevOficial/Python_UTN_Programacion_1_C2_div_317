color = []
COLOR_VERDE = (0, 255, 100)
COLOR_VERDE_2 = tuple([150, COLOR_VERDE[1], COLOR_VERDE[2]])
COORDENADA_ITEM = (50, 140)

matriz_tupla = (
    ("auto", "tren"),
    ("remera", "pantalon")
)


# for indice, valor in enumerate(matriz_tupla):
#     print(f'{indice} -> {valor}')


def una_funcion(mi_tupla: tuple):
    suma = 0
    for numero in mi_tupla:
        suma += numero
    return suma

suma = una_funcion(COLOR_VERDE_2)

print(suma)
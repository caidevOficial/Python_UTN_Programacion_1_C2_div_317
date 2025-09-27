

def sumar_matrices(matriz_1: list[list], matriz_2: list[list]) -> list[list]:

    matriz_r = []

    for indice_fila in range(len(matriz_1)):
        fila_resultado = []

        for indice_columna in range(len(matriz_1[indice_fila])):
            suma = matriz_1[indice_fila][indice_columna] +\
                    matriz_2[indice_fila][indice_columna]
            fila_resultado.append(suma)
        
        matriz_r.append(fila_resultado)
    return matriz_r

matriz_a = [
    [3, 8],
    [4, 6],
    [10, 20]
]

matriz_b = [
    [4, 0],
    [1, -9],
    [20, 10]
]

"""
Resultado esperado:
[
    [7, 8],
    [5, -3],
    [30, 30]
]
"""
matriz_r = sumar_matrices(matriz_a, matriz_b)
print(matriz_r)


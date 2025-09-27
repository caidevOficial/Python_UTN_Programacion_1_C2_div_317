
def multiplicar_matriz_por_escalar(matriz: list[list], escalar: int) -> list[list]:

    matriz_r = []
    for indice_fila in range(len(matriz)):
        fila_r = []
        for indice_col in range(len(matriz[indice_fila])):
            resultado = matriz[indice_fila][indice_col] * escalar
            fila_r.append(resultado)
        matriz_r.append(fila_r)
    return matriz_r


matriz_a = [
    [3, 8],
    [4, 6]
]

resultado = multiplicar_matriz_por_escalar(matriz_a, escalar=2)
print(resultado)
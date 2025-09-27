def order_selection(matriz: list[list], indice_a_ordenar: int) -> list[list]:

    for indice_col in range(len(matriz[indice_a_ordenar]) - 1):
        indice_elem_menor = indice_col

        for indice_sig_col in range(indice_col + 1, len(matriz[indice_a_ordenar])):
            if matriz[indice_a_ordenar][indice_elem_menor] > matriz[indice_a_ordenar][indice_sig_col]:
                indice_elem_menor = indice_sig_col
        
        if indice_elem_menor != indice_col:
            # Tengo que intercambiar todas las filas en esa columna
            for indice_fila in range(len(matriz)):

                elemento_aux = matriz[indice_fila][indice_elem_menor]
                matriz[indice_fila][indice_elem_menor] = matriz[indice_fila][indice_col]
                matriz[indice_fila][indice_col] = elemento_aux
    return matriz

def order_selection_2(matriz: list[list], indice_col_ordenar: int) -> list[list]:

    for indice_fila in range(len(matriz) - 1):
        indice_elem_menor = indice_fila

        for indice_sig_fila in range(indice_fila + 1, len(matriz)):
            if matriz[indice_elem_menor][indice_col_ordenar] > matriz[indice_sig_fila][indice_col_ordenar]:
                indice_elem_menor = indice_sig_fila
        
        if indice_elem_menor != indice_fila:
            fila_aux = matriz[indice_elem_menor]
            matriz[indice_elem_menor] = matriz[indice_fila]
            matriz[indice_fila] = fila_aux
    return matriz


def crear_matriz_t(matriz: list) -> list[list]:
    matriz_t = []

    cant_col = len(matriz[0])

    for indice_col in range(cant_col):
        nueva_fila = []

        for indice_fila in range(len(matriz)):
            nueva_fila.append(matriz[indice_fila][indice_col])
        matriz_t.append(nueva_fila)
    
    return matriz_t

mi_matriz = [
    ["Pepe", "Moni", "Fatiga"],
    [54, 45, 12],
    [1.70, 1.60 , 0.80]
]

mi_matriz_2 = [
    ["Pepe", 54, 1.7],
    ["Moni", 45, 1.6],
    ["Dardo", 50, 1.85],
    ["Fatiga", 12, 0.8],
]


# mi_matriz_2 = crear_matriz_t(mi_matriz_2)
# order_selection(mi_matriz_2, 1)
order_selection_2(mi_matriz_2, 2)
# mi_matriz_2 = crear_matriz_t(mi_matriz_2)


print(mi_matriz_2)
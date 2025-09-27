

mi_matriz = [
    ["Pepe", "Moni", "Fatiga"],
    [54, 45, 12],
    [1.70, 1.60 , 0.80]
]


cantidad_col = len(mi_matriz[0])

# recorro primero las columnas
for indice_columna in range(cantidad_col):
    
    # recorrer las filas por cada columna
    for indice_fila in range(len(mi_matriz)):

        print(mi_matriz[indice_fila][indice_columna], end=' ')
    print('')
from utn_fra.datasets import matriz_data_heroes_small


def order_selection(matriz: list[list], indice_a_ordenar: int, tipo_orden: str) -> list[list]:

    for indice_col in range(len(matriz[indice_a_ordenar]) - 1):
        indice_elem_menor = indice_col

        for indice_sig_col in range(indice_col + 1, len(matriz[indice_a_ordenar])):
            if (matriz[indice_a_ordenar][indice_elem_menor] > matriz[indice_a_ordenar][indice_sig_col] and tipo_orden == 'ASC') or\
                (matriz[indice_a_ordenar][indice_elem_menor] < matriz[indice_a_ordenar][indice_sig_col] and tipo_orden == 'DES'):
                indice_elem_menor = indice_sig_col
        
        if indice_elem_menor != indice_col:
            # Tengo que intercambiar todas las filas en esa columna
            for indice_fila in range(len(matriz)):

                elemento_aux = matriz[indice_fila][indice_elem_menor]
                matriz[indice_fila][indice_elem_menor] = matriz[indice_fila][indice_col]
                matriz[indice_fila][indice_col] = elemento_aux
    return matriz

def mostrar_datos(matriz: list[list]):
    # id,nombre,tipo,poder,condición
    cant_columnas = len(matriz[0])

    texto = 'nombre,vistas,duraciones,canti_simbolo\n\n'
    for indice_columna in range(cant_columnas):

        dato = ''
        for indice_fila in range(len(matriz)):
            dato = f'{dato}{matriz[indice_fila][indice_columna]}'
            
            if indice_fila < len(matriz) - 1:
                dato = f'{dato},'
        
        texto += f'{dato}\n'
    print(texto)

def order_selection_T(matriz: list[list], indice_col_ordenar: int) -> list[list]:

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

def crear_matriz_t(matriz: list) -> list[tuple]:
    matriz_t = []

    cant_col = len(matriz[0])

    for indice_col in range(cant_col):
        nueva_fila = []

        for indice_fila in range(len(matriz)):
            nueva_fila.append(matriz[indice_fila][indice_col])
        matriz_t.append(tuple(nueva_fila))
    
    return matriz_t

def obtener_datos_fila(matriz: list, indice_fila: int) -> str:
    fila_actual = matriz[indice_fila]
    mensaje_fila = ''
    for indice_col in range(len(fila_actual)):
        mensaje_fila = f'{mensaje_fila} | {fila_actual[indice_col]:7}'
    mensaje_fila = f'{mensaje_fila} |\n'

    return mensaje_fila

def mostrar_datos_matriz(matriz: list):
    mensaje_matriz = ''

    for indice_fila in range(len(matriz)):
        mensaje_fila = obtener_datos_fila(matriz, indice_fila)
        mensaje_matriz = f'{mensaje_matriz}{mensaje_fila}'
    
    print(mensaje_matriz)

import copy
# matriz_copia = copy.deepcopy(matriz_data_heroes_small)

matriz_o_t = crear_matriz_t(matriz_data_heroes_small)

matriz_c_t = matriz_o_t.copy()

"""
matriz_1 = [
    ["nombre_1", "Nombre_2"],
    [24, 8]
]

matriz_2 = [
    ["nombre_1", 24],
    ["nombre_2", 8]
]

"""

order_selection_T(matriz_c_t, 4)
mostrar_datos_matriz(matriz_c_t)
print()
mostrar_datos_matriz(matriz_o_t)
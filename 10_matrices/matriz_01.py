# mi_matriz = [
#     [1,3,5],
#     [2,4,6],
#     [7,8,9]
# ]


# # Este primer bucle lo usamos para recorrer las filas de la matriz
# mensaje_matriz = ''
# for indice_fila in range(len(mi_matriz)):
#     fila_actual = mi_matriz[indice_fila]
#     mensaje_fila = ''
#     for indice_columna in range(len(fila_actual)):

#         mensaje_fila = f'{mensaje_fila} | {mi_matriz[indice_fila][indice_columna]}'
#     mensaje_matriz = f'{mensaje_matriz}{mensaje_fila} |\n'

# print(mensaje_matriz)

def obtener_datos_fila(matriz: list, indice_fila: int) -> str:
    fila_actual = matriz[indice_fila]
    mensaje_fila = ''
    for indice_col in range(len(fila_actual)):
        mensaje_fila = f'{mensaje_fila} | {fila_actual[indice_col]:7}'
    mensaje_fila = f'{mensaje_fila} |\n'

    return mensaje_fila

def mostrar_datos_matriz(matriz: list):
    mensaje_matriz = ' | Nombres | Edades  | Alturas |\n'\
                    ' _____________________________\n'

    for indice_fila in range(len(matriz)):
        mensaje_fila = obtener_datos_fila(matriz, indice_fila)
        mensaje_matriz = f'{mensaje_matriz}{mensaje_fila}'
    
    print(mensaje_matriz)


# recorrido F x C
mi_matriz = [
    ["Pepe", "Moni", "Fatiga"],
    [54, 45, 12],
    [1.70, 1.60 , 0.80]
]

mi_matriz_2 = [
    ["Pepe", 54, 1.7],
    ["Moni", 45, 1.6],
    ["Fatiga", 12, 0.8],
]

# fila = int(input('indique el indice de fila a modificar: '))
# columna = int(input('indique el indice de columna a modificar: '))
# dato = input('Que dato nuevo quiere agregar?: ')


# if fila > len(mi_matriz) - 1 or columna > len(mi_matriz[fila]) - 1:
#     print('Te pasaste con las filas o las columnas')
# else:
#     mi_matriz[fila][columna] = dato

mostrar_datos_matriz(mi_matriz)
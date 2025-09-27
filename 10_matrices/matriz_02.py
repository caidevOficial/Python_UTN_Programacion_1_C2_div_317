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

def crear_matriz_de_dimension(alto: int, ancho: int, valor: str) -> list[list]:
    matriz = []

    for fila in range(alto):
        fila_actual = []
        for columna in range(ancho):
            fila_actual.append(valor)
        matriz.append(fila_actual)
    
    return matriz

def crear_matriz_nula():
    return crear_matriz_de_dimension(alto=3, ancho=3, valor=0)

matriz = crear_matriz_nula()
mostrar_datos_matriz(matriz)
# print(matriz)
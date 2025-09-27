
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
    ["Pepe", "Moni", "Fatiga", "Moni"],
    [54, 45, 12, 45],
    [1.70, 1.60 , 0.80, 1.63]
]

matriz_t = crear_matriz_t(mi_matriz)
mostrar_datos_matriz(matriz_t)

que_buscar = float(input('Ingrese un nombre a buscar: '))
matriz_coordenadas = []

for indice_fila in range(len(matriz_t)):

    for indice_columna in range(len(matriz_t[indice_fila])):

        if matriz_t[indice_fila][indice_columna] == que_buscar:
            celda_encontrada = [indice_fila, indice_columna]
            matriz_coordenadas.append(celda_encontrada)


for coordenada in matriz_coordenadas:

    indice_f = coordenada[0]
    indice_c = coordenada[1]

    print(f'Encontre {que_buscar} en la fila {indice_f} y columna {indice_c}')



# mostrar_datos_matriz(matriz_t)
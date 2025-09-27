
def crear_matriz(filas: int, columnas: int, valor: str) -> list[list]:
    matriz = []

    for fila in range(filas):
        fila_actual = [valor] * columnas
        matriz.append(fila_actual)
    return matriz
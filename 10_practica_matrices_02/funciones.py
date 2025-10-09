
def crear_matriz(lista_a, lista_b, lista_c, lista_d):
    """
    
    """

    mi_matriz = [
        lista_a, 
        lista_b, 
        lista_c, 
        lista_d
    ]

    return mi_matriz


def obtener_existencias (matriz: list[list]) -> int:
    return len(matriz[0])

def mostrar_datos(matriz: list[list]):
    cant_columna = len(matriz[0])

    for indice_columna in range(cant_columna):

        datos = ""

        for indice_fila in range(len(matriz)):
            datos = f"{datos}{matriz[indice_fila][indice_columna]}"

            if indice_fila < len(matriz) - 1:
                datos = f"{datos}, "

        print(datos)

def sacar_promedio(matriz, indice_fila):
    suma_alturas = 0
    cantidad = obtener_existencias(matriz)

    for personaje in matriz[indice_fila]:
        print(personaje)
        suma_alturas += int(personaje)
    
    promedio = suma_alturas / cantidad

    return promedio

def filtrar_personaje(matriz, indice_fila, genero):

    promedio = sacar_promedio(matriz, indice_fila)
    
    for indice_columna in range(len(matriz[indice_fila])):
        if promedio > int(matriz[indice_fila][indice_columna]):
            if matriz[1][indice_columna] == genero:
                for in_fila in range(len(matriz)):
                    print(matriz[in_fila][indice_columna], end=" ")
                

        print("")


"""
Ordenar Female: Ordenar la matriz según altura DES los personajes que sean “female”
"""

def order_selection(matriz: list[list], indice_a_ordenar: int, tipo_orden: str) -> list[list]:

    for indice_col in range(len(matriz[indice_a_ordenar]) - 1):
        indice_elem_menor = indice_col

        for indice_sig_col in range(indice_col + 1, len(matriz[indice_a_ordenar])):
            if (int(matriz[indice_a_ordenar][indice_elem_menor]) > int(matriz[indice_a_ordenar][indice_sig_col])and tipo_orden == 'ASC') or\
                (int(matriz[indice_a_ordenar][indice_elem_menor]) < int(matriz[indice_a_ordenar][indice_sig_col])and tipo_orden == 'DES'):
                indice_elem_menor = indice_sig_col
        
        if indice_elem_menor != indice_col:
            # Tengo que intercambiar todas las filas en esa columna
            for indice_fila in range(len(matriz)):

                elemento_aux = matriz[indice_fila][indice_elem_menor]
                matriz[indice_fila][indice_elem_menor] = matriz[indice_fila][indice_col]
                matriz[indice_fila][indice_col] = elemento_aux
    return matriz

def ordenar_matriz_segun_genero(matriz: list[list], indice_a_ordenar: int, genero: str, modo: str = 'ASC'):

    cantidad_col = obtener_existencias(matriz)
    order_selection(matriz, indice_a_ordenar, modo)

    for indice_columna in range(cantidad_col):

        if matriz[1][indice_columna] == genero:
            for in_fila in range(len(matriz)):
                    print(matriz[in_fila][indice_columna], end=" ")
            print('')


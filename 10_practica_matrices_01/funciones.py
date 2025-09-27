
def crear_matriz(lista_poke_ids, lista_poke_nombres,
                lista_poke_tipos, lista_poke_poderes,
                lista_poke_condiciones):
    matriz = [
        lista_poke_ids, 
        lista_poke_nombres,
        lista_poke_tipos, 
        lista_poke_poderes,
        lista_poke_condiciones
    ]
    return matriz

def obtener_existencias(matriz: list[list]) -> int:
    return len(matriz[0])


def mostrar_datos(matriz: list[list]):
    # id,nombre,tipo,poder,condición
    cant_columnas = len(matriz[0])

    for indice_columna in range(cant_columnas):

        dato = ''

        for indice_fila in range(len(matriz)):
            dato = f'{dato}{matriz[indice_fila][indice_columna]}'
            
            if indice_fila < len(matriz) - 1:
                dato = f'{dato},'
        
        print(dato)

def obtener_promedio(matriz: list[list], indice_a_buscar: int) -> float:
    cantidad_elementos = len(matriz[0])
    suma_dato = 0

    for numero in matriz[indice_a_buscar]:
        suma_dato += numero
    
    if cantidad_elementos < 1:
        return 0
    
    promedio = suma_dato / cantidad_elementos
    return promedio

def obtener_indices(matriz: list[list], indice_a_buscar: int, valor_a_buscar: float):
    lista_indices_encontrados = []

    for indice in range(len(matriz[indice_a_buscar])):
        if matriz[indice_a_buscar][indice] > valor_a_buscar:
            lista_indices_encontrados.append(indice)

    return lista_indices_encontrados

def obtener_matriz_filtrada(matriz: list[list], lista_indices: list[int]):
    matriz_filtrada = [
        [],
        [],
        [],
        [],
        [],
    ]

    for indice in lista_indices:
        for indice_fila in range(len(matriz)):

            dato = matriz[indice_fila][indice]
            matriz_filtrada[indice_fila].append(dato)
    return matriz_filtrada


def mapear_valor(dato: str):
    indice = None
    match dato:
        case 'id':
            indice = 0
        case 'nombre':
            indice = 1
        case 'tipo':
            indice = 2
        case 'poder':
            indice = 3
        case 'condicion':
            indice = 4
    return indice
        
def mostrar_pokemones_poder_superior_promedio(matriz: list[list]):
    indice_seleccionadio = mapear_valor('poder')
    promedio = obtener_promedio(matriz, indice_seleccionadio)
    lista_indices = obtener_indices(matriz, indice_seleccionadio, promedio)
    matriz_filtrada = obtener_matriz_filtrada(matriz, lista_indices)
    
    print(f'El promedio de poder es: {promedio}\n\n')
    mostrar_datos(matriz_filtrada)

    # informe = f'El promedio de poder es: {promedio}\n\n'
    # for indice in lista_indices:
    #     id = matriz[0][indice]
    #     nombre = matriz[1][indice]
    #     tipo = matriz[2][indice]
    #     poder = matriz[3][indice]
    #     condicion = matriz[4][indice]

    #     mensaje =\
    #     f"""{id},{nombre},{tipo},{poder:.2f},{condicion}\n"""
    #     informe = f"{informe}{mensaje}"
    # print(informe)

def obtener_indices_que_cumplen(matriz: list[list], indice_a_buscar: int, valor_a_buscar: str):
    lista_indices_encontrados = []

    for indice in range(len(matriz[indice_a_buscar])):
        if matriz[indice_a_buscar][indice] == valor_a_buscar:
            lista_indices_encontrados.append(indice)

            # opcional: recorremos las filas de la matriz
            # para crearnos una matriz auxiliar filtrada

    return lista_indices_encontrados

def mostrar_pokemones_tipo(matriz: list[list], dato: str, valor: str):
    indice_seleccionadio = mapear_valor(dato)
    lista_indices = obtener_indices_que_cumplen(matriz, indice_seleccionadio, valor)
    matriz_filtrada = obtener_matriz_filtrada(matriz, lista_indices)
    
    print(f'Pkemones de tipo: {valor}\n\n')
    mostrar_datos(matriz_filtrada)

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

def filtrar_ordenar_pokemones(matriz: list[list], dato: str, valor: str, tipo_orden: str = 'ASC'):
    indice_seleccionadio = mapear_valor(dato)
    lista_indices = obtener_indices_que_cumplen(matriz, indice_seleccionadio, valor)
    matriz_filtrada = obtener_matriz_filtrada(matriz, lista_indices)
    
    indice_sort = mapear_valor('poder')
    order_selection(matriz_filtrada, indice_sort, tipo_orden)
    
    print(f'Pkemones de tipo: {valor}\n\n')
    mostrar_datos(matriz_filtrada)

def crear_matriz_t(matriz: list) -> list[list]:
    matriz_t = []

    cant_col = len(matriz[0])

    for indice_col in range(cant_col):
        nueva_fila = []

        for indice_fila in range(len(matriz)):
            nueva_fila.append(matriz[indice_fila][indice_col])
        matriz_t.append(nueva_fila)
    
    return matriz_t

def mostrar_datos_t(matriz: list[list]):
    # id,nombre,tipo,poder,condición
    # cant_columnas = len(matriz[0])

    # for indice_columna in range(cant_columnas):

    #     dato = ''

    #     for indice_fila in range(len(matriz)):
    #         dato = f'{dato}{matriz[indice_fila][indice_columna]}'
            
    #         if indice_fila < len(matriz) - 1:
    #             dato = f'{dato},'
        
    #     print(dato)
    print('MATRIZ T')
    for fila in matriz:
        dato = ''
        for columna in fila:
            dato = f'{dato}{columna}'

            if fila.index(columna) < len(fila) - 1:
                dato = f'{dato},'
        print(dato)


def trasponer_mostrar_matriz(matriz: list[list]):
    matriz_t = crear_matriz_t(matriz)
    mostrar_datos_t(matriz_t)
from utn_fra.datasets import (
    	lista_nombres_videos_small,
        lista_vistas_videos_small,
        lista_duraciones_videos_small
 )

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

"""
Ordenar por cantidad de hashtags (“#”) : 
    Ordenar la matriz según la cantidad de hashtags 
    que tengan  los nombres de los videos de modo DES.
"""

matriz_paulina = [
    lista_nombres_videos_small,
    lista_vistas_videos_small,
    lista_duraciones_videos_small
]

def mapear_valor(texto: str):
    """
    Mapea segun numeros de indices:

    Args:
        nombres -> 0
        vistas -> 1
        duraciones -> 2


    """
    match texto:
        case 'nombres':
            return 0
        case 'vistas':
            return 1
        case 'duraciones':
            return 2

def obtener_cantidad_tags_nombre(texto: str, simbolo: str = '#') -> int:
    cantidad_tags = 0

    for character in texto:
        if character == simbolo:
            cantidad_tags += 1
    return cantidad_tags

def adicionar_fila_a_matriz(matriz: list[list], simbolo: str = '#') -> list[list]:

    matriz_auxiliar = []
    lista_cantidad_tags = []

    lista_nombres = matriz[0]
    
    for nombre in lista_nombres:
        cantidad_tags = obtener_cantidad_tags_nombre(nombre, simbolo)
        lista_cantidad_tags.append(cantidad_tags)

    for fila in matriz:
        matriz_auxiliar.append(fila)
    matriz_auxiliar.append(lista_cantidad_tags)
    
    
    return matriz_auxiliar

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

def ordenar_segun_elementos_nombres(matriz: list[list], simbolo: str = '#'):

    matriz_aux = adicionar_fila_a_matriz(matriz, simbolo)

    order_selection(matriz_aux, 3, tipo_orden='DES')
    
    # matriz_aux.pop(-1)
    mostrar_datos(matriz_aux)

# ordenar_segun_elementos_nombres(matriz_paulina, simbolo='a')


"""
Trasponer Datos: Trasponer la matriz y mostrar su información 
prolija con una función que acepte ese tipo de matriz, 
además debe estar ordenada por vistas DES
"""

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
    print('MATRIZ T')
    texto = 'NOMBRE,VISTAS,DURACIÓN\n\n'
    for fila in matriz:
        dato = ''
        for columna in fila:
            dato = f'{dato}{columna}'

            if fila.index(columna) < len(fila) - 1:
                dato = f'{dato},'
        texto += f'{dato}\n'
    print(texto)

"""
matriz = [
    [NOMBRE2, VISTAS, DURACION],
    [NOMBRE1, VISTAS, DURACION],
    [NOMBRE4, VISTAS, DURACION],
    [NOMBRE5, VISTAS, DURACION],
    [NOMBRE3, VISTAS, DURACION],
]

"""



def ordenar_selection_t(matriz_t: list[list], in_columna_a_ordenar: int):

    for indice_fila in range(len(matriz_t) - 1 ):
        indice_mayor_elemento = indice_fila

        for indice_sig_fila in range(indice_fila + 1, len(matriz_t)):

            if matriz_t[indice_mayor_elemento][in_columna_a_ordenar] < matriz_t[indice_sig_fila][in_columna_a_ordenar]:
                indice_mayor_elemento = indice_sig_fila
        
        if indice_mayor_elemento != indice_fila:
            # tem que trocar
            fila_aux = matriz_t[indice_mayor_elemento]
            matriz_t[indice_mayor_elemento] = matriz_t[indice_fila]
            matriz_t[indice_fila] = fila_aux

def trasponer_y_ordenar(matriz: list[list]):
    matriz_t = crear_matriz_t(matriz)
    indice_elegido = mapear_valor('vistas')
    ordenar_selection_t(matriz_t, indice_elegido)

    # mostrar_datos(matriz_t)
    mostrar_datos_t(matriz_t)

trasponer_y_ordenar(matriz_paulina)


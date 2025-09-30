from utn_fra.datasets import (
    titulos_lk,
    duraciones_lk,
    vistas_lk,
    likes_lk
 )

matriz_lk = [
    titulos_lk,
    duraciones_lk,
    vistas_lk,
    likes_lk
]


# 3
def obtener_existencias(matriz: list[list]):
    return len(matriz[0])
# 3
def mostrar_existencias(matriz: list[list]):
    cantidad = obtener_existencias(matriz)
    mensaje =\
    f"""
    Hay {cantidad} Videos
    """
    print(mensaje)

"""
4 - Existencias Videos en vivo: 
    Mostrar la cantidad de videos que contengan en su titulo “(En vivo…)”
5 - Existencias Videos oficiales: 
    Mostrar la cantidad de videos que contengan en su título: (Video Oficial)
"""

def obtener_datos_filtrados(matriz_original: list[list], matriz_filtrada: list[list], indice_col: int):
    for indice_fila in range(len(matriz_original)):
        dato = matriz_original[indice_fila][indice_col]
        matriz_filtrada[indice_fila].append(dato)

def filtrar_video(matriz: list[list], tipo_video: str='En Vivo'):
    matriz_filtrada = [
        [],[],[],[]
    ]

    for indice_columna in range(len(matriz[0])):
        if tipo_video in matriz[mapear_valor('titulos')][indice_columna]:
            obtener_datos_filtrados(matriz, matriz_filtrada, indice_columna)
            
    return matriz_filtrada


# print(filtrar_video(matriz_lk, tipo_video='Video Oficial'))
# print(filtrar_video(matriz_lk, tipo_video='En Vivo'))

def filtrar_2(matriz: list[list], tipo_video: str='En Vivo'):
    matriz_filtrada = [
        [],[],[],[]
    ]

    cant_columnas = obtener_existencias(matriz)

    for indice_columna in range(cant_columnas):

        es_en_vivo = False

        for indice_fila in range(len(matriz)):

            if indice_fila == 0 and tipo_video in matriz[indice_fila][indice_columna].lower():
                es_en_vivo = True
            
            if es_en_vivo:
                matriz_filtrada[indice_fila].append(
                    matriz[indice_fila][indice_columna].lower()
                )

    return obtener_existencias(matriz_filtrada)

# print(filtrar_video(matriz_lk, tipo_video='Video Oficial'))
# print(filtrar_2(matriz_lk, tipo_video='Video Oficial'))

def mostrar_cantidad_de_videos(matriz: list[list], tipo_video: list = ['En Vivo']):

    existencias = 0

    for tipo in tipo_video:
        matriz_filtrada = filtrar_video(matriz, tipo)
        existencias += obtener_existencias(matriz_filtrada)

    mensaje =\
    f"""
    Hay {existencias} videos de tipo: """

    for tipo in tipo_video:
        mensaje += f'{tipo}'

        if tipo_video.index(tipo) != len(tipo_video) -1:
            mensaje += ', '


    print(mensaje)

# mostrar_cantidad_de_videos(matriz_lk, tipo_video=['En Vivo', 'Estadio', 'Video Oficial'])

def mapear_valor(texto: str):
    """
    Mapea segun numeros de indices:

    Args:
        titulos -> 0
        vistas -> 2
        duraciones -> 1
        likes -> 3
    """
    match texto:
        case 'titulos':
            return 0
        case 'vistas':
            return 2
        case 'duraciones':
            return 1
        case 'likes':
            return 3
        
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

"""
Ordenar personalizado : Ordenar la matriz según lo siguiente:

Primero deben aparecer los videos en vivo (Ordenados según tiempo DES).
Luego deben aparecer los videos oficiales (Ordenados según tiempo DES).

Por último deben aparecer el resto de videos (Ordenados según tiempo DES).

"""

def concatenar_matrices(matriz_concatenada: list[list], matriz_aux: list[list]):

    for indice_fila in range(len(matriz_concatenada)):
        fila_concatenada = matriz_concatenada[indice_fila] + matriz_aux[indice_fila]
        matriz_concatenada[indice_fila] = fila_concatenada

def verificar_si_excluye(matriz: list[list], tipo_video: list[str], indice_columna: int):
    cantidad_excluida = 0
    for tipo in tipo_video:
        titulo = matriz[mapear_valor('titulos')][indice_columna]
        if tipo not in titulo:
            cantidad_excluida += 1
    return cantidad_excluida

def filtrar_video_excluidos(matriz: list[list], tipo_video: list=['En Vivo']):
    matriz_filtrada = [
        [],[],[],[]
    ]

    for indice_columna in range(len(matriz[0])):
        
        cantidad_excluida = verificar_si_excluye(matriz, tipo_video, indice_columna)
        if cantidad_excluida == len(tipo_video):
            obtener_datos_filtrados(matriz, matriz_filtrada, indice_columna)
            
    return matriz_filtrada

def ordenar_personalizado(matriz: list[list]):
    matriz_auxiliar = [[],[],[],[]]

    # Como tenemos 3 tipos de videos en vivo: "Estadio...", "En Vivo en..", "Sessions"
    # Filtramos por las tres
    matriz_estadio = filtrar_video(matriz, tipo_video='Estadio')
    matriz_en_vivo = filtrar_video(matriz, tipo_video='En Vivo')
    matriz_sessions = filtrar_video(matriz, tipo_video='Sessions')
    
    # Concatenamos las 3 matrices en una sola
    concatenar_matrices(matriz_estadio, matriz_en_vivo)
    concatenar_matrices(matriz_estadio, matriz_sessions)

    # ordenamos los videos en vivo
    order_selection(matriz_estadio, mapear_valor('duraciones'), tipo_orden='DES')
    # Agregamos la matris de videos en vivo a nuestra matriz auxiliar
    concatenar_matrices(matriz_auxiliar, matriz_estadio)

    # Filtramos videos oficiales
    matriz_vid_oficial = filtrar_video(matriz, tipo_video='Video Oficial')
    # Excluimos de ese filtro los videos en vivo que podrian ser oficiales (ya que queremos videos de estudio)
    matriz_vid_oficial = filtrar_video_excluidos(matriz_vid_oficial, tipo_video=["Estadio", "En Vivo"])
    # ordenamos la matriz
    order_selection(matriz_vid_oficial, mapear_valor('duraciones'), tipo_orden='DES')
    # concatenamos con nuestra matriz aux
    concatenar_matrices(matriz_auxiliar, matriz_vid_oficial)

    # filtramos el resto de videos que no son en vivo (los 3 tipos) ni en estudio
    matriz_videos_excl = filtrar_video_excluidos(matriz, tipo_video=['En Vivo', "Estadio", "Video Oficial",  "Sessions"])
    # ordenamos
    order_selection(matriz_videos_excl, mapear_valor('duraciones'), tipo_orden='DES')
    # concatenamos con la matrix aux
    concatenar_matrices(matriz_auxiliar, matriz_videos_excl)

    # mostramos los datos ordenados
    mostrar_datos(matriz_auxiliar)



ordenar_personalizado(matriz_lk)


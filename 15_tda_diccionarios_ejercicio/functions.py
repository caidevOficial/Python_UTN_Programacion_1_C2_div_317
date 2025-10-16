import datetime


def normalizar_nombre_colaborador(video: dict) -> str:
    nombre_tema_base: str = video.get('Tema')
    elementos_titulo = nombre_tema_base.split(' - ')
    
    titulo_saneado = ''
    colaboradores = 'No Tiene'

    if len(elementos_titulo) > 1:
        titulo_saneado = elementos_titulo[1]
        colaboradores = elementos_titulo[0]
    else:
        titulo_saneado = elementos_titulo[0]
    video['Tema'] = titulo_saneado
    video['Colaboradores'] = colaboradores

def normalizar_vistas(video: dict):
    datos_vistas = video.get('Vistas').split(' ')
    cantidad = int(datos_vistas[0])

    cantidad_saneada = cantidad * 1000000
    video['Vistas'] = cantidad_saneada

def normalizar_duracion(video: dict):
    datos_tiempo = video.get('Duracion').split(':')
    minutos = int(datos_tiempo[0])
    segundos = int(datos_tiempo[1])
    segundos_totales = minutos * 60 + segundos
    video['Duracion'] = segundos_totales

def normalizar_tiempo(video: dict):
    fecha = datetime.datetime.strptime(video.get('Fecha lanzamiento'), '%Y-%m-%d')
    fecha = fecha.date()
    video['Fecha lanzamiento'] = fecha

def normalizar_video(video: dict):

    normalizar_nombre_colaborador(video)
    normalizar_vistas(video)
    normalizar_duracion(video)
    normalizar_tiempo(video)
    video['Link'] = video.get('Link Youtube')



def normalizar_datos(videos: list[dict]) -> list[dict]:
    list_copy = videos.copy()

    for video in list_copy:
        normalizar_video(video)
    return list_copy

def max_caracteres(videos: list[dict]) -> int:
    cantidad = 0
    for video in videos:
        if len(video.get('Tema')) > cantidad:
            cantidad = len(video.get('Tema'))
    return cantidad

def mostrar_info_video(caracteres: int, video: dict):
    datos = f'{video.get("Tema"):{caracteres}} | {video.get("Duracion"):03}'
    print(datos)

def mostrar_info_completa_video(caracteres: int, video: dict):
    colaboradores_normalizados = video.get('Colaboradores').replace('|', '-')
    if len(colaboradores_normalizados) > 15:
        colab_truncado = f'{colaboradores_normalizados[:12]}...'
    else:
        colab_truncado = colaboradores_normalizados
    datos = f'{video.get("Tema"):{caracteres}} | {colab_truncado:15} | {video.get("Duracion"):03} | {video.get('Vistas'):010}'
    print(datos)

def mostrar_temas(videos: list[dict]):
    cantidad_maxima_caracteres = max_caracteres(videos)
    header = f'{'Nombre: ':{cantidad_maxima_caracteres}} | Duracion'
    separacion = '_' * cantidad_maxima_caracteres
    separacion + '_' * 10
    print(header)
    print(separacion)
    for video in videos:
        mostrar_info_video(cantidad_maxima_caracteres, video)


def ordenar_quick_por(videos: list[dict], key: str, modo: str = 'ASC') -> list[dict]:

    if len(videos) < 2:
        return videos
    
    pivot = videos.pop()

    mas_grandes = []
    mas_chicos = []

    for video in videos:
        if video.get(key) > pivot.get(key):
            mas_grandes.append(video)
        else:
            mas_chicos.append(video)
    
    if modo == 'ASC':
        return ordenar_quick_por(mas_chicos, key, modo) + [pivot] + ordenar_quick_por(mas_grandes, key, modo)
    else:
        return ordenar_quick_por(mas_grandes, key, modo) + [pivot] + ordenar_quick_por(mas_chicos, key, modo)

def calcular_promedio(videos: list[dict]) -> float:
    suma = 0
    cantidad = len(videos)

    for video in videos:
        suma += video.get('Vistas')
    
    promedio = suma / cantidad
    return promedio

def mostrar_promedio(videos: list[dict]):
    promedio = calcular_promedio(videos)
    promedio_redondeado = round(promedio / 1000000, 2)
    mensaje = f"El promedio de vistas es: {promedio_redondeado} millones"
    print(mensaje)

def calcular_max_min(videos: list[dict], key:str, operacion: str = 'maximo') -> float:
    max_min = None

    for video in videos:
        if operacion == 'maximo' and (max_min == None or max_min < video.get(key)) or\
            operacion == 'minimo' and (max_min == None or max_min > video.get(key)):
            max_min = video.get(key)

    return max_min

def mostrar_max_min(videos: list[dict], key:str, operacion: str = 'maximo'):
    max_min = calcular_max_min(videos, key, operacion)

    mensaje = f'El {operacion} de {key} es {max_min}'
    print(mensaje)

def buscar_video_por(videos: list[dict], key: str, valor: str):
    cantidad_maxima_caracteres = max_caracteres(videos)
    for video in videos:
        if valor in video.get(key).upper():
            mostrar_info_completa_video(cantidad_maxima_caracteres, video)

def buscar_videos_coincidencia(videos: list[dict], key: str, valor: str) -> list[dict]:
    coincidencias = []

    for video in videos:
        if valor in video.get(key).upper():
            coincidencias.append(video)
    return coincidencias

def mostrar_info_completa(videos: list[dict]):
    cantidad_maxima_caracteres = max_caracteres(videos)
    for video in videos:
        mostrar_info_completa_video(cantidad_maxima_caracteres, video)

def mostrar_coincidencias(videos: list[dict]):

    buscar_por = input('Buscar por:\nTema\nColaboradores\nOpcion: ').capitalize()
    busqueda = input('Palabra a buscar: ').upper()

    if buscar_por in ('Tema', 'Colaboradores'):
        # buscar_video_por(videos, key=buscar_por, valor=busqueda)
        coincidencias = buscar_videos_coincidencia(videos, key=buscar_por, valor=busqueda)
        mostrar_info_completa(coincidencias)

    else:
        print(f'Error, "{buscar_por}" no es una opcion válida de busqueda')

def obtener_colaboradores_unicos(videos: list[dict]) -> list[str]:
    colab_unicos = set()


    for video in videos:
        if not 'No Tiene' in video.get('Colaboradores'):
            colaboradores = video.get('Colaboradores').split(' | ')

            for colaborador in colaboradores:
                colab_unicos.add(colaborador)
    
    lista_colab_unicos = list(colab_unicos)
    lista_colab_unicos.sort()

    return lista_colab_unicos

def mapear_colaboradores(list_colaboradores: list[str]):
    cantidad = len(list_colaboradores)

    for numero in range(cantidad):
        list_colaboradores[numero] = f'{numero + 1} - {list_colaboradores[numero]}'

def mostrar_colaboradores(lista_colab: list[str]):
    for colab in lista_colab:
        print(colab)


def mostrar_videos_con_colab(videos: list[dict]):

    colabs = obtener_colaboradores_unicos(videos)
    # mapear_colaboradores(colabs)

    print('Elija un colaborador de la lista para mostrar un video en le que participe.')
    mostrar_colaboradores(colabs)
    colaborador = input('Escriba un nombre: ').upper()
    coincidencias = buscar_videos_coincidencia(videos, key='Colaboradores', valor=colaborador)
    mostrar_info_completa(coincidencias)






# fecha = datetime.datetime.strptime('2025-10-15', '%Y-%m-%d')

# fecha.month
from menu import show_menu
from validations import validate_input
import os
from functions import (
    normalizar_datos, mostrar_temas, ordenar_quick_por,
    mostrar_promedio, mostrar_max_min, mostrar_coincidencias,
    mostrar_videos_con_colab, filtrar_videos_de_mes
)


def application(songs: list[dict]):
    
    running = True
    lista_normalizada = []

    while running:
        show_menu()
        option = validate_input(1, 10)

        match option:
            case 1:
                lista_normalizada = normalizar_datos(songs)
            case 2:
                mostrar_temas(lista_normalizada)
            case 3:
                lista_ordenada = ordenar_quick_por(lista_normalizada, key='Duracion', modo='DES')
                mostrar_temas(lista_ordenada)
            case 4:
                mostrar_promedio(lista_normalizada)
            case 5:
                mostrar_max_min(lista_normalizada, key='Vistas', operacion='maximo')
            case 6:
                mostrar_max_min(lista_normalizada, key='Vistas', operacion='minimo')
            case 7:
                mostrar_coincidencias(lista_normalizada)
            case 8:
                mostrar_videos_con_colab(lista_normalizada)
            case 9:
                filtrar_videos_de_mes(lista_normalizada)
            case 10:
                running = False
                print('Cerrando App')
        os.system('pause')
        os.system('cls')

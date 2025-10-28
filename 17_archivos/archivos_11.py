import json
from utn_fra.datasets import lista_diccionario_heroes

heroes = lista_diccionario_heroes[:4]


def leer_archivo_texto(ruta: str) -> str:
    content = ''
    with open(ruta, 'r', encoding='utf-8') as file:
        content = file.readlines()
    
    return content



def crear_diccionario(lista_claves: list, lista_datos: list):
    diccionario = {}
    for index_key in range(len(lista_claves)):
        nombre_clave = lista_claves[index_key]
        nombre_valor = lista_datos[index_key]

        diccionario[nombre_clave] = nombre_valor
    return diccionario

def cargar_csv_a_lista_dict(ruta: str) -> list[dict]:
    lista_info_heroes = leer_archivo_texto(ruta)
    lista_claves = lista_info_heroes.pop(0).split(',')

    lista_dict_heroes = []

    for linea in lista_info_heroes:
        datos_h = linea.split(',')
        dict_h = crear_diccionario(lista_claves, datos_h)
        
        lista_dict_heroes.append(dict_h)
    return lista_dict_heroes

def crear_json_desde_lista_dict(ruta: str, lista_dic: list[dict]):
    with open(ruta, 'w', encoding='utf-8') as file:
        diccionario = {}
        diccionario['heroes'] = lista_dic
        json.dump(diccionario, file, indent=4)

CSV_HEROES = './17_archivos/heroes_dc.csv'

import datetime

fecha_str = datetime.date.strftime(datetime.datetime.now(),'%Y_%m_%d__%H_%M_%S')
JSON_FILE = f'./17_archivos/heroes_{fecha_str}.json'
lista_diccionario_de_csv = cargar_csv_a_lista_dict(CSV_HEROES)

crear_json_desde_lista_dict(JSON_FILE, lista_diccionario_de_csv[:2])

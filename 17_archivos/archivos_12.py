import json


def leer_json_a_list_dict(ruta: str) -> list[dict]:
    data = {}
    with open(ruta, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


JSON_FILE = './17_archivos/heroes.json'

dict_lista_dict = leer_json_a_list_dict(JSON_FILE)

lista_heroes = dict_lista_dict.get('heroes')



"""
config_juego = leer_json_a_list_dict(JSON_FILE)
config_player = config_juego.get('player')
config_enemy = config_juego.get('enemy')

"""

print(dict_lista_dict)
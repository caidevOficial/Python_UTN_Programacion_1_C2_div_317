
def leer_archivo_texto(ruta: str) -> str:
    content = ''
    with open(ruta, 'r', encoding='utf-8') as file:
        content = file.readlines()
    
    return content

CSV_HEROES = './17_archivos/heroes_dc.csv'

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


from funciones import show_dict_list_to_table

lista = cargar_csv_a_lista_dict(CSV_HEROES)[12:15]
headers = {
    key: key.upper()
    for key in lista[0].keys()
}


show_dict_list_to_table(lista, headers)
# print()

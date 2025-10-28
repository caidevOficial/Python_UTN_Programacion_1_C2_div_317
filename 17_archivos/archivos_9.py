from utn_fra.datasets import lista_diccionario_heroes

def escribir_texto(ruta: str, contenido: str, anexar: bool = False) -> int:
    lineas = 0
    modo = 'w'
    if anexar == True:
        modo = 'a'

    with open(ruta, modo, encoding='utf-8') as file:
        lineas = file.write(contenido)
    return lineas











heroes = lista_diccionario_heroes[:]

heroes_dc = []
for heroe in heroes:
    if heroe.get('empresa') == 'DC Comics':
        heroes_dc.append(heroe)

def obtener_encabezado(heroe: dict) -> str:
    encabezado = ''
    for key in heroe.keys():
        encabezado += f'{key},'
    encabezado = encabezado[:-1]
    return encabezado

def parsear_dict_a_csv_str(heroe: dict) -> str:
    info = ''
    for value in heroe.values():
        info = f'{info}{value},'
    # "goku,saiyan,100,50"
    info = info[:-1]
    return info

info_heroes = obtener_encabezado(heroes_dc[0])

for heroe in heroes_dc:
    info = parsear_dict_a_csv_str(heroe)

    info_heroes += f'\n{info}'


CSV_HEROES = './17_archivos/heroes_dc.csv'
escribir_texto(CSV_HEROES, info_heroes)
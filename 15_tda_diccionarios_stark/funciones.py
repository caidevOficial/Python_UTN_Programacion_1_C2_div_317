
def es_genero(heroe: dict, genero: str) -> bool:
    return heroe.get('genero') == genero

def mostrar_datos_heroe(heroe: dict) -> None:
    message =\
    f"""{heroe.get("nombre")[:15]:15} | {heroe.get("identidad")[:15]:15} | {heroe.get("alias")[:15]:15} | {heroe.get("genero")[:15]:15}"""
    print(message)

def mostrar_datos_heroes(heroes: list[dict]) -> None:
    header = f'Nombre          | Identidad       | Alias           | Género'
    print(header)
    for heroe in heroes:
        mostrar_datos_heroe(heroe)

def filtrar_heroes_por_genero(heroes: list[dict], genero: str):
    heroes_filtrados = []
    for heroe in heroes:
        if es_genero(heroe, genero):
            heroes_filtrados.append(heroe)
    return heroes_filtrados

def stark_imprimir_heroe_genero(heroes: list[dict], genero: str) -> None:
    heroes_filtrados = filtrar_heroes_por_genero(heroes, genero)
    mostrar_datos_heroes(heroes_filtrados)

def calcular_min(heroes: list[dict], key: str) -> dict:
    minimo = None
    for heroe in heroes:
        if minimo == None or heroe.get(key) < minimo.get(key):
            minimo = heroe
    return minimo

def calcular_max(heroes: list[dict], key: str) -> dict:
    maximo = None
    for heroe in heroes:
        if maximo == None or heroe.get(key) > maximo.get(key):
            maximo = heroe
    return maximo

def calcular_min_genero(heroes: list[dict], key: str, valor_genero: str) -> dict:
    heroes_filtrados = filtrar_heroes_por_genero(heroes, valor_genero)
    heroe_minimo = calcular_min(heroes_filtrados, key)
    return heroe_minimo

def calcular_max_genero(heroes: list[dict], key: str, valor_genero: str) -> dict:
    heroes_filtrados = filtrar_heroes_por_genero(heroes, valor_genero)
    heroe_maximo = calcular_max(heroes_filtrados, key)
    return heroe_maximo

def calcular_max_min_dato_genero(heroes: list[dict], calculo: str, key: str, valor_genero: str) -> dict:
    heroe_seleccionado = {}

    if calculo == 'maximo':
        heroe_seleccionado = calcular_max_genero(heroes, key, valor_genero)
    else:
        heroe_seleccionado = calcular_min_genero(heroes, key, valor_genero)
    return heroe_seleccionado

def stark_calcular_imprimir_heroe_genero(heroes: list[dict], calculo: str, key: str, valor_genero: str):
    if len(heroes) > 0:
        heroe_seleccionado = calcular_max_min_dato_genero(heroes, calculo, key, valor_genero)
        mostrar_datos_heroes([heroe_seleccionado])

def sumar_valor_clave(heroes: list[dict], key: str) -> float:
    suma = 0
    for heroe in heroes:
        suma += heroe.get(key, 0)
    return suma

def sumar_dato_heroe_genero(heroes: list[dict], key: str, valor_genero: str) -> float:
    heroes_filtrados = filtrar_heroes_por_genero(heroes, valor_genero)
    suma = sumar_valor_clave(heroes_filtrados, key)
    return suma

def cantidad_heroes_genero(heroes: list[dict], valor_genero: str) -> int:
    heroes_filtrados = filtrar_heroes_por_genero(heroes, valor_genero)
    return len(heroes_filtrados)

def calcular_promedio_genero(heroes: list[dict], key: str, valor_genero: str) -> float:
    suma = sumar_dato_heroe_genero(heroes, key, valor_genero)
    cantidad = cantidad_heroes_genero(heroes, valor_genero)

    if cantidad != 0:
        promedio = suma / cantidad
    else:
        promedio = 0
    return promedio

def stark_calcular_imprimir_promedio_altura_genero(heroes: list[dict], key: str, valor_genero: str) -> None:
    if len(heroes) == 0:
        print('ERROR: La lista esta vacía')
    else:
        promedio = calcular_promedio_genero(heroes, key, valor_genero)
        print(f'El promedio de {key.capitalize()} de genero {valor_genero} es: {promedio:.2f}')

def calcular_cantidad_tipo(heroes: list[dict], key: str) -> dict:

    nuevo_diccionario = dict()

    if len(heroes) != 0:
        for heroe in heroes:
            dato = heroe.get(key)

            if dato == '-':
                dato = 'Desconocido'

            if  dato not in nuevo_diccionario.keys():
                nuevo_diccionario[dato] =  1
            else:
                nuevo_diccionario[dato] +=  1

    return nuevo_diccionario

def imprimir_cantidad_heroes_tipo(variedades_tipos: dict, tipo_de_dato: str) -> None:

    for clave, valor in variedades_tipos.items():
        mensaje = f"Característica: {tipo_de_dato} {clave} - Cantidad de héroes: {valor}"
        print(mensaje)

def stark_calcular_cantidad_por_tipo(heroes: list[dict], tipo_de_dato: str) -> None:
    diversidad = calcular_cantidad_tipo(heroes, tipo_de_dato)
    imprimir_cantidad_heroes_tipo(diversidad, tipo_de_dato)

def obtener_lista_de_tipos(heroes: list[dict], key: str) -> list:
    valores_unicos = set()

    for heroe in heroes:
        valores_unicos.add(heroe.get(key))
    
    lista_unicos = list(valores_unicos)
    lista_unicos.sort()

    return lista_unicos

def normalizar_dato(valor: str, valor_defecto: str) -> str:
    if valor in ('', '-', None):
        valor = valor_defecto
    return valor

def obtener_heroes_por_tipo(heroes: list[dict], lista_tipos: list, key: str):
    diccionario_lista_tipos = {}

    for variedad in lista_tipos:
        if variedad not in diccionario_lista_tipos.keys():
            diccionario_lista_tipos[variedad] = []

        for heroe in heroes:
            valor_normalizado = normalizar_dato(heroe.get(key), 'N/A')
            if valor_normalizado in diccionario_lista_tipos.keys():
                if heroe.get('nombre') not in diccionario_lista_tipos[valor_normalizado]:
                    diccionario_lista_tipos[valor_normalizado].append(heroe.get('nombre'))
    return diccionario_lista_tipos

def imprimir_heroes_por_tipo(diccionario_variedades: dict, key: str):
    for variedad, heroes in diccionario_variedades.items():

        str_heroes = ' | '.join(heroes)
        mensaje = f'{key} {variedad}: {str_heroes}'
        print(mensaje)

def stark_listar_heroes_por_dato(heroes: list[dict], key: str):
    lista_tipos = obtener_lista_de_tipos(heroes, key=key)
    variedades = obtener_heroes_por_tipo(heroes, lista_tipos, key=key)
    imprimir_heroes_por_tipo(variedades, key=key)

if __name__ == '__main__':
    from utn_fra.datasets import lista_diccionario_heroes
    lista_tipos = obtener_lista_de_tipos(lista_diccionario_heroes, key='raza')
    variedades = obtener_heroes_por_tipo(lista_diccionario_heroes, lista_tipos, key='raza')
    imprimir_heroes_por_tipo(variedades, key='raza')

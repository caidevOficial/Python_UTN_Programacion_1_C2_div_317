"""
Recorrer la lista imprimiendo por consola el modelo de 
                autos que hay en cada garage
"""

def obtener_dato_de_indice(lista_datos: list, indice_dato: int):
    return lista_datos[indice_dato]

def mostrar_modelos(modelos: list) -> None:

    # for modelo in modelos:
    #     print(f'{modelo}')
    
    for indice_garaje in range(len(modelos)):
        dato_modelo = obtener_dato_de_indice(modelos, indice_garaje)
        print(f'Garaje N°{indice_garaje} -> {dato_modelo}')

"""
Recorrer la lista imprimiendo por consola el modelo de 
                autos que hay en cada garage junto con la cantidad que posee.
"""

def mostrar_modelo_y_cantidad(modelos: list, cantidades: list) -> None:

    for indice_datos in range(len(modelos)):
        modelo = obtener_dato_de_indice(modelos, indice_datos)
        cantidad = obtener_dato_de_indice(cantidades, indice_datos)

        print(f'Garaje N°{indice_datos} -> {modelo} - {cantidad} unidades')

"""
Recorrer las listas y determinar cuál es el modelo de auto 
                que más cantidad posee la concesionaria (MÁXIMO).
"""

def obtener_indice_condicion(lista_datos: list, modo: str = 'mayor') -> int:

    indice_elegido = None

    for indice_dato in range(len(lista_datos)):

        if indice_elegido == None or\
            (lista_datos[indice_elegido] < lista_datos[indice_dato] and modo == 'mayor') or\
            (lista_datos[indice_elegido] > lista_datos[indice_dato] and modo == 'menor'):
            indice_elegido = indice_dato
    
    return indice_elegido

def mostrar_modelo_con_cantidad(modelos: list, cantidades: list, modo: str = 'mayor') -> None:
    indice_mayor = obtener_indice_condicion(cantidades, modo)
    modelo = obtener_dato_de_indice(modelos, indice_mayor)
    cantidad = obtener_dato_de_indice(cantidades, indice_mayor)

    mensaje = f'El garaje con {modo} cantidad: N° {indice_mayor} -> {modelo} - {cantidad} unidades'
    print(mensaje)

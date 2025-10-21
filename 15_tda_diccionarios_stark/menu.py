from validations import validate_input


def obtener_menu():
    message =\
    """
    1 - Recorrer la lista imprimiendo por consola el nombre de 
        cada superhéroe de género M
    2 - Recorrer la lista imprimiendo por consola el nombre de 
        cada superhéroe de género F
    3 - Recorrer la lista y determinar cuál es el superhéroe más alto de género M 
    4 - Recorrer la lista y determinar cuál es el superhéroe más alto de género NB 
    5 - Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M 
    6 - Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F 
    7 - Recorrer la lista y determinar la altura promedio de los  superhéroes de género M
    8 - Recorrer la lista y determinar la altura promedio de los  superhéroes de género F
    9 - Informar cual es el Nombre del superhéroe asociado a cada uno de los 
        indicadores anteriores (ítems C a F)
    10 - Determinar cuántos superhéroes tienen cada tipo de color de ojos.
    11 - Determinar cuántos superhéroes tienen cada tipo de color de pelo.
    12 - Determinar cuántos superhéroes tienen cada tipo de inteligencia 
            (En caso de no tener, Inicializarlo con ‘No Tiene’). 
    13 - Listar todos los superhéroes agrupados por color de ojos.
    14 - Listar todos los superhéroes agrupados por color de pelo.
    15 - Listar todos los superhéroes agrupados por alineación
    16 - Salir
    """
    return message

def imprimir_menu() -> None:
    texto = obtener_menu()
    print(texto)

def stark_menu_principal():
    imprimir_menu()
    return validate_input(1,16)


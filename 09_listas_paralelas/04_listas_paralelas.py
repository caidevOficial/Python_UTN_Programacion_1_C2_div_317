# listas paralelas

def tomar_datos(lista_nombre: list, lista_apellido: list, lista_edad: list) -> None:

    cantidad = 3

    for vuelta in range(cantidad):

        print(f'Complete los datos de la {vuelta + 1}° Persona.')

        nombre = input(f'Ingrese el nombre de la {vuelta + 1}° persona: ')
        
        apellido = input(f'Ingrese el apellido de la {vuelta + 1}° persona: ')
        
        edad_str = input(f'Ingrese el edad de la {vuelta + 1}° persona: ')
        edad = int(edad_str)
        
        
        lista_nombre.append(nombre)
        lista_apellido.append(apellido)
        lista_edad.append(edad)

def mostrar_info_persona_en_indice(lista_nombre: list, lista_apellido: list, lista_edad: list, indice_a_buscar: int) -> str:
    nombre = lista_nombre[indice_a_buscar]
    apellido = lista_apellido[indice_a_buscar]
    edad = lista_edad[indice_a_buscar]

    mensaje = f"{nombre} - {apellido} - {edad}"
    return mensaje

def imprimir_datos_personas(lista_nombre: list, lista_apellido: list, lista_edad: list) -> None:
    cantidad = len(lista_nombre)

    for indice_persona in range(cantidad):

        sub_mensaje = mostrar_info_persona_en_indice(lista_nombre, lista_apellido, lista_edad, indice_persona)
        mensaje = f'Persona N° {indice_persona + 1} {sub_mensaje}'
        print(mensaje)

def buscar_indice_mayor_persona(lista_edad: list) -> int:
    indice_mayor_edad = None

    for indice_persona in range(len(lista_edad)):

        if indice_mayor_edad == None or lista_edad[indice_persona] > lista_edad[indice_mayor_edad]:
            indice_mayor_edad = indice_persona
    
    return indice_mayor_edad



lista_nombres_personas = []
lista_apellidos_personas = []
lista_edades_personas = []

tomar_datos(lista_nombres_personas, lista_apellidos_personas, lista_edades_personas)
imprimir_datos_personas(lista_nombres_personas, lista_apellidos_personas, lista_edades_personas)

indice_mayor = buscar_indice_mayor_persona(lista_edades_personas)
mensaje = mostrar_info_persona_en_indice(lista_nombres_personas, lista_apellidos_personas, lista_edades_personas, indice_mayor)

print(f'La persona de mayor edad es: {mensaje}')



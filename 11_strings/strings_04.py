
# buen día
# Buen día
def utn_capitalize(texto: str) -> str:
    # nuevo_texto = texto[0].upper() + texto[1:].lower()
    nuevo_texto = f'{texto[0].upper()}{texto[1:].lower()}'
    return nuevo_texto

# buen día gente de la 317
# Buen Día Gente De La 317
def utn_title(texto: str) -> str:
    mi_nuevo_texto = ''
    ultimo_indice_espacio = None
    
    for indice_caracter in range(len(texto)):
        
        if indice_caracter == 0:
            caracter_actual = texto[indice_caracter].upper()
        elif ultimo_indice_espacio != None and ultimo_indice_espacio + 1 == indice_caracter:
            caracter_actual = texto[indice_caracter].upper()
        else:
            caracter_actual = texto[indice_caracter]
        
        mi_nuevo_texto += caracter_actual

        if texto[indice_caracter].isspace():
            ultimo_indice_espacio = indice_caracter
    return mi_nuevo_texto


def encontrar_indices_de_espacio(texto: str) -> list[int]:
    indices_espacios = []

    for indice_char in range(len(texto)):
        if texto[indice_char].isspace():
            indices_espacios.append(indice_char)
    return indices_espacios

# buen día gente de la 317
#     4   8     14 17 20
def utn_title_slice(texto: str) -> str:
    indices_espacios = encontrar_indices_de_espacio(texto)
    print(indices_espacios)
    mi_nuevo_texto = ''

    indice_inicio = 0
    for indice_espacio in range(len(indices_espacios)):
        
        indice_final = indices_espacios[indice_espacio]
        mi_nuevo_texto += utn_capitalize(texto[indice_inicio:indice_final])
        if texto[indice_final].isspace():
            mi_nuevo_texto += texto[indice_final]
        indice_inicio = indice_final + 1
    
    if indice_inicio < len(texto) -1:
        mi_nuevo_texto += utn_capitalize(texto[indice_inicio:])
    
    return mi_nuevo_texto


print(utn_title_slice('buen día gente de la 317'))
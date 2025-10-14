personas = [
    {
        "nombre": 'Pepe',
        "edad": 56
    },
    {
        "nombre": 'Moni',
        "edad": 45
    }
]


def selection_sort_dict(diccionarios: list[dict], key: str, modo: str = 'ASC'):
    lista_diccionarios_cp = diccionarios.copy()

    for indice_actual in range(len(lista_diccionarios_cp) - 1):
        indice_menor = indice_actual

        for indice_sig in range(indice_actual + 1, len(lista_diccionarios_cp)):
            dict_actual = lista_diccionarios_cp[indice_menor]
            dict_sig = lista_diccionarios_cp[indice_sig]
            
            if (modo == 'ASC' and dict_actual.get(key) > dict_sig.get(key)) or\
                modo == 'DES' and dict_actual.get(key) < dict_sig.get(key):
                indice_menor = indice_sig
        
        if indice_menor != indice_actual:
            # aux = lista_diccionarios_cp[indice_menor]
            # lista_diccionarios_cp[indice_menor] = lista_diccionarios_cp[indice_actual]
            # lista_diccionarios_cp[indice_actual] = aux

            lista_diccionarios_cp[indice_menor],lista_diccionarios_cp[indice_actual] =\
            lista_diccionarios_cp[indice_actual],lista_diccionarios_cp[indice_menor]

    return lista_diccionarios_cp

print(personas)
print(selection_sort_dict(personas, key='edad'))
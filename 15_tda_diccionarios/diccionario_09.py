mascotas = [
    {
        "especie": 'ave',
        "raza": 'cardenal',
        "movimiento": 'volador'
    },
    {
        "especie": 'ave',
        "raza": 'hornero',
        "movimiento": 'volador'
    },
    {
        "especie": 'gato',
        "raza": 'siames',
        "movimiento": 'terrestre'
    },
    {
        "especie": 'gato',
        "raza": 'persa',
        "movimiento": 'terrestre'
    },
    {
        "especie": 'perro',
        "raza": 'husky',
        "movimiento": 'terrestre'
    },
    {
        "especie": 'perro',
        "raza": 'pug',
        "movimiento": 'terrestre'
    }
]

ciudades = [
    {
        "continente": 'america',
        "pais": 'argentina',
        "hemisferio": 'sur'
    },
    {
        "continente": 'europa',
        "pais": 'francia',
        "hemisferio": 'norte'
    },
    {
        "continente": 'america',
        "pais": 'canada',
        "hemisferio": 'norte'
    },
    {
        "continente": 'asia',
        "pais": 'china',
        "hemisferio": 'norte'
    },
    {
        "continente": 'asia',
        "pais": 'japon',
        "hemisferio": 'norte'
    },
    {
        "continente": 'america',
        "pais": 'brasil',
        "hemisferio": 'sur'
    }
]

def filtrar_por_clave(lista_dict: list[dict], clave_filtro: str, valor: str):

    # Algoritmo clásico
    lista_filtrada = []

    for elemento in lista_dict:
        if elemento.get(clave_filtro) == valor:
            lista_filtrada.append(elemento)
    
    # List Comprehension
    # lista_filtrada = [
    #     elemento for elemento in lista_dict 
    #     if elemento.get(clave_filtro) == valor
    # ]


    return lista_filtrada


print(filtrar_por_clave(ciudades, clave_filtro='hemisferio', valor='norte'))
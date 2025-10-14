
mascota = {
    "especie": 'Perro',
    "raza": 'Doberman',
    "datos": {
        "nombre": 'Bobby',
        "edad": 4,
        "vacunas": {
            "vacuna_1": 'Rabia',
            "vacuna_2": 'Moquillo'
        }
    }
}

# for clave, valor in mascota.items():
#     if type(valor) == dict:
#         for clave_sd, valor_sd in valor.items():
#             print(f'{clave} -> {clave_sd} -> {valor_sd}')
#     else:
#         print(f'{clave} -> {valor}')


especie = mascota.get('especie')


datos_mascota = mascota.get('datos')

nombre = datos_mascota.get('nombre')

vacunas_mascota = datos_mascota.get('vacunas')
vacunas_mascota['vacuna_2'] = 'Gripe'


vacuna_moquillo = vacunas_mascota.get('vacuna_2')

for clave, valor in mascota.items():
    if type(valor) == dict:
        for clave_sd, valor_sd in valor.items():
            print(f'{clave} -> {clave_sd} -> {valor_sd}')
    else:
        print(f'{clave} -> {valor}')

# print(f'{especie},{nombre},{vacuna_moquillo}')
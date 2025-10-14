texto = 'Hoy es Lunes y estamos en la clase de programación I viendo diccionarios con el lenguaje Python' * 61

diccionario_cant_caracteres = dict()

for caracter in texto:
    caracter_min = caracter.lower()
    if caracter_min not in diccionario_cant_caracteres.keys():
        diccionario_cant_caracteres[caracter_min] = 1
    else:
        diccionario_cant_caracteres[caracter_min] = diccionario_cant_caracteres.get(caracter_min) + 1


# for caracter in texto:
#     caracter_min = caracter.lower()
#     diccionario_cant_caracteres[caracter_min] = diccionario_cant_caracteres.get(caracter_min, 0) + 1

# print(diccionario_cant_caracteres)

for clave, valor in diccionario_cant_caracteres.items():

    print(f'{clave} -> {valor}')

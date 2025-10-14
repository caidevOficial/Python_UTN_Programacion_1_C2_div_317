persona = {
    "nombre": 'Pepe Argento',
    "edad": 57,
    "dni": '11111111',
    "direccion": 'Calle falsa 123, Boedo'
}

persona["nombre"] = 'Fatiga'

persona['altura'] = 1.72

lista_claves = list(persona.keys())
lista_claves.sort()

print(lista_claves)


diccionario_aux = dict()
for clave in lista_claves:
    diccionario_aux[clave] = persona.get(clave)

persona = diccionario_aux

persona['apellido'] = 'Perro'



for clave in diccionario_aux.keys():
    print(f'Clave: {clave} -> Valor: {persona.get(clave)}')

# for valor in persona.values():
#     print(valor)
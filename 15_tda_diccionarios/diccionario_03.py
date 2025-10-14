import random as rd



lista_personas = []

for i in range(3):

    persona = {
        "nombre": rd.choice(["Pepe", "Jose", "Fatiga", "Tito"]),
        "edad": rd.choice([57, 54, 46, 72])
    }
    lista_personas.append(persona)



for persona in lista_personas:
    # nombre = persona.get('nombre')
    # edad = persona.get('edad')

    persona['apellido'] = rd.choice(["Rodriguez", "Gonzalez", "Falcone", "Marconi"])
    persona['dni'] = rd.choice(['11111111', '22222222', '33333333'])
    # persona['nombre'] = None

print(lista_personas)


persona = lista_personas[0]

for clave, valor in persona.items():

    if clave == 'dni':
        persona[clave] = int(valor)


if 'dni' in persona.keys():
    persona['dni'] = int(persona.get('dni'))

print(persona)
    # print(datos)
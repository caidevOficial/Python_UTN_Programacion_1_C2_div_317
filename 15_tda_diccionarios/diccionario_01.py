import random as rd



lista_personas = []

for i in range(5):

    persona = {
        "nombre": rd.choice(["Pepe", "Jose", "Fatiga", "Tito"]),
        "edad": rd.choice([57, 54, 46, 72])
    }
    lista_personas.append(persona)

persona = {
    "nombre": 'Pepe Argento',
    "edad": 57,
    "dni": '11111111',
    "direccion": 'Calle falsa 123, Boedo'
}

# persona_1 = [
#     ['Pepe Argento'],
#     [57],
#     ['11111111'],
#     ['calle falsa 123']
# ]

# persona_2 = [
#     ['Pepe Argento', 57, '11111111', 'calle falsa 123']
# ]

# nombre_persona = persona["altura"]

nombre_persona = persona.get('altura', 'No existe esa clave')

print(nombre_persona)
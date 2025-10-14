"""
 Crea un diccionario llamado informacion_personal con las claves: 
 "nombre", "edad", "ciudad", y "ocupación". Asigna valores apropiados. 
 Luego, imprime el valor de la clave "edad".

"""

informacion_personal = {
    "nombre": 'Pepe Argento',
    "edad": 54,
    "ciudad": 'Boedo',
    "ocupacion": 'Vendedor'
}

print(informacion_personal['edad'])
print(informacion_personal.get('edad', 'No se encontro la clave edad'))



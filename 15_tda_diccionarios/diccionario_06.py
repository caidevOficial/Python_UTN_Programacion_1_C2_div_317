
mascota = {
    "nombre": "Huesos",
    "raza": "Perro",
    "edad": 6
}

mascota_datos_adicionales = {
    "nombre": 'Huesos 2',
    "familia": 'Los Simpsons',
    "ciudad": "Springfield"
}

# for clave, valor in mascota_datos_adicionales.items():
#     mascota[clave] = valor


mascota.update(mascota_datos_adicionales)

del mascota["nombre"]
# dato = mascota.pop('nombre')

# print(dato)

for clave, valor in mascota.items():
    print(f'{clave} -> {valor}')

mi_set_numerico = {1,2,3,"pepe", "fatiga"}
mi_lista = ["Moni","Pepe", "Fatiga","Pepe","Moni","Pepe", "Fatiga","Pepe","Moni","Pepe", "Fatiga","Pepe"]


def obtener_elementos_unicos(mi_lista: list) -> list:
    mi_set = set(mi_lista)
    mi_nueva_lista = list(mi_set)
    mi_nueva_lista.sort()
    return mi_nueva_lista

# print(mi_lista)
# print(obtener_elementos_unicos(mi_lista))

mi_nuevo_set = set()

for nombre in mi_lista:
    mi_nuevo_set.add(nombre)


elemento = 'Pepe'
if elemento in mi_nuevo_set:
    mi_nuevo_set.remove(elemento)
    print(f'Borrado: {elemento}')
else:
    print(f'No existe: {elemento}')
print(mi_nuevo_set)

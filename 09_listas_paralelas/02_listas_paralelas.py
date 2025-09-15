


def modificar_lista(lista: list[int]) -> None:
    lista.append(6)
    lista.pop(1)
    print(f'Direccion de memoria de la lista de la funcion: {hex(id(lista))}')
    print(f'Lista dentro de la funcion: {lista}')
    return lista


mi_lista = [1, 2, 3, 4, 5]
print(f'Direccion de memoria de la lista inicial: {hex(id(mi_lista))}')
mi_lista = modificar_lista(mi_lista)
print(mi_lista)  # None
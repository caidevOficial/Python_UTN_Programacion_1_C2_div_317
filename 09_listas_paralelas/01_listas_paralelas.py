mi_numero = 5


def modificar_numero(numero: int) -> None:
    numero += 5
    print(f'Direccion de memoria de la variable de la funcion: {hex(id(numero))}')
    print(f'Numero dentro de la funcion: {numero}')
    return numero


print(f'Direccion de memoria de la variable inicial: {hex(id(mi_numero))}')
modificar_numero(mi_numero)
print(mi_numero)
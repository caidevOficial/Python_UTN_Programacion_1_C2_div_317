
lista_original = ["Pepsi", "Coca", "Sprite"]

# lista_copia = lista_original.copy()


def ordenar_lista(lista_original: list):
    copia = lista_original.copy()

    copia.sort()
    print(copia)


ordenar_lista(lista_original)
print(lista_original)
lista_nombres = [
    "Pepe", "Goku", "Fatiga", "Homero"
]


for elemento in lista_nombres:
    indice_elemento = lista_nombres.index(elemento)
    lista_nombres[indice_elemento] = "Hola Mundo"
    print(elemento)


print(lista_nombres)

from utn_fra.datasets import lista_diccionario_heroes
from aplicacion import stark_marvel_app
import random as rd

if __name__ == '__main__':
    lista_copia = lista_diccionario_heroes.copy()
    rd.shuffle(lista_copia)
    stark_marvel_app(lista_copia[:50])

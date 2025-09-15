
# DES -> Mayor a Menor
def ordenar_selection_sort(mi_lista: list, modo: str = 'ASC') -> list:
    
    largo_lista = len(mi_lista)
    for indice_actual in range(largo_lista - 1):
        indice_mayor_elemento = indice_actual

        for siguiente_indice in range(indice_actual + 1, largo_lista):
            elemento_mayor = mi_lista[indice_mayor_elemento]
            siguiente_elemento = mi_lista[siguiente_indice]

            if (elemento_mayor > siguiente_elemento and modo == 'ASC') or\
                (elemento_mayor < siguiente_elemento and modo == 'DESC'):
                indice_mayor_elemento = siguiente_indice
        
        if indice_mayor_elemento != indice_actual:
            auxiliar = mi_lista[indice_actual]
            mi_lista[indice_actual] = mi_lista[indice_mayor_elemento]
            mi_lista[indice_mayor_elemento] = auxiliar
            
    return mi_lista


# ============ Testeamos tiempo y rendimiento ============
import random
from test_sorts import test_sort

cantidad = 1000 # 5.5 seg
mi_lista_test = list(range(cantidad))
random.shuffle(mi_lista_test)

test_sort(ordenar_selection_sort, mi_lista_test, 'DESC', sort_name='Selection Sort')
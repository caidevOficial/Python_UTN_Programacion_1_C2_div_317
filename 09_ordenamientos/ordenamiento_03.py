
def ordenar_quick_sort(mi_lista: list, modo: str = 'ASC') -> list:
    
    if len(mi_lista) < 2:
        return mi_lista
    
    # aca hacemos la chamba
    pivot = mi_lista.pop()
    lista_pivote = [pivot]
    mas_chicos = []
    mas_grandes = []

    for elemento in mi_lista:
        if elemento > pivot:
            mas_grandes.append(elemento)
        else:
            mas_chicos.append(elemento)
    
    if modo == 'DESC':
        return ordenar_quick_sort(mas_grandes, modo) + lista_pivote + ordenar_quick_sort(mas_chicos, modo)

    return ordenar_quick_sort(mas_chicos, modo) + lista_pivote + ordenar_quick_sort(mas_grandes, modo)


# ============ Testeamos tiempo y rendimiento ============
import random
from test_sorts import test_sort

cantidad = 10000
mi_lista_test = list(range(cantidad))
random.shuffle(mi_lista_test)

test_sort(ordenar_quick_sort, mi_lista_test, 'DESC', sort_name='Quick Sort')
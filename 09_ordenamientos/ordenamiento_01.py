

def ordenar_bubble_sort(mi_lista: list, modo: str = 'ASC') -> list:
    
    largo_lista = len(mi_lista)
    for indice in range(largo_lista):
        intercambio_realizado = False
        for siguiente_indice in range(0, (largo_lista - 1) - indice, 1):
            elemento_actual = mi_lista[siguiente_indice]
            proximo_elemento = mi_lista[siguiente_indice + 1]
            
            if (elemento_actual > proximo_elemento and modo == 'ASC') or\
                (elemento_actual < proximo_elemento and modo == 'DESC'):
                
                auxiliar = mi_lista[siguiente_indice]
                mi_lista[siguiente_indice] = mi_lista[siguiente_indice + 1]
                mi_lista[siguiente_indice + 1] = auxiliar
                intercambio_realizado = True
        
        if not intercambio_realizado:
            break
    return mi_lista
    

# ============ Testeamos tiempo y rendimiento ============
import random
from test_sorts import test_sort

cantidad = 1000 # 12seg
mi_lista_test = list(range(cantidad))
random.shuffle(mi_lista_test)

# test_sort(ordenar_bubble_sort, mi_lista_test, 'DESC', sort_name='Bubble Sort')

print(mi_lista_test[:15])

ordenar_bubble_sort(mi_lista_test, 'DESC')

print(mi_lista_test[:15])

ordenar_bubble_sort(mi_lista_test, 'ASC')

print(mi_lista_test[:15])
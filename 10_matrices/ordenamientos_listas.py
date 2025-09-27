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

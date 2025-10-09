# Creamos dos conjuntos (sets) con números para practicar operaciones de conjuntos
set_1 = {1,2,3,4,5}        # Primer conjunto: números del 1 al 5
set_2 = {4,5,6,7,8}        # Segundo conjunto: números del 4 al 8 (nota que 4 y 5 están en ambos)

# Demostraciones de operaciones básicas con conjuntos:
print(set_2.difference(set_1))     # Obtiene elementos que están en set_2 pero no en set_1 (6,7,8)
print(set_1.union(set_2))   # Une ambos conjuntos sin duplicar elementos (1,2,3,4,5,6,7,8)
print(set_1.intersection(set_2))  # Muestra elementos comunes entre ambos conjuntos (4,5)
print(set_1.symmetric_difference(set_2))  # Elementos que están en uno u otro conjunto, pero no en ambos (1,2,3,6,7,8)

# Ejemplo práctico: Eliminación de duplicados de una lista de razas
from utn_fra.datasets import lista_razas_pp

# Convertimos la lista a set para eliminar duplicados automáticamente
set_razas = set(lista_razas_pp)
# Convertimos de vuelta a lista para poder ordenarla
lista_razas_unicas = list(set_razas)
# Ordenamos la lista alfabéticamente
lista_razas_unicas.sort()
# Imprimimos la lista final de razas únicas ordenadas
print(lista_razas_unicas)

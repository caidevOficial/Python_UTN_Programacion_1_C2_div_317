"""
Contar Frecuencias con un Diccionario
Ejercicio: Dada la siguiente lista de palabras, usa un diccionario 
para contar y almacenar la frecuencia de cada palabra (cuántas veces aparece).
palabras = ["gato", "perro", "gato", "pez", "perro", "gato"]
"""

palabras = ["gato", "perro", "gato", "pez", "perro", "gato"]
diccionario_frecuencia = {}

for palabra in palabras:
    if palabra not in diccionario_frecuencia.keys():
        diccionario_frecuencia[palabra] = 1
    else:
        diccionario_frecuencia[palabra] = diccionario_frecuencia.get(palabra) + 1

print(diccionario_frecuencia)
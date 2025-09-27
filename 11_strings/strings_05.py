import random as rd

def formatear_como_flogger(texto: str) -> str:
    texto_salida = ''
    for caracter in texto:

        num_elegido = rd.randint(0, 1)
        if num_elegido == 0:
            texto_salida += caracter.upper()
        else:
            texto_salida += caracter.lower()


    return texto_salida
from utn_fra.datasets import (
    	lista_nombres_videos_small,
lista_vistas_videos_small,
lista_duraciones_videos_small
 )



print(formatear_como_flogger('Bienvenidos a la division 317 para aprender Python'))

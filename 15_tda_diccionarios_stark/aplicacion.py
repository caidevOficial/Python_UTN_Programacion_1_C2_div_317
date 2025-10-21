from menu import stark_menu_principal
from funciones import (
    stark_imprimir_heroe_genero,
    stark_calcular_imprimir_heroe_genero,
    stark_calcular_imprimir_promedio_altura_genero,
    stark_calcular_cantidad_por_tipo,
    stark_listar_heroes_por_dato
)

import os



def stark_marvel_app(lista_heroes: list[dict]) -> None:

    running = True
    lista_heroes_app = lista_heroes.copy()
    while running:

        
        opcion = stark_menu_principal()


        match opcion:
            case 1:
                stark_imprimir_heroe_genero(heroes=lista_heroes_app, genero='Masculino')
            case 2:
                stark_imprimir_heroe_genero(heroes=lista_heroes_app, genero='Femenino')
            case 3:
                stark_calcular_imprimir_heroe_genero(lista_heroes_app, calculo='maximo', key='altura_mts', valor_genero='Masculino')
            case 4:
                stark_calcular_imprimir_heroe_genero(lista_heroes_app, calculo='maximo', key='altura_mts', valor_genero='No-Binario')
            case 5:
                stark_calcular_imprimir_heroe_genero(lista_heroes_app, calculo='minimo', key='fuerza', valor_genero='Masculino')
            case 6:
                stark_calcular_imprimir_heroe_genero(lista_heroes_app, calculo='minimo', key='fuerza', valor_genero='Femenino')
            case 7:
                stark_calcular_imprimir_promedio_altura_genero(lista_heroes_app, key='fuerza', valor_genero='Masculino')
            case 8:
                stark_calcular_imprimir_promedio_altura_genero(lista_heroes_app, key='fuerza', valor_genero='Femenino')
            case 9:
                pass
            case 10:
                stark_calcular_cantidad_por_tipo(lista_heroes_app, tipo_de_dato='genero')
            case 11:
                stark_calcular_cantidad_por_tipo(lista_heroes_app, tipo_de_dato='raza')
            case 12:
                stark_calcular_cantidad_por_tipo(lista_heroes_app, tipo_de_dato='inteligencia')
            case 13:
                stark_listar_heroes_por_dato(lista_heroes_app, key='color_ojos')
            case 14:
                stark_listar_heroes_por_dato(lista_heroes_app, key='color_pelo')
            case 15:
                stark_listar_heroes_por_dato(lista_heroes_app, key='alineacion')
            case 16:
                print('Gracias por usar la aplicación.')
                running = False
        os.system('pause')
        os.system('cls') # 'clear' para UNIX (Mac/Linux)
            

if __name__ == '__main__':

    from utn_fra.datasets import lista_alias_pp

    print('Hola Mundo')
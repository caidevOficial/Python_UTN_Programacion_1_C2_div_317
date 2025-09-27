import os
import funciones as fun
import validaciones as val

def aplicacion(lista_poke_ids, lista_poke_nombres,
                lista_poke_tipos, lista_poke_poderes,
                lista_poke_condiciones):
    corriendo = True
    matriz_pokedex = []

    while corriendo:

        print("""
                1 - Crear Matriz
                2 - Mostrar existencias
                3 - Mostrar Datos Pokémons
                4 - Filtrar mas fuertes que promedio
                5 - Filtrar tipo Fuego
                6 - Filtrar tipo Eléctrico
                7 - Ordenar legandario DES
                8 - Ordenar normal ASC
                9 - trasponer y mostrar matriz
                10 - Salir
                """)
        opcion = val.validar_input(1, 10)

        match opcion:
            case 1:
                matriz_pokedex = fun.crear_matriz(lista_poke_ids, lista_poke_nombres,
                                    lista_poke_tipos, lista_poke_poderes,
                                    lista_poke_condiciones)
                print('Matriz Cargada')
                print(matriz_pokedex)
            case 2:
                if len(matriz_pokedex) != 0:
                    cantidad = fun.obtener_existencias(matriz_pokedex)
                    print(f'Hay {cantidad} pokémons')
                else:
                    print('ERROR: Inicializa la matriz en la opcion 1.')
            case 3:
                # validar que la matriz este cargada
                fun.mostrar_datos(matriz_pokedex)
            case 4:
                fun.mostrar_pokemones_poder_superior_promedio(matriz_pokedex)
            case 5:
                fun.mostrar_pokemones_tipo(matriz_pokedex, 'tipo', 'fuego')
            case 6:
                fun.mostrar_pokemones_tipo(matriz_pokedex, 'tipo', 'eléctrico')
            case 7:
                fun.filtrar_ordenar_pokemones(matriz_pokedex, 'condicion', 'legendario', tipo_orden='DES')
            case 8:
                fun.filtrar_ordenar_pokemones(matriz_pokedex, 'condicion', 'normal', tipo_orden='ASC')
            case 9:
                fun.trasponer_mostrar_matriz(matriz_pokedex)
            case 10:
                corriendo = False
        os.system('pause')
        os.system('cls')
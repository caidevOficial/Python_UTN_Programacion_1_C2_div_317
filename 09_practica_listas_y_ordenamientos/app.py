import os
import funciones_autos as autos

def automovilies(marcas: list, modelos: list, cantidades: list, precios: list):
    
    corriendo = True


    while corriendo:

        print(
            """
            1 - Recorrer la lista imprimiendo por consola el modelo de 
                autos que hay en cada garage
            2 - Recorrer la lista imprimiendo por consola el modelo de 
                autos que hay en cada garage junto con la cantidad que posee.
            3 - Recorrer las listas y determinar cuál es el modelo de auto 
                que más cantidad posee la concesionaria (MÁXIMO).
            4 - Recorrer las listas y determinar cuál es el modelo de auto 
                que menos cantidad posee la concesionaria (MÍNIMO).

            14 - Salir
            """
        )

        opcion = int(input('Ingrese una opcion: '))

        match opcion:
            case 1:
                autos.mostrar_modelos(modelos)
            case 2:
                autos.mostrar_modelo_y_cantidad(modelos, cantidades)
            case 3:
                autos.mostrar_modelo_con_cantidad(modelos, cantidades, modo='mayor')
            case 4:
                autos.mostrar_modelo_con_cantidad(modelos, cantidades, modo='menor')
            case 14:
                print('Gracias por visitarnos, compranos un autito!')
                corriendo = False
        
        os.system('pause')
        os.system('cls')
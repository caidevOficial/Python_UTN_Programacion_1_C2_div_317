import funciones as fn


def aplicacion(lista_a, lista_b, lista_c, lista_d):
    """
    
    """

    corriendo = True

    mensaje = f"""
            [1] Crear una matriz
            [2] Mostrar existencias
            [3] Mostrar Datos

            [11] Salir
                """

    mi_matriz = []
    while corriendo:

        print(mensaje)
        opcion = int(input("Seleccione una opcion: "))

        match opcion:
            case 1:
                mi_matriz = fn.crear_matriz(lista_a, lista_b, lista_c, lista_d)
                print("La matriz ya esta creada")
                print(mi_matriz)
            case 2:
                if len(mi_matriz) != 0:
                    existencias = fn.obtener_existencias(mi_matriz)
                    print (f"Hay {existencias} personajes!")
                else:
                    print ("Error! Inicializa primero la matriz")
            case 3:
                if len(mi_matriz) != 0:
                    fn.mostrar_datos(mi_matriz)
                else:
                    print ("Error! Inicializa primero la matriz")
            case 4:
                fn.filtrar_personaje(mi_matriz, 2, "n/a")
            case 7:
                fn.ordenar_matriz_segun_genero(mi_matriz, 2, 'female', modo='DES')
            case 8:
                fn.ordenar_matriz_segun_genero(mi_matriz, 3, 'male', modo='ASC')
            case 9:
                fn.ordenar_matriz_segun_genero(mi_matriz, 2, 'n/a', modo='ASC')
            case 11:
                print("Nos vemos!")
                corriendo = False
        

def validar_edad(edad_min: int, edad_max: int) -> int:
    edad = None
    flag = False
    while edad == None or not (edad_min <= edad <= edad_max):
        if flag:
            print(f'Edad incorrecta, ingrese un numero entre [{edad_min} - {edad_max}]:')
        edad_str = input(f'Ingrese su edad [{edad_min} - {edad_max}]: ')
        flag = True
        edad = int(edad_str)
    return edad


def validar_edad_recursiva(edad_min: int, edad_max: int, mostrar: bool = False) -> int:
    edad_str = input(f'Ingrese su edad [{edad_min} - {edad_max}]: ')
    edad = int(edad_str)

    if not (edad_min <= edad <= edad_max):
        print(f'Edad incorrecta, ingrese un numero entre [{edad_min} - {edad_max}]:')
        edad = validar_edad_recursiva(edad_min, edad_max, mostrar=False)
    
    if mostrar:
        print(f'Edad Correcta, su edad es: {edad}')
    return edad


# edad = validar_edad(18, 99)
edad = validar_edad_recursiva(18, 99, mostrar=True)
print(f'Print luego de las llamadas: EDAD: {edad}')
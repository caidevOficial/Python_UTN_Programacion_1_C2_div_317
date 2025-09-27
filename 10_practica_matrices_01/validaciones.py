
def validar_input(min: int, max: int) -> int:
    input_str = input(f'Ingrese su opción [{min} - {max}]: ')
    opcion = int(input_str)

    if not (min <= opcion <= max):
        print(f'Opción incorrecta, ingrese un numero entre [{min} - {max}]:')
        opcion = validar_input(min, max, mostrar=False)
    
    return opcion
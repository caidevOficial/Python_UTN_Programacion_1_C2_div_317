
def validar_input(texto: str) -> float:
    """
    ¿Que hace?

    ¿Que recibe por parametro?

    ¿Que retorna?
    """
    input_usuario = input(texto)
    valor = float(input_usuario)
    return valor

def validar_input_entre(minimo: int, maximo: int) -> int:
    input_usuario = input(f'Ingrese un número entre [{minimo} - {maximo}]: ')
    while not (minimo <= int(input_usuario) <= maximo):
        print('SYSTEM ERROR, numero incorrecto!!')
        input_usuario = input(f'Ingrese un número entre [{minimo} - {maximo}]: ')
    input_usuario_int = int(input_usuario)
    return input_usuario_int


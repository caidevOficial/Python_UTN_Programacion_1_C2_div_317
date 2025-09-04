
saludo = 'Hola División 317'

precio_base_original = 1500

def calcular_precio_con_iva(precio_sin_iva: float, iva: float = 21) -> float:
    """
    Calcula el iva y se lo agrega al precio sin iva, retornandolo

    :params: precio_sin_iva - El precio del producto sin iva
    :params: iva - El iva a agregarle al precio del producto

    :returns:
        Devuelve el precio del producto con el iva agregado
    """
    print(saludo)
    precio_con_iva = precio_sin_iva * (1 + iva / 100)
    return precio_con_iva

def pedir_dato_usuario(texto: str) -> float:
    """
    Pide un dato al usuario y retorna el input del usuario como un flotante

    :params: texto - Es el texto que el usuario va a ver en consola

    :returns: El valor que el usuario escribio, parseado a flotante
    """
    print(saludo)
    valor_str = input(f'SYSTEM UTN: {texto}')
    valor = float(valor_str)
    return valor





precio_base = pedir_dato_usuario('Ingrese un valor para calcularle el iva: ')
supuesto_iva = pedir_dato_usuario('Ingrese un iva [21 - 10.5]: ')

precio_calculado_con_iva = calcular_precio_con_iva(
    precio_sin_iva=precio_base_original, iva=supuesto_iva
)

print(f'El valor final con IVA {supuesto_iva}% es: {precio_calculado_con_iva}')

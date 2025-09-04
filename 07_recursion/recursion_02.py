
def obtener_maximo_comun_divisor(numero_a: int, numero_b: int) -> int:
    if numero_b == 0:
        return numero_a
    
    modulo_a_b = numero_a % numero_b
    resultado = obtener_maximo_comun_divisor(numero_b, modulo_a_b)
    return resultado

ma_co_di = obtener_maximo_comun_divisor(20, 15)
print(f'El MCD de 20 y 15 es: {ma_co_di}')
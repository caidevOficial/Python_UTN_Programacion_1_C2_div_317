import math

def sumar_dos_numeros(numero_a: float, numero_b: float) -> float:
    resultado = numero_a + numero_b
    return resultado

def restar_dos_numeros(numero_a: float, numero_b: float) -> float:
    resultado = numero_a - numero_b
    return resultado

def multiplicar_dos_numeros(numero_a: float, numero_b: float) -> float:
    resultado = numero_a * numero_b
    return resultado

def dividir_dos_numeros(numero_a: float, numero_b: float) -> float:
    resultado = numero_a / numero_b
    return resultado

def potencia_elevada(base: int, exponente: int) -> float:
    resultado = base ** exponente
    return resultado

def calcular_area_circulo(radio: float) -> float:
    res_potencia = potencia_elevada(radio, 2)
    resultado = multiplicar_dos_numeros(math.pi, res_potencia)
    return resultado

def calcular_area_rectangulo(base: float, altura: float) -> float:
    # BxH
    # BxH / 2 -> cuadrado
    resultado = multiplicar_dos_numeros(base, altura)
    return resultado

def calcular_area_de_triangulo(base: float, altura: float) -> float:
    # (BxH) / 2 -> triangulo
    res_mult = multiplicar_dos_numeros(base, altura)
    res_div = dividir_dos_numeros(res_mult, 2)
    return res_div

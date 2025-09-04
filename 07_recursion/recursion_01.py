
def calcular_factorial(numero: int) -> int:
    if numero == 1 or numero == 0:
        return 1
    else:
        anterior = numero - 1
        res_facto = numero * calcular_factorial(anterior)
        return res_facto

numero_str = input('Escriba un numero para ver su factorial: ')
numero = int(numero_str)

resultado = calcular_factorial(numero)

print(f'El factorial de {numero}! = {resultado}')
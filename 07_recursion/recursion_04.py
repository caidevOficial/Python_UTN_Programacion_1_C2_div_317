
def calcular_potencia_recursiva(base: int, exponente: int) -> int:
    if exponente == 0:
        return 1
    elif exponente % 2 == 0: # exponente par
        res_temp_par = calcular_potencia_recursiva(base, exponente // 2)
        return res_temp_par * res_temp_par
    else: # exponente impar
        res_temp_impar = base * calcular_potencia_recursiva(base, exponente - 1)
        return res_temp_impar

def calcular_potencia_recursiva(base: int, exponente: int) -> int:
    resultado = None
    if exponente == 0:
        resultado =  1
    elif exponente % 2 == 0: # exponente par
        res_temp_par = calcular_potencia_recursiva(base, exponente // 2)
        resultado =  res_temp_par * res_temp_par
    else: # exponente impar
        resultado = base * calcular_potencia_recursiva(base, exponente - 1)
    return resultado



resultado = calcular_potencia_recursiva(2, 8)
print(f'Resultado de 2 ** 8: {resultado}')
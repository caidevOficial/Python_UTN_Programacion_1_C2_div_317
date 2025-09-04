
# Realizar una función recursiva que calcule la suma de los primeros números naturales
# 5 -> los primeros 5 num nat. (A partir del 0)
def sumar_naturales(numero: int) -> int:
    if numero == 0:
        return numero
    
    anterior = numero - 1
    sub_total = numero + sumar_naturales(anterior)

    return sub_total


numero = int(input('Ingrese la cantidad de num nat a sumar desde el 0: '))
resultado = sumar_naturales(numero)

print(f'La suma es: {resultado}')

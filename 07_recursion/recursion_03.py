
def calcular_fibonacci_nro(numero_orden: int) -> int:
    if numero_orden < 2:
        return numero_orden
    
    else:
        # cada numero es la suma de sus dos anteriores
        ultimo = numero_orden - 1
        penultimo = ultimo - 1
        fibo_ultimo = calcular_fibonacci_nro(ultimo)
        fibo_penultimo = calcular_fibonacci_nro(penultimo)
        suma_fibo = fibo_ultimo + fibo_penultimo
        return suma_fibo

ubicacion = 3
resultado = calcular_fibonacci_nro(ubicacion)

print(f'El {ubicacion}° numero de la secuencia Fibonacci es: {resultado}')
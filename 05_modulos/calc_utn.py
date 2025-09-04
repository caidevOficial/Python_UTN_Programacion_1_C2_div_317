import matematico
import validaciones
import pantalla
import os


def calc_utn() -> None:
    """
    Funcion principal de la calculadora de la division 317
    El usuario puede elegir entre las 6 opciones del menú
    para realizar operaciones matematicas.

    Operaciones:
        Suma
        Resta
        Multiplicacion
        Division
        Potencia
        Área de círculo
        Área de rectángulo
    """
    
    corriendo = True

    while corriendo:

        pantalla.mostrar_menu()
        opcion = validaciones.validar_input_entre(minimo=1, maximo=9)

        if 1 <= opcion <= 5:
            numero_a = validaciones.validar_input('Escriba el 1° numero: ')
            numero_b = validaciones.validar_input('Escriba el 2° numero: ')
        elif opcion == 6:
            numero_a = validaciones.validar_input('Escriba el radio del circulo: ')
        elif 7 <= opcion <= 8:
            numero_a = validaciones.validar_input('Escriba la base: ')
            numero_b = validaciones.validar_input('Escriba la altura: ')
        


        match opcion:
            case 1:
                operacion = f'{numero_a} + {numero_b}'
                resultado = matematico.sumar_dos_numeros(numero_a=numero_a, numero_b=numero_b)
            case 2:
                operacion = f'{numero_a} - {numero_b}'
                resultado = matematico.restar_dos_numeros(numero_a=numero_a, numero_b=numero_b)
            case 3:
                operacion = f'{numero_a} * {numero_b}'
                resultado = matematico.multiplicar_dos_numeros(numero_a=numero_a, numero_b=numero_b)
            case 4:
                operacion = f'{numero_a} / {numero_b}'
                resultado = matematico.dividir_dos_numeros(numero_a=numero_a, numero_b=numero_b)
            case 5:
                operacion = f'{numero_a} ** {numero_b}'
                resultado = matematico.potencia_elevada(base=numero_a, exponente=numero_b)
            case 6:
                operacion = f'PI * {numero_a} ** 2'
                resultado = matematico.calcular_area_circulo(numero_a)
            case 7: # Área de rectángulo
                operacion = f'Area rectangulo'
                resultado = matematico.calcular_area_rectangulo(numero_a, numero_b)
            case 8: # Área de rectángulo
                operacion = f'Area triangulo'
                resultado = matematico.calcular_area_de_triangulo(numero_a, numero_b)
            case 9:
                corriendo = False
                print('Gracias, vuelva pronto!')

        if opcion != 9:
            print(f'El resultado de {operacion} es: {resultado}')
        
        os.system('pause')
        os.system('cls') # 'clear' -> UNIX

mi_nombre = None

while mi_nombre == None or not mi_nombre.isalpha():
    mi_nombre = input('Ingrese su nombre: ').upper()
    # mi_nombre = mi_nombre.lower()

print(f'Su nombre es: {mi_nombre}')
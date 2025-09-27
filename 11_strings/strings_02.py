
mi_edad = None

while mi_edad == None or not mi_edad.isdigit() or int(mi_edad) < 18:
    mi_edad = input('Ingrese su edad: ')

print(f'Su edad es: {mi_edad}')

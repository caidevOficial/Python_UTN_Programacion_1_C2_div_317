mi_lista_de_numeros = []
indices_de_impares = []




for vuelta in range(5):

    input_usuario = input('Ingrese un numero: ')
    input_usuario_int = int(input_usuario)

    mi_lista_de_numeros.append(input_usuario_int)


    # mi_lista_de_numeros.remove(2) # borramos primera ocurrencia de elemento
    # mi_lista_de_numeros.pop(4) # borramos elemento en el indice especificado


for indice in range(len(mi_lista_de_numeros)):

    elemento = mi_lista_de_numeros[indice]
    print(f'Indice n° {indice} -> elemento: {elemento}')


# si el numero es par: elevarlo al cubo, sino elevarlo al cuadrado
for indice in range(len(mi_lista_de_numeros)):

    elemento = mi_lista_de_numeros[indice]
    if elemento % 2 == 0: # es par
        print('========== ELEVADO AL CUBO')
        print(f'PM: Indice n° {indice} -> {elemento}')
        mi_lista_de_numeros[indice] = elemento ** 3
        print(f'PostM: Indice n° {indice} -> {mi_lista_de_numeros[indice]}')
        print('==========')
    else: # es impar
        # print('========== ELEVADO AL CUADRADO')
        # print(f'PM: Indice n° {indice} -> {elemento}')
        # mi_lista_de_numeros[indice] = elemento ** 2
        # print(f'PostM: Indice n° {indice} -> {mi_lista_de_numeros[indice]}')
        # print('==========')
        indices_de_impares.append(indice)

print(f'Indices a borrar: {indices_de_impares}')

# [2,6]
print(f'Lista original: {mi_lista_de_numeros}')

ultimo_indice = len(indices_de_impares) -1
for indice in range(ultimo_indice, -1, -1):
    indice_a_borrar = indices_de_impares[indice]

    mi_lista_de_numeros.pop(indice_a_borrar)

print(f'Lista original depurada: {mi_lista_de_numeros}')


    
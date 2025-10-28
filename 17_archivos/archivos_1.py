texto = 'Hoy es Lunes y estamos aprendiendo a manejar archivos'

FILE_PATH = './17_archivos/mi_texto.txt'

# Lectura

archivo = open(FILE_PATH, mode='r', encoding='UTF-8')

# contenido = archivo.read()
# lista_contenido = archivo.readlines()

# for row_index in range(len(lista_contenido)):
#     lista_contenido[row_index] = lista_contenido[row_index].replace('\n', '')

contenido = archivo.read()

print(contenido)

archivo.close()

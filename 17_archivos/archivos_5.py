texto = 'Hoy es Lunes y estamos aprendiendo a manejar archivos'

FILE_PATH = './17_archivos/mi_texto_z.txt'

archivo = open(FILE_PATH, 'a', encoding='UTF-8')

contenido = archivo.write(f'\n\n{texto}')

print(contenido)

archivo.close()
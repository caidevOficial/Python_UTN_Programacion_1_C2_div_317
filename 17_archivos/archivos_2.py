texto = 'Hoy es Lunes y estamos aprendiendo a manejar archivos'

FILE_PATH = './17_archivos/mi_texto_w.txt'

archivo = open(FILE_PATH, 'w', encoding='UTF-8')

archivo.write(texto)

archivo.close()
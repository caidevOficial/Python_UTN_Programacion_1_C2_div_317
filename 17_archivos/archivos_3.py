texto = 'Hoy es Lunes y estamos aprendiendo a manejar archivos'

FILE_PATH = './17_archivos/mi_texto_w.txt'

archivo = open(FILE_PATH, 'r+', encoding='UTF-8')

contenido = archivo.read()
print(contenido)
archivo.write(texto)

archivo.seek(0)

contenido = archivo.readlines()
print(contenido)


archivo.close()
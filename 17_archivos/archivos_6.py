texto = 'El pato ñato esta volando  óóó áaaá'

FILE_PATH = './17_archivos/mi_texto_z.txt'

archivo = open(FILE_PATH, 'a+', encoding='UTF-8')


archivo.write(f'\n{texto}\n')
archivo.seek(0)
contenido = archivo.read()
print(contenido)

archivo.close()
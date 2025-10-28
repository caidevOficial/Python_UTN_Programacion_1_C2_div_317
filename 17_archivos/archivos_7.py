texto = 'El pato ñato esta volando  óóó áaaá'

FILE_PATH = './17_archivos/mi_texto_z.txt'

with open(FILE_PATH, 'r', encoding='UTF-8') as archivo:
    contenido = archivo.readlines()

    for linea in contenido:
        print(linea)


print('Terminado!')
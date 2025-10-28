FILE_PATH = './17_archivos/mi_texto_z.txt'
FILE_LOG = './17_archivos/system_logs.txt'

def leer_archivo_texto(ruta: str) -> str:
    content = ''
    with open(ruta, 'r', encoding='utf-8') as file:
        content = file.readlines()
    
    return content

def escribir_texto(ruta: str, contenido: str, anexar: bool = False) -> int:
    lineas = 0
    modo = 'w'
    if anexar == True:
        modo = 'a'

    with open(ruta, modo, encoding='utf-8') as file:
        lineas = file.write(contenido)
    return lineas

# mi_texto = leer_archivo_texto(FILE_PATH)

import datetime


fecha_hoy = datetime.datetime.now()
error = f'{fecha_hoy} -> Fallo la lectura de archivos\n'

lineas = escribir_texto(FILE_LOG, contenido=error, anexar=True)
print(lineas)
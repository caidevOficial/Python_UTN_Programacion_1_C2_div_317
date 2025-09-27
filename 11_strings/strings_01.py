texto = "   Bienvenidos a la división 317 para aprender Python    "

sub_texto = texto[10:18]
print(f'Caracteres totales: {len(texto)}')


for indice in range(len(texto)):
    texto[indice] = '1'
    print(texto[indice])

for caracter in texto:
    print(caracter)
    
import copy as deepcopy

lista_original = [
    ["Papa", "Lechuga", "Tomate"],
    ["Pepsi", "Coca", "Sprite"]
]



# Deep Copy
lista_copia = deepcopy.deepcopy(lista_original)


dir_mem_1 = hex(id(lista_original))
dir_mem_2 = hex(id(lista_copia))

lista_copia[0][0] = 'Palta'

lista_copia[1] = ["Manaos", "Sprite", "Pepsi"]

print(f'LO: {dir_mem_1} | LC: {dir_mem_2}')

for indice in range(len(lista_original)):
    d_m_1 = hex(id(lista_original[indice]))
    d_m_2 = hex(id(lista_copia[indice]))

    print(f'E-LO: {lista_original[indice]} | E-LC: {lista_copia[indice]}')
    print(f' ---- E-LO: {d_m_1} | E-LC: {d_m_2}')
    
    if type(lista_original[indice]) == list:

        for sub_elmt in range(len(lista_original[indice])):


            s_d_m_1 = hex(id(lista_original[indice][sub_elmt]))
            s_d_m_2 = hex(id(lista_copia[indice][sub_elmt]))
            print(f' ---- SE-LO: {lista_original[indice][sub_elmt]} | SE-LC: {lista_copia[indice][sub_elmt]}')
            print(f' -------- E-LO: {s_d_m_1} | E-LC: {s_d_m_2}')








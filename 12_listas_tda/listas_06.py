lista_bebidas_1 = ["Pepsi", "Coca", "Manaos"]
lista_bebidas_2 = ["Buhero", "Branca", "Odone", "Secco"]

for gaseosa, fernet in zip(lista_bebidas_1, lista_bebidas_2):
    print(f'{gaseosa} - {fernet}')
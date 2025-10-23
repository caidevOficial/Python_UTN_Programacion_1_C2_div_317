from game import run_game
from utn_fra.datasets import (
    lista_diccionario_heroes
)

if __name__ == '__main__':
    
    run_game(game_name='Visualizador de heroes', heroes=lista_diccionario_heroes)
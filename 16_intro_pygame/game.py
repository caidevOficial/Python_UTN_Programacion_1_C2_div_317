import pygame as pg
import sys
from variables import (
    ASPECT_RATIO, COLOR_AZUL, DIMENSION_ESFERA,
    PIXELES_MOV, PATH_ESFERA_IMG
)
import random as rd

def set_main_game_configs(game_name: str) -> dict:
    img_esfera = pg.image.load(PATH_ESFERA_IMG)
    configs = {
        'icono_surface': pg.image.load(PATH_ESFERA_IMG),
        # main_display: pg.display.set_mode(ASPECT_RATIO, pg.RESIZABLE)
        'main_display': pg.display.set_mode(ASPECT_RATIO),
        'img_esfera': pg.transform.scale_by(img_esfera, 0.15),
        'posicion_inicial': [0,0],
        'color_fondo': pg.Color('black'),
        'running_state': True
    }

    pg.display.set_caption(game_name)
    pg.display.set_icon(configs.get('icono_surface'))

    return configs

def manejador_de_eventos(configs: dict):

    for event in pg.event.get():

        if event.type == pg.QUIT:
            configs['running_state'] = False
        
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT and configs.get('posicion_inicial')[0] >= PIXELES_MOV:
                configs.get('posicion_inicial')[0] -= PIXELES_MOV
            elif event.key == pg.K_RIGHT and configs.get('posicion_inicial')[0] <= (ASPECT_RATIO[0] - (DIMENSION_ESFERA[0] + PIXELES_MOV)):
                configs.get('posicion_inicial')[0] += PIXELES_MOV
            elif event.key == pg.K_UP and configs.get('posicion_inicial')[1] >= PIXELES_MOV:
                configs.get('posicion_inicial')[1] -= PIXELES_MOV
            elif event.key == pg.K_DOWN and configs.get('posicion_inicial')[1] <= (ASPECT_RATIO[1] - (DIMENSION_ESFERA[1] + PIXELES_MOV)):
                configs.get('posicion_inicial')[1] += PIXELES_MOV
        elif event.type == pg.MOUSEBUTTONDOWN:
            print(event)
            if event.button == 1:
                background_color_name = rd.choice(['cyan', 'red', 'blue', 'black', 'pink'])
                configs['color_fondo'] = pg.Color(background_color_name)

                print('Guardando imagen')
                pg.image.save(configs.get('img_esfera'), '16_intro_pygame/ESFERA_317.png')
                
                coordenada_click = list(event.pos)
                # (300x , 400y) -> (0,0)
                centro_imagen = [
                    coordenada_click[0] - DIMENSION_ESFERA[0] // 2,
                    coordenada_click[1] - DIMENSION_ESFERA[1] // 2,
                ]
                configs['posicion_inicial'] = centro_imagen

def cerrar_juego():
    print('Cerrando el juego')
    pg.quit()
    sys.exit()

def run_game(game_name: str):

    configs = set_main_game_configs(game_name)
    
    while configs.get('running_state'):

        manejador_de_eventos(configs)

        configs.get('main_display').fill(configs.get('color_fondo'))
        esfera_rect = configs.get('img_esfera').get_rect()
        configs.get('main_display').blit(source=configs.get('img_esfera'), dest=configs.get('posicion_inicial'), area=esfera_rect)

        pg.display.update()

    cerrar_juego()
    
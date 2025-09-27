from utn_fra.datasets import (
    lista_poke_ids, lista_poke_nombres,
    lista_poke_tipos, lista_poke_poderes,
    lista_poke_condiciones, lista_sw_alturas
 )
import aplicacion as appli

appli.aplicacion(lista_poke_ids, lista_poke_nombres,
                lista_poke_tipos, lista_poke_poderes,
                lista_poke_condiciones)

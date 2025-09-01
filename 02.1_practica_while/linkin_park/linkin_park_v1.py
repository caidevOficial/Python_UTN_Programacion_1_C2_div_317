# Copyright (C) 2023 <UTN FRA>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import warnings
from utn_fra.pygame_widgets.game_sound import GameSound


'''
################# INTRODUCCION #################
#? Se nos ha solicitado desarrollar una aplicación para llevar registro de las 
#? entradas vendidas en el Parque de la Ciudad, para el concierto de Linkin Park. 
#? Para ello, se solicitará al usuario la siguiente información al momento de 
#? comprar cada entrada:
'''
NOMBRE = 'Facu' # Completa tu nombre completo solo en esa variable
'''
#?################ ENUNCIADO #################
A) Para ello deberas programar el boton "Cargar Ventas" para poder cargar 10 ventas.
Los datos que deberas pedir para los ventas son:
    * Nombre del comprador
    * Edad (no menor a 18)
    * Género (Masculino, Femenino, Otro)
    * Tipo de entrada (General, Campo delantero, Vip)
    * Medio de pago (Crédito, Efectivo, Débito) 
    * Precio de la entrada (Se debe calcular)

Para cada venta, se calculará el total a pagar en función del tipo de entrada elegida, 
el medio de pago y su precio correspondiente.

 * Lista de precios: 
        * General:           $90000
        * Campo delantero:   $180000
        * Vip:               $230000

Las entradas adquiridas con tarjeta de crédito tendrán un 10% de descuento sobre el 
precio de la entrada, mientras que las adquiridas con tarjeta de débito un 20%. 


#!################ ACLARACION IMPORTANTE #################
Del punto B SOLO debera realizar DOS informes.
Para determinar que informe hacer, tenga en cuenta lo siguiente:

    1- Tome el ultimo numero de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)
    2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). 
        Realiza el informe correspondiente al numero obtenido. En caso de que su DNI 
        finalice con el número 0, deberá realizar el informe 9.

EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 
B) INFORMES
    #! 0) - Cantidad total de dinero recaudado por las ventas de entradas.
    #! 1) - Cantidad de entradas vendidas para cada tipo.
    #! 2) - Promedio de edad de las personas que compraron ubicación VIP.
    #! 3) - Nombre de la persona de mayor edad que compró una entrada VIP.
    #! 4) - Porcentaje de entradas vendidas de tipo "General"
    #! 5) - Porcentaje de entradas vendidas de tipo "Campo delantero"
    #! 6) - Nombre de la/s persona/s de mayor edad, de género Femenino que compro una 
    #!       entrada VIP.
    #! 7) - Nombre de la/s persona/s de menor edad, de género Masculino que compro una 
    #!       entrada general.
    #! 8) - Tipo de entradas más vendidas.
    #! 9) - Tipo de entradas menos vendidas.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title(f"UTN FRA - Punto de Venta {NOMBRE} [From Zero World Tour]")
        self.minsize(320, 250)

        self.audio_path = './linkin_park/linkin_park.ogg'
        self.audio_manager = GameSound()
        self.audio_manager.play_music(self.audio_path, volume = 0.4)
        
        self.label_title = customtkinter.CTkLabel(master=self, text=f"Punto de Venta {NOMBRE} [From Zero World Tour]", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        
        self.image = tk.PhotoImage(file='./linkin_park/UTN_PuntoVenta_LP_App_v1.png')
        self.top_banner = customtkinter.CTkLabel(master = self, image = self.image, text = '')
        self.top_banner.grid_configure(row = 1, column = 0, padx = 20, pady = 5, columnspan = 2, rowspan = 1, sticky = 'we')

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Ventas", command=self.btn_cargar_ventas_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")


    def btn_cargar_ventas_on_click(self):
        # Desarrollá la lógica debajo
        datos_tomados = 0
        limite_de_datos = 3
        edad_minima = 18
        """
        * General:           $90000
        * Campo delantero:   $180000
        * Vip:               $230000
        """
        precio_general = 90000
        precio_campo = 180000
        precio_vip = 230000
        recaudacion_total = 0
        descuento_credito = 0.9
        descuento_debito = 0.8
        cant_general = 0
        cant_vip = 0
        cant_campo = 0
        suma_edades_vip = 0
        cant_ventas_vip = 0
        nombre_mayor_vip = None
        edad_mayor_vip = None
        edad_menor_gral = None
        # edad_mayor_vip = -1
        femeninas_entradas_vip = ''
        masculinos_entradas_gral = ''

        # toma de datos

        while datos_tomados < limite_de_datos:
            
            """
            * Nombre del comprador
            * Edad (no menor a 18)
            * Género (Masculino, Femenino, Otro)
            * Tipo de entrada (General, Campo delantero, Vip)
            * Medio de pago (Crédito, Efectivo, Débito) 
            * Precio de la entrada (Se debe calcular)
            """
            
            nombre_actual = None
            while nombre_actual == None:
                nombre_actual = input('Ingrese su nombre: ')
            
            edad_actual_int = None
            while edad_actual_int == None or edad_actual_int < edad_minima:
                edad_actual = input('Ingrese su edad: ')
                edad_actual_int = int(edad_actual)

            genero_actual = None # (Masculino, Femenino, Otro)
            while genero_actual != 'm' and genero_actual != 'f' and genero_actual != 'o':
                genero_actual = input('Ingrese su género: [m/f/o]')
            
            tipo_entrada_actual = None # (General, Campo delantero, Vip)
            while tipo_entrada_actual != 'general' and tipo_entrada_actual != 'campo' and tipo_entrada_actual != 'vip':
                tipo_entrada_actual = input('Ingrese tipo entrada [general - campo - vip]: ')
            

            # tipo_entrada_actual = None # (General, Campo delantero, Vip)
            # while tipo_entrada_actual != '1' and tipo_entrada_actual != '2' and tipo_entrada_actual != '3':
            #     tipo_entrada_actual = input('Ingrese numero de tipo entrada: [1 - General | 2 - Campo | 3 - Vip]: ')


            tipo_pago_actual = None # (credito, Campo efectivo, debito)
            while tipo_pago_actual != 'credito' and tipo_pago_actual != 'efectivo' and tipo_pago_actual != 'debito':
                tipo_pago_actual = input('Ingrese tipo de pago [credito - efectivo - debito]: ')
                        

            datos_tomados += 1


            #! 0) - Cantidad total de dinero recaudado por las ventas de entradas.
            # Valor base de la entrada [sin descuentos]
            ##! 1) - Cantidad de entradas vendidas para cada tipo.
            #! 2) - Promedio de edad de las personas que compraron ubicación VIP.
            #! 3) - Nombre de la persona de mayor edad que compró una entrada VIP.
            costo_base = None
            match tipo_entrada_actual:
                case 'campo':
                    costo_base = precio_campo
                    cant_campo += 1
                case 'general':
                    costo_base = precio_general
                    cant_general += 1
                    #! 7) - Nombre de la/s persona/s de menor edad, de género Masculino que compro una 
                    #!       entrada general.
                    if edad_menor_gral == None or edad_actual_int < edad_menor_gral:
                        if genero_actual == 'm':
                            edad_menor_gral = edad_actual_int
                            masculinos_entradas_gral = nombre_actual
                    elif genero_actual == 'm' and edad_actual_int == edad_menor_gral:
                        masculinos_entradas_gral = f'{masculinos_entradas_gral},{nombre_actual}'
                case 'vip':
                    costo_base = precio_vip
                    cant_vip += 1
                    cant_ventas_vip += 1
                    suma_edades_vip += edad_actual_int

                    # Calculamos el mayor para reemplazar sus datos
                    # y obtener el nombre y edad

                    #! 6) - Nombre de la/s persona/s de mayor edad, de género Femenino que compro una 
                    #!       entrada VIP.
                    if edad_mayor_vip == None or edad_actual_int > edad_mayor_vip:
                        edad_mayor_vip = edad_actual_int
                        nombre_mayor_vip = nombre_actual
                        if genero_actual == 'f':
                            femeninas_entradas_vip = nombre_actual
                    elif edad_actual_int == edad_mayor_vip and genero_actual == 'f':
                        femeninas_entradas_vip = f'{femeninas_entradas_vip},{nombre_actual}'

            costo_entrada_actual = None
            if tipo_pago_actual == 'credito':
                costo_entrada_actual = costo_base * descuento_credito
            elif tipo_pago_actual == 'debito':
                costo_entrada_actual = costo_base * descuento_debito
            else:
                costo_entrada_actual = costo_base


            recaudacion_total += costo_entrada_actual

        # analisis de datos
        
        if cant_ventas_vip > 0:
            promedio_edad_vip = suma_edades_vip / cant_ventas_vip
        else:
            promedio_edad_vip = 0
        #! 4) - Porcentaje de entradas vendidas de tipo "General"
        #! 5) - Porcentaje de entradas vendidas de tipo "Campo delantero"
        porcentaje_general = cant_general * 100 / datos_tomados
        porcentaje_campo = cant_campo * 100 / datos_tomados

        #! 8) - Tipo de entradas más vendidas.

        if cant_vip > cant_general and cant_vip > cant_campo:
            mas_vendidas = 'VIP'
        elif cant_general > cant_campo:
            mas_vendidas = 'GRAL'
        else:
            mas_vendidas = 'CAMPO'


        #! 9) - Tipo de entradas menos vendidas.
        if cant_vip < cant_general and cant_vip < cant_campo:
            menos_vendidas = 'VIP'
        elif cant_general < cant_campo:
            menos_vendidas = 'GRAL'
        else:
            menos_vendidas = 'CAMPO'



        # Mostrar informes
        data_informe =\
            f"""
            #0 - Recaudacion total: ${recaudacion_total}
            #1 - Cantidad Vendidas:
                    General: {cant_general}
                    Campo: {cant_campo}
                    Vip: {cant_vip}
            #2 - Promedio edad personas Vip: {promedio_edad_vip} años.
            #3 - Nombre persona mayor q compro vip: {nombre_mayor_vip}.
            #4 - Porcentaje entradas vendidas General: {porcentaje_general} un.
            #5 - Porcentaje entradas vendidas Campo: {porcentaje_campo} un.
            #6 - Mujeres Mayor edad Vip: {femeninas_entradas_vip}
            #7 - Hombres Menor edad Gral: {masculinos_entradas_gral}.
            #8 - Entradas Mas vendidas: {mas_vendidas}.
            #9 - Entradas Menos vendidas: {menos_vendidas}.
            """
        alert('Informe', message=data_informe)

    
if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    app = App()
    app.mainloop()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2024 Eón Corp

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import streamlit as st
orbn_hdpe = 0.75*(0.83*0.18+4.16*0.2)
orbn_ldpe = 0.75*(1.67*0.22+4.16*0.2)
orbn_pet = 0.75*(1.11*0.18+4.16*0.2)
orbn_papel = 0.82*(4.98*0.18)
orbn_vidrio = 0.88*(0.026*0.22)
orbn_aluminio = (8.4*0.72)
orbn_acero = 1.27*0.68

rbr_hdpe = 0.83*0.18
rbr_ldpe = 0.83*0.18
rbr_pet= 0.83*0.18
rbr_papel = 1.47*0.18
rbr_vidrio = 0.00028*0.18
rbr_aluminio = 0.66*0.18
rbr_acero = 0.9*0.18

hdpe = 0
ldpe = 0
pet = 0
papel = 0
vidrio = 0
aluminio = 0
acero = 0

def degradacion_organica_papel(cantidad, degradacion=8.95):
    if abs(cantidad) != 0.0:
        return cantidad * degradacion
    return 0.0

def calcular_reduccion_emisiones(cantidad, orbn, rbr):
    if abs(cantidad) != 0.0:
        reduccion = (cantidad * orbn - cantidad * rbr) - 0.001
        return reduccion
    return 0.0

def calculo_galones_gasolina(cantidad):
    if abs(cantidad) != 0.0:
        reduccion = cantidad * 1000000 / 8887
        return reduccion
    return 0.0

def calculo_galones_diesel(cantidad):
    if abs(cantidad) != 0.0:
        reduccion = cantidad * 1000000 / 10180
        return reduccion
    return 0.0

def calculo_bolsas_basura(cantidad):
    if abs(cantidad) != 0.0:
        reduccion = cantidad * 1000000 / 23000
        return reduccion
    return 0.0

def calculo_camiones_basura(cantidad):
    if abs(cantidad) != 0.0:
        reduccion = cantidad * 1000000 / 20160000
        return reduccion
    return 0.0



col1, col2 = st.columns(2)
with col1:
    # Opciones para el combo box
    options = ['Toneladas', 'Kilogramos']

# Seleccionar una opción
    selected_option = st.selectbox('Selecciona una unidad de peso:', options)

# Multiplicar por 1000 si se selecciona "Kilogramos"
    if selected_option == 'Kilogramos':
        factor = 1000
    else:
        factor = 1
    hdpe = st.number_input("HDPE/PP",format="%.5f")
    ldpe = st.number_input("LDPE",format="%.5f")
    pet = st.number_input("PET/PS",format="%.5f")
    papel = st.number_input("Papel/Cartón",format="%.5f")
    vidrio = st.number_input("Vidrio",format="%.5f")
    aluminio = st.number_input("Aluminio",format="%.5f")
    acero = st.number_input("Acero",format="%.5f")

    red_hdpe=calcular_reduccion_emisiones(hdpe/factor, orbn_hdpe, rbr_hdpe)
    red_ldpe=calcular_reduccion_emisiones(ldpe/factor,orbn_ldpe,rbr_ldpe)
    red_pet=calcular_reduccion_emisiones(pet/factor,orbn_pet ,rbr_pet)
    red_papel=calcular_reduccion_emisiones(papel/factor,orbn_papel ,rbr_papel)
    red_vidrio=calcular_reduccion_emisiones(vidrio/factor,orbn_vidrio ,rbr_vidrio)
    red_aluminio=calcular_reduccion_emisiones(aluminio/factor,orbn_aluminio, rbr_aluminio)
    red_acero=calcular_reduccion_emisiones(acero/factor,orbn_acero ,rbr_acero)

    red_total = red_hdpe+red_ldpe+red_pet+red_papel+red_vidrio+red_aluminio+red_acero
with col2:
    degradacion = degradacion_organica_papel(papel)
    equivalencia = red_total+degradacion
    st.markdown("## Reduccion total de CO2 {:.2f}".format(equivalencia))
    if degradacion:
        st.markdown("## Reduccion de CO2 debido a degradacion de papel {:.2f}".format(degradacion))

    col3, col4 = st.columns([4,9])
    with col3:
        st.image("bomba-de-gasolina.png", width=100,caption="Gasolina")
        st.image("bomba-de-gasolina.png", width=100,caption="Diesel")
        st.image("bolsa-de-basura.png", width=100,caption="Bolsas de basura")
        st.image("camion-de-la-basura.png", width=100,caption="Camion de basura")
    with col4:
        st.markdown("## {:.2f} galones de gasolina ahorrados".format(calculo_galones_gasolina(equivalencia)))
        st.markdown("## {:.2f} galones de diesel ahorrados".format(calculo_galones_diesel(equivalencia)))
        st.markdown("## {:.2f} bolsas de basura recicladas".format(calculo_bolsas_basura(equivalencia)))
        st.markdown("## {:.2f} camiones de basura recicladas".format(calculo_camiones_basura(equivalencia)))

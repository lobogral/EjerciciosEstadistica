from sys import path
path.append("../")

from Comandos.medidasPosición import *
from Comandos.gráficas import *
from Comandos.otros import *

escribir("1.1")
escribir("Mediciones tiempo de secado en pintura (horas)")
muestra = [3.4, 2.5, 4.8, 2.9, 3.6,
           2.8, 3.3, 5.6, 3.7, 2.8,
           4.4, 4.0, 5.2, 3.0, 4.8]
escribir(muestra)
escribir("a) Tamaño de la muestra =", tamaño(muestra), "datos")
escribir("b) Media de la muestra =", media(muestra, 3), "horas")
escribir("c) Mediana de la muestra =", mediana(muestra, 3), "horas")
#dibujar("puntos", muestra, "d) Análisis pintura esmaltada","Tiempo secado (horas)")
escribir("e) x_tr(20) =", mediaRecortada(muestra, 3, 0.2), "horas")


escribir("")
escribir("1.3")
escribir("Mediciones resistencia a la tensión en aviones (psi)")
escribir("Sin envejecimiento acelerado")
muestra1 = [227, 222, 218, 217, 225,
            218, 216, 229, 228, 221]
escribir(muestra1)
escribir("Con envejecimiento acelerado")
muestra2 = [219, 214, 215, 211, 209,
            218, 203, 204, 201, 205]
escribir(muestra2)
#dibujar("puntos", muestra2, "a) Análisis aviones","Resistencia tensión (psi)")
#dibujar("puntos", muestra1, "a) Análisis aviones","Resistencia tensión (psi)")
escribir("c)")
escribir("Media Envejecimiento =", media(muestra2, 2), "psi")
escribir("Media NoEnvejecimiento =", media(muestra1, 2), "psi")
escribir("d)")
escribir("Mediana Envejecimiento =", mediana(muestra2, 2), "psi")
escribir("Mediana NoEnvejecimiento =", mediana(muestra1, 2), "psi")


escribir("")
escribir("1.5")
escribir("Mediciones reducción de Colesterol en personas (mg/dL)")
escribir("Grupo de control")
muestra1 = [7,  3, -4, 14, 2,
         5, 22, -7,  9, 5]
escribir(muestra1)
escribir("Grupo de tratamiento")
muestra2 = [-6,  5, 9, 4, 4,
         12, 37, 5, 3, 3]
escribir(muestra2)
#dibujar("puntos", muestra1, "a) Análisis personas","Reducción colesterol (mg/dL)")
#dibujar("puntos", muestra2, "a) Análisis personas","Reducción colesterol (mg/dL)")
escribir("b)")
escribir("Control")
escribir("x_ =", media(muestra1, 2), "mg/dL")
escribir("x~ =", mediana(muestra1, 2), "mg/dL")
escribir("x_tr(10) =", mediaRecortada(muestra1, 3, 0.1), "mg/dL")
escribir("Tratamiento")
escribir("x_ =", media(muestra2, 2), "mg/dL")
escribir("x~ =", mediana(muestra2, 2), "mg/dL")
escribir("x_tr(10) =", mediaRecortada(muestra2, 3, 0.1), "mg/dL")


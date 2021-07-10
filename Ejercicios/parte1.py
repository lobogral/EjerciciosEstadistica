from sys import path
path.append("../")

from Comandos.medidasPosición import *
from Comandos.gráficas import *
from Comandos.otros import *

escribir("1.1")
muestra = [3.4, 2.5, 4.8, 2.9, 3.6,
           2.8, 3.3, 5.6, 3.7, 2.8,
           4.4, 4.0, 5.2, 3.0, 4.8]
escribir("Mediciones tiempo de secado (horas)")
escribir(muestra)
escribir("a) Tamaño de la muestra =", tamaño(muestra), "datos")
escribir("b) Media de la muestra =", media(muestra, 3), "horas")
escribir("c) Mediana de la muestra =", mediana(muestra, 3), "horas")
dibujarGraficaPuntos(muestra, "d)", "pintura esmaltada","Tiempo secado (horas)")
escribir("e) x_tr(20) =", mediaRecortada(muestra, 3, 0.2), "horas")


escribir("")
escribir("1.3")
muestra = [227, 222, 218, 217, 225,
         218, 216, 229, 228, 221]
escribir(muestra)
escribir("Media NoEnvejecimiento =", media(muestra, 2))
escribir("Mediana NoEnvejecimiento =", mediana(muestra, 2))
muestra = [219, 214, 215, 211, 209,
         218, 203, 204, 201, 205]
escribir(muestra)
escribir("Media Envejecimiento =", media(muestra, 2))
escribir("Mediana Envejecimiento =", mediana(muestra, 2))


escribir("")
escribir("1.5")
muestra = [7,  3, -4, 14, 2,
         5, 22, -7,  9, 5]
escribir(muestra)
escribir("Control")
escribir("x_ =", media(muestra, 2))
escribir("x~ =", mediana(muestra, 2))
escribir("x_tr(10) =", mediaRecortada(muestra, 3, 0.1))
muestra = [-6,  5, 9, 4, 4,
         12, 37, 5, 3, 3]
escribir(muestra)
escribir("Tratamiento")
escribir("x_ =", media(muestra, 2))
escribir("x~ =", mediana(muestra, 2))
escribir("x_tr(10) =", mediaRecortada(muestra, 3, 0.1))


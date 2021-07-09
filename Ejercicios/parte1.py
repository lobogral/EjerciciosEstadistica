from sys import path
path.append("../")

from Comandos.medidasPosición import *
from Comandos.otrosComandos import *

print("1.1")
muestra = [3.4, 2.5, 4.8, 2.9, 3.6,
           2.8, 3.3, 5.6, 3.7, 2.8,
           4.4, 4.0, 5.2, 3.0, 4.8]
print(muestra)
print("Tamaño de la muestra =", tamaño(muestra))
print("Media de la muestra =", media(muestra, 3))
print("Mediana de la muestra =", mediana(muestra, 3))
print("x_tr(20) =", mediaRecortada(muestra, 3, 0.2))


print("")
print("1.3")
muestra = [227, 222, 218, 217, 225,
         218, 216, 229, 228, 221]
print(muestra)
print("Media NoEnvejecimiento =", media(muestra, 2))
print("Mediana NoEnvejecimiento =", mediana(muestra, 2))
muestra = [219, 214, 215, 211, 209,
         218, 203, 204, 201, 205]
print(muestra)
print("Media Envejecimiento =", media(muestra, 2))
print("Mediana Envejecimiento =", mediana(muestra, 2))


print("")
print("1.5")
muestra = [7,  3, -4, 14, 2,
         5, 22, -7,  9, 5]
print(muestra)
print("Control")
print("x_ =", media(muestra, 2))
print("x~ =", mediana(muestra, 2))
print("x_tr(10) =", mediaRecortada(muestra, 3, 0.1))
muestra = [-6,  5, 9, 4, 4,
         12, 37, 5, 3, 3]
print(muestra)
print("Tratamiento")
print("x_ =", media(muestra, 2))
print("x~ =", mediana(muestra, 2))
print("x_tr(10) =", mediaRecortada(muestra, 3, 0.1))


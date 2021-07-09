from sys import path
path.append("../")

from Comandos.medidasVariabilidad import *
from Comandos.otros import *

escribir("1.7")
muestra = [3.4, 2.5, 4.8, 2.9, 3.6,
           2.8, 3.3, 5.6, 3.7, 2.8,
           4.4, 4.0, 5.2, 3.0, 4.8]
escribir(muestra)
escribir("Varianza de la muestra =", varianza(muestra, 3))
escribir("Desviación estándar de la muestra =", desviaciónEstándar(muestra, 3))

escribir("")
escribir("1.9")
muestra = [227, 222, 218, 217, 225,
         218, 216, 229, 228, 221]
escribir(muestra)
escribir("Sin envejecimiento")
escribir("Varianza de la muestra =", varianza(muestra, 2))
escribir("Desviación estándar de la muestra =", desviaciónEstándar(muestra, 2))
muestra = [219, 214, 215, 211, 209,
         218, 203, 204, 201, 205]
escribir(muestra)
escribir("Con envejecimiento")
escribir("Varianza de la muestra =", varianza(muestra, 2))
escribir("Desviación estándar de la muestra =", desviaciónEstándar(muestra, 2))


escribir("")
escribir("1.11")
muestra = [7,  3, -4, 14, 2,
         5, 22, -7,  9, 5]
escribir(muestra)
escribir("Control")
escribir("Varianza de la muestra =", varianza(muestra, 2))
escribir("Desviación estándar de la muestra =", desviaciónEstándar(muestra, 2))
muestra = [-6,  5, 9, 4, 4,
         12, 37, 5, 3, 3]
escribir(muestra)
escribir("Tratamiento")
escribir("Varianza de la muestra =", varianza(muestra, 2))
escribir("Desviación estándar de la muestra =", desviaciónEstándar(muestra, 2))

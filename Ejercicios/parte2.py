from sys import path
path.append("../")

from Comandos.medidasVariabilidad import *

print("1.7")
muestra = [3.4, 2.5, 4.8, 2.9, 3.6,
           2.8, 3.3, 5.6, 3.7, 2.8,
           4.4, 4.0, 5.2, 3.0, 4.8]
print(muestra)
print("Varianza de la muestra =", varianza(muestra, 3))
print("Desviación estándar de la muestra =", desviaciónEstándar(muestra, 3))

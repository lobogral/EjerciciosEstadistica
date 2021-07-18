from sys import path
path.append("../")

from comandos.tiposGráficas import puntos

def dibujar(tipo, diccionarios, títuloVentana, unidadMedida):
    if tipo=="puntos":
        puntos.dibujar(diccionarios, títuloVentana, unidadMedida)
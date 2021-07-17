from matplotlib import pyplot as plt
import random

def dibujar(tipo, diccionarios, títuloVentana, unidadMedida):
    if tipo=="puntos":
        dibujarPuntos(diccionarios, títuloVentana, unidadMedida)

def dibujarPuntos(diccionarios, títuloVentana, unidadMedida):
    plt.figure(títuloVentana, figsize=(9,1))
    for diccionario in diccionarios:
        color = diccionario['color']
        muestra = diccionario['muestra']
        label = diccionario['nombre'] if len(diccionarios)>1 else ""
        plt.hlines(0,min(muestra),max(muestra), colors='k')
        plt.plot(muestra, [0]*len(muestra), 'o', color=color, label=label)
    if len(diccionarios)>1: plt.legend(bbox_to_anchor =(1.05, 1), loc='upper left')
    plt.xlabel(unidadMedida)
    plt.gca().axes.get_yaxis().set_visible(False)
    plt.tight_layout()
    plt.show()

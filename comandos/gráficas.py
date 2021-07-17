from matplotlib import pyplot as plt
import random

def dibujar(tipo, diccionarios, títuloVentana, unidadMedida):
    if tipo=="puntos":
        dibujarPuntos(diccionarios, títuloVentana, unidadMedida)

def dibujarPuntos(diccionarios, títuloVentana, unidadMedida):
    diccionarios = agregarValoresy(diccionarios)
    plt.figure(títuloVentana, figsize=(9,1.5))
    for diccionario in diccionarios:
        color = diccionario['color']
        valoresx = diccionario['valoresx']
        valoresy = diccionario['valoresy']
        label = diccionario['nombre'] if len(diccionarios)>1 else ""
        plt.hlines(0,min(valoresx),max(valoresx), colors='k')
        plt.plot(valoresx, valoresy, 'o', color=color, label=label)
    if len(diccionarios)>1: plt.legend(bbox_to_anchor =(1.05, 1), loc='upper left')
    plt.xlabel(unidadMedida)
    plt.ylim(-1,4)
    plt.gca().axes.get_yaxis().set_visible(False)
    plt.tight_layout()
    plt.show()

def agregarValoresy(diccionarios):
    valoresy = []
    valoresx = []
    inicio = 0
    for diccionario in diccionarios:
        diccionario['valoresx'] = diccionario.pop('muestra')
        valoresx += diccionario['valoresx']
        for i in range(inicio, len(valoresx)):
            valoresy += [valoresx[0:i+1].count(valoresx[i])-1]
        diccionario['valoresy'] = valoresy[inicio:len(valoresx)]
        inicio += len(valoresx)
    return diccionarios

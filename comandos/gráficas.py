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
    valsx = [val for dic in diccionarios for val in dic['muestra']]
    valsy = [valsx[0:i+1].count(valsx[i])-1 for i in range(len(valsx))]
    numElem = len(valsy)//len(diccionarios)
    listasy = [valsy[i:i+numElem] for i in range(0, len(valsy), numElem)]
    for diccionario, listay in zip(diccionarios,listasy):
        diccionario['valoresx'] = diccionario.pop('muestra')
        diccionario['valoresy'] = listay
    return diccionarios

from matplotlib import pyplot
import random

def dibujar(tipo, diccionarios, títuloVentana, unidadMedida):
    if tipo=="puntos":
        dibujarPuntos(diccionarios, títuloVentana, unidadMedida)

def dibujarPuntos(diccionarios, títuloVentana, unidadMedida):
    fig, ax = pyplot.subplots(figsize=(9,1))
    fig.canvas.manager.set_window_title(títuloVentana)
    for diccionario in diccionarios:
        color = diccionario['color']
        muestra = diccionario['muestra']
        label = diccionario['nombre'] if len(diccionarios)>1 else ""
        ax.hlines(0,min(muestra),max(muestra), colors='k')
        ax.plot(muestra, [0]*len(muestra), 'o', color=color, label=label)
    if len(diccionarios)>1:
        pyplot.legend(bbox_to_anchor =(1.05, 1), loc='upper left')
    ax.set_xlabel(unidadMedida)
    ax.get_yaxis().set_visible(False)
    pyplot.subplots_adjust(top=0.6, bottom=0.45, left=0.06, right=0.76)
    pyplot.show()

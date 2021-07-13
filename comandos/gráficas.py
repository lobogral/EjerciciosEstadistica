from matplotlib import pyplot
import random

def dibujar(tipo, muestras, títuloVentana, unidadMedida):
    if tipo=="puntos":
        dibujarPuntos(muestras, títuloVentana, unidadMedida)

def dibujarPuntos(diccionarios, títuloVentana, unidadMedida):
    fig, ax = pyplot.subplots(figsize=(9,1))
    fig.canvas.manager.set_window_title(títuloVentana)
    for diccionario in diccionarios:
        color = diccionario['color']
        muestra = diccionario['muestra']
        muestra = sorted(muestra)
        ax.hlines(0,muestra[0],muestra[len(muestra)-1], colors='k')
        if(len(diccionarios)==1):
            ax.plot(muestra, [0]*len(muestra), 'o', color=color)
        else:
            label = diccionario['nombre']
            ax.plot(muestra, [0]*len(muestra), 'o', color=color, label=label)
    if(len(diccionarios)>1):
        pyplot.legend(bbox_to_anchor =(1.05, 1), loc='upper left')
    ax.set_xlabel(unidadMedida)
    ax.get_yaxis().set_visible(False)
    pyplot.subplots_adjust(top=0.6, bottom=0.45, left=0.06, right=0.76)
    pyplot.show()

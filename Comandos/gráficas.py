from matplotlib import pyplot
import random

def dibujar(tipo, muestras, títuloVentana, unidadMedida):
    if tipo=="puntos":
        dibujarPuntos(muestras, títuloVentana, unidadMedida)

def dibujarPuntos(muestras, títuloVentana, unidadMedida):
    fig, ax = pyplot.subplots(figsize=(9,1))
    fig.canvas.manager.set_window_title(títuloVentana)
    colores = ['b','r','y']
    for muestra, color in zip(muestras, colores):
        muestra = sorted(muestra)
        ax.hlines(0,muestra[0],muestra[len(muestra)-1], colors='k')
        ax.plot(muestra, [0]*len(muestra), 'o', color=color);
    ax.set_xlabel(unidadMedida)
    ax.get_yaxis().set_visible(False)
    pyplot.subplots_adjust(bottom=0.6)
    pyplot.show()

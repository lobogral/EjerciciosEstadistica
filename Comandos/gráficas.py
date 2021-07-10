from matplotlib import pyplot

def dibujarGraficaPuntos(muestra, sección, título, unidadMedida):
    muestra = sorted(muestra)
    fig, ax = pyplot.subplots(figsize=(9,1))
    fig.canvas.manager.set_window_title(sección + ' Análisis ' + título)
    pyplot.subplots_adjust(bottom=0.6)
    ax.set_xlabel(unidadMedida)
    ax.hlines(0,muestra[0],muestra[len(muestra)-1], colors='k')
    ax.plot(muestra, [0]*len(muestra), 'o', color='b');
    ax.get_yaxis().set_visible(False)
    pyplot.show()

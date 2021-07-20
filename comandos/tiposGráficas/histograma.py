import matplotlib.pyplot as plt

def dibujar(diccionario):
    pntMed = diccionario['Punto medio']
    frecRel = diccionario['Frecuencia relativa']
    plt.bar(pntMed, frecRel, width=1, edgecolor='black')
    plt.show()
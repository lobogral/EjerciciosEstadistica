import matplotlib.pyplot as plt

def dibujar(diccionario):
    valoresx = diccionario['valoresx']
    valoresy = diccionario['valoresy']
    plt.bar(valoresx, valoresy, width=1, edgecolor='black')
    plt.show()
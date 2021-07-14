import matplotlib.pyplot as plt

valores = [1.2, 1.4, 1, 1.3, 2.5, 3.2, 1, 5, 3.5, 4.2, 0.1]
intervalos = [0, 1, 2, 3, 4, 5]

plt.title("Ejemplo calificaciones colombia")
plt.hist(valores, intervalos, edgecolor = 'black')
plt.show()

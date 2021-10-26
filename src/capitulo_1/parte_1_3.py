from estadistica.medidas_posicion import media
from estadistica.medidas_variabilidad import rango
from estadistica.medidas_variabilidad import desviacion_estandar
from estadistica.tabla_frecuencias import imprimir_tabla
from estadistica.graficas import histograma
from redondeo.redondeo import redondear

print("1.19")
print("Vida útil de 30 bombas de combustible similares (años)")
muestra = [2.0, 3.0, 0.3, 3.3, 1.3, 0.4,
           0.2, 6.0, 5.5, 6.5, 0.2, 2.3,
           1.5, 4.0, 5.9, 1.8, 4.7, 0.7,
           4.5, 0.3, 1.5, 0.5, 2.5, 5.0,
           1.0, 6.0, 5.6, 6.0, 1.2, 0.2]
diccionario = {
    "muestra": muestra,
    "paso": 0.1,
    "minimo": 0.0,
    "maximo": 7.0,
    "num_div": 7
}
print(muestra)
print("b)")
imprimir_tabla(diccionario)

print("c)")
print("Media de la muestra =",
      redondear(media(muestra), 4), "años")
print("Rango de la muestra =",
      rango(muestra), "años")
print("Desviación estándar de la muestra =",
      redondear(desviacion_estandar(muestra), 4), "años")

histograma.dibujar(diccionario,
                   "Análisis bombas de combustible",
                   "Vida útil (años)")

from estadistica.medidas_posicion import media
from estadistica.medidas_posicion import mediana
from estadistica.medidas_posicion import media_recortada
from estadistica.graficas import puntos
from redondeo.redondeo import redondear

print("1.1")
print("Mediciones tiempo de secado en pintura (horas)")
muestra = [3.4, 2.5, 4.8, 2.9, 3.6,
           2.8, 3.3, 5.6, 3.7, 2.8,
           4.4, 4.0, 5.2, 3.0, 4.8]
print(muestra)
print("a) Tamaño de la muestra =", len(muestra), "datos")
print("b) Media de la muestra =", redondear(media(muestra), 3), "horas")
print("c) Mediana de la muestra =", mediana(muestra), "horas")
print("e) x_tr(20) =", redondear(media_recortada(muestra, 0.2), 3), "horas")

puntos.dibujar(
       [{'color': 'b', 'muestra': muestra}],
       "d) Análisis pintura esmaltada",
       "Tiempo secado (horas)")


print("")
print("1.3")
print("Mediciones resistencia a la tensión en aviones (psi)")
print("Sin deterioro acelerado")
muestra_1 = [227, 222, 218, 217, 225,
             218, 216, 229, 228, 221]
print(muestra_1)
print("Con deterioro acelerado")
muestra_2 = [219, 214, 215, 211, 209,
             218, 203, 204, 201, 205]
print(muestra_2)
print("c)")
print("Media Deterioro =", redondear(media(muestra_2), 2), "psi")
print("Media No Deterioro =", redondear(media(muestra_1), 2), "psi")
print("d)")
print("Mediana Deterioro =", redondear(mediana(muestra_2), 2), "psi")
print("Mediana No Deterioro =", redondear(mediana(muestra_1), 2), "psi")

puntos.dibujar(
        [{'nombre': 'Sin deterioro', 'color': 'b', 'muestra': muestra_1},
         {'nombre': 'Con deterioro', 'color': 'r', 'muestra': muestra_2}],
        "a) Análisis aviones",
        "Resistencia tensión (psi)")


print("")
print("1.5")
print("Mediciones reducción de Colesterol en personas (mg/dL)")
print("Grupo de control")
muestra_1 = [7,  3, -4, 14, 2,
             5, 22, -7,  9, 5]
print(muestra_1)
print("Grupo de tratamiento")
muestra_2 = [-6,  5, 9, 4, 4,
             12, 37, 5, 3, 3]
print(muestra_2)
print("b)")
print("Control")
print("x_ =", redondear(media(muestra_1), 2), "mg/dL")
print("x~ =", redondear(mediana(muestra_1), 2), "mg/dL")
print("x_tr(10) =", redondear(media_recortada(muestra_1, 0.1), 2), "mg/dL")
print("Tratamiento")
print("x_ =", redondear(media(muestra_2), 2), "mg/dL")
print("x~ =", redondear(mediana(muestra_2), 2), "mg/dL")
print("x_tr(10) =", redondear(media_recortada(muestra_2, 0.1), 2), "mg/dL")

puntos.dibujar(
        [{'nombre': 'Control', 'color': 'b', 'muestra': muestra_1},
         {'nombre': 'Tratamiento', 'color': 'r', 'muestra': muestra_2}],
        "a) Análisis personas",
        "Reducción colesterol (mg/dL)")

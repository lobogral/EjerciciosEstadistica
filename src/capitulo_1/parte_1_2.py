from estadistica.medidas_variabilidad import varianza
from estadistica.medidas_variabilidad import desviacion_estandar
from redondeo.redondeo import redondear

print("1.7")
print("Mediciones tiempo de secado en pintura (horas)")
muestra = [3.4, 2.5, 4.8, 2.9, 3.6,
           2.8, 3.3, 5.6, 3.7, 2.8,
           4.4, 4.0, 5.2, 3.0, 4.8]
print(muestra)
print("Varianza de la muestra =",
      redondear(varianza(muestra), 3), "(horas)^2")
print("Desviación estándar de la muestra =",
      redondear(desviacion_estandar(muestra), 3), "horas")

print("")
print("1.9")
print("Mediciones resistencia a la tensión en aviones (psi)")
print("Sin envejecimiento acelerado")
muestra_1 = [227, 222, 218, 217, 225,
             218, 216, 229, 228, 221]
print(muestra_1)
print("Con envejecimiento acelerado")
muestra_2 = [219, 214, 215, 211, 209,
             218, 203, 204, 201, 205]
print(muestra_2)
print("Sin envejecimiento")
print("Varianza de la muestra =",
      redondear(varianza(muestra_1), 2), "(psi)^2")
print("Desviación estándar de la muestra =",
      redondear(desviacion_estandar(muestra_1), 2), "psi")
print("Con envejecimiento")
print("Varianza de la muestra =",
      redondear(varianza(muestra_2), 2), "(psi)^2")
print("Desviación estándar de la muestra =",
      redondear(desviacion_estandar(muestra_2), 2), "psi")


print("")
print("1.11")
print("Mediciones reducción de Colesterol en personas (mg/dL)")
print("Grupo de control")
muestra_1 = [7,  3, -4, 14, 2,
             5, 22, -7,  9, 5]
print(muestra_1)
print("Grupo de tratamiento")
muestra_2 = [-6,  5, 9, 4, 4,
             12, 37, 5, 3, 3]
print(muestra_2)
print("Control")
print("Varianza de la muestra =",
      redondear(varianza(muestra_1), 2), "(mg/dL)^2")
print("Desviación estándar de la muestra =",
      redondear(desviacion_estandar(muestra_1), 2), "mg/dL")
print("Tratamiento")
print("Varianza de la muestra =",
      redondear(varianza(muestra_2), 2), "(mg/dL)^2")
print("Desviación estándar de la muestra =",
      redondear(desviacion_estandar(muestra_2), 2), "mg/dL")

desde sistema importar ruta
ruta.agregar("../")

desde comandos.medidasVariabilidad importar *
desde comandos.redondeo importar *

definirRedondeoMitadArriba()

escribir("1.7")
escribir("Mediciones tiempo de secado en pintura (horas)")
muestra = [3.4, 2.5, 4.8, 2.9, 3.6,
           2.8, 3.3, 5.6, 3.7, 2.8,
           4.4, 4.0, 5.2, 3.0, 4.8]
escribir(muestra)
escribir("Varianza de la muestra =",
         redondear(varianza(muestra), 3), "(horas)^2")
escribir("Desviación estándar de la muestra =",
         redondear(desviaciónEstándar(muestra), 3), "horas")

escribir("")
escribir("1.9")
escribir("Mediciones resistencia a la tensión en aviones (psi)")
escribir("Sin envejecimiento acelerado")
muestra1 = [227, 222, 218, 217, 225,
            218, 216, 229, 228, 221]
escribir(muestra1)
escribir("Con envejecimiento acelerado")
muestra2 = [219, 214, 215, 211, 209,
            218, 203, 204, 201, 205]
escribir(muestra2)
escribir("Sin envejecimiento")
escribir("Varianza de la muestra =",
         redondear(varianza(muestra1), 2), "(psi)^2")
escribir("Desviación estándar de la muestra =",
         redondear(desviaciónEstándar(muestra1), 2), "psi")
escribir("Con envejecimiento")
escribir("Varianza de la muestra =",
         redondear(varianza(muestra2), 2), "(psi)^2")
escribir("Desviación estándar de la muestra =",
         redondear(desviaciónEstándar(muestra2), 2), "psi")


escribir("")
escribir("1.11")
escribir("Mediciones reducción de Colesterol en personas (mg/dL)")
escribir("Grupo de control")
muestra1 = [7,  3, -4, 14, 2,
         5, 22, -7,  9, 5]
escribir(muestra1)
escribir("Grupo de tratamiento")
muestra2 = [-6,  5, 9, 4, 4,
         12, 37, 5, 3, 3]
escribir(muestra2)
escribir("Control")
escribir("Varianza de la muestra =",
         redondear(varianza(muestra1), 2), "(mg/dL)^2")
escribir("Desviación estándar de la muestra =",
         redondear(desviaciónEstándar(muestra1), 2), "mg/dL")
escribir("Tratamiento")
escribir("Varianza de la muestra =",
         redondear(varianza(muestra2), 2), "(mg/dL)^2")
escribir("Desviación estándar de la muestra =",
         redondear(desviaciónEstándar(muestra2), 2), "mg/dL")

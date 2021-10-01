desde estadistica.medidas_posicion importar *
desde estadistica.medidas_variabilidad importar *
desde estadistica.tabla_frecuencias importar *
desde estadistica.graficas importar histograma
desde redondeo.redondeo importar *

escribir("1.19")
escribir("Vida útil de 30 bombas de combustible similares (años)")
muestra = [2.0, 3.0, 0.3, 3.3, 1.3, 0.4,
           0.2, 6.0, 5.5, 6.5, 0.2, 2.3,
           1.5, 4.0, 5.9, 1.8, 4.7, 0.7,
           4.5, 0.3, 1.5, 0.5, 2.5, 5.0,
           1.0, 6.0, 5.6, 6.0, 1.2, 0.2]
escribir(muestra)
escribir("b)")
imprimir_tabla(muestra, 0.1, 0.0, 7.0, 7)

escribir("c)")
escribir("Media de la muestra =", 
         redondear(media(muestra), 4), "años")
escribir("Rango de la muestra =",
         rango(muestra), "años")
escribir("Desviación estándar de la muestra =",
         redondear(desviacion_estandar(muestra), 4), "años")

histograma.dibujar( 
        establecer_datos_hist(muestra, 0.1, 0.0, 7.0, 7),
        "Análisis bombas de combustible",
        "Vida útil (años)")

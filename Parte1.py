def medidasPosicion(datos, decimales):

    n = len(datos)
    print("El tamaño de la muestra es:", n)

    media = sum(datos)/n
    media = '{:.{}f}'.format(media, decimales)
    print("La media de la muestra es:", media)

    datosOrdenados = sorted(datos)
    if len(datosOrdenados) % 2 != 0:
        mediana = datosOrdenados[(n-1)//2]
    else:
        mediana = (datosOrdenados[n//2-1]+datosOrdenados[n//2])/2
        mediana = '{:.{}f}'.format(mediana, decimales)
    print("La mediana de la muestra es:", mediana)
    
def mediaRecortada(datos, decimales, porcentaje):

    n = len(datos)
    datos = sorted(datos)
    numDatosRetirados = round(porcentaje*n)
    
    datos = datos[numDatosRetirados:(n - numDatosRetirados)]
    mediaRecortada = sum(datos)/(n - numDatosRetirados*2)
    mediaRecortada = '{:.{}f}'.format(mediaRecortada, decimales)
    print("La media recortada de la muestra es:", mediaRecortada)
    

datos = [3.4, 2.5, 4.8, 2.9, 3.6,
         2.8, 3.3, 5.6, 3.7, 2.8,
         4.4, 4.0, 5.2, 3.0, 4.8]
print(datos)
medidasPosicion(datos, 3)
mediaRecortada(datos, 3, 0.2)

print("")
datos = [227, 222, 218, 217, 225,
         218, 216, 229, 228, 221]
print(datos)
medidasPosicion(datos, 2)

print("")
datos = [219, 214, 215, 211, 209,
         218, 203, 204, 201, 205]
print(datos)
medidasPosicion(datos, 2)

print("")
datos = [7,  3, -4, 14, 2,
         5, 22, -7,  9, 5]
print(datos)
medidasPosicion(datos, 2)
mediaRecortada(datos, 3, 0.1)

print("")
datos = [-6,  5, 9, 4, 4,
         12, 37, 5, 3, 3]
print(datos)
medidasPosicion(datos, 2)
mediaRecortada(datos, 3, 0.1)

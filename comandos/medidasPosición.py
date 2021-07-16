from decimal import Decimal
import comandos.tipoRedondeo

def media(muestra, decimales):
    media = sum(muestra)/len(muestra)
    return round(Decimal(str(media)), decimales)

def mediana(muestra, decimales):
    n = len(muestra)
    muestra = sorted(muestra)
    if len(muestra) % 2 != 0:
        return muestra[(n-1)//2]
    else:
        mediana = (muestra[n//2-1]+muestra[n//2])/2
        return round(Decimal(str(mediana)), decimales)
    
def mediaRecortada(muestra, decimales, porcentaje):
    n = len(muestra)
    muestra = sorted(muestra)
    numDatosRetirados = round(porcentaje*n)
    muestra = muestra[numDatosRetirados:(n - numDatosRetirados)]
    mediaRecortada = sum(muestra)/(n - numDatosRetirados*2)
    return round(Decimal(str(mediaRecortada)), decimales)

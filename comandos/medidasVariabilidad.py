import decimal
context = decimal.getcontext()
context.rounding = decimal.ROUND_HALF_UP

from sys import path
path.append("../")

from comandos.medidasPosición import media

def varianza(muestra, decimales):
    listaMedias = [float(media(muestra,decimales))]*len(muestra)
    cuadrados = [(x - y)**2 for x, y in zip(muestra, listaMedias)]
    varianza = sum(cuadrados)/(len(cuadrados)-1)
    return round(decimal.Decimal(str(varianza)), decimales)
    
def desviaciónEstándar(muestra, decimales):
    desviaciónEstándar = float(varianza(muestra, decimales))**(0.5)
    return round(decimal.Decimal(str(desviaciónEstándar)), decimales)

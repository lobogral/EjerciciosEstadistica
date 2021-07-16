from decimal import Decimal, getcontext, ROUND_HALF_UP

def redondear(número, decimales):
    return round(Decimal(str(número)), decimales)

def definirRedondeoMitadArriba():
    context = getcontext()
    context.rounding = ROUND_HALF_UP

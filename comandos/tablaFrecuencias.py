from redondeo import *
from tiposGráficas import histograma

def obtenerTabla(datos, paso, mínimo, máximo, numDivisiones):
    tabla = {}
    intsCls, pntsMed, frecs, frecsRel = [], [], [], []    
    div = (máximo-mínimo)/numDivisiones
    for i in range(numDivisiones):
        minCls = mínimo + div*i
        maxCls = mínimo + div*(i+1) - paso
        frec = len([dato for dato in datos if minCls<=dato<=maxCls])
        intsCls += [f'{minCls}-{maxCls}']
        pntsMed += [str((minCls+maxCls)/2)]
        frecs += [frec]
        frecsRel += [redondear(frec/len(datos), 3)]
    tabla['intCls'] = intsCls
    tabla['pntMed'] = pntsMed
    tabla['frec'] = frecs
    tabla['frecRel'] = frecsRel    
    return tabla

def imprimirTabla(tabla):
    # Transpone datos
    tablaTras = []
    for vals in zip(*tabla.values()):
        tablaTras += [dict(zip(tabla.keys(), vals))]
    tabla = tablaTras
    # Imprime datos
    strIntCls = "Int. Cls.     "
    strPntMed = "Pnt. Med.    "
    strFrec = "Frec.    "
    strFrecRel = "Frec. Rel."
    print(f'{strIntCls}{strPntMed}{strFrec}{strFrecRel}')
    for diccionario in tabla:
        intCls = diccionario['intCls']
        pntMed = diccionario['pntMed']
        frec = diccionario['frec']
        frecRel = diccionario['frecRel']
        print(intCls, end="")
        espacios = len(strIntCls) - len(intCls) + len(str(pntMed))
        print('{:>{}}'.format(pntMed, espacios), end="")
        espacios = len(strPntMed) - len(str(pntMed)) + len(str(frec))
        print('{:>{}}'.format(frec, espacios), end="")
        espacios = len(strFrec) - len(str(frec)) + len(str(frecRel))
        print('{:>{}}'.format(frecRel, espacios))

def establecerDatosHist(tabla):
    tabla['valoresx'] = tabla.pop('pntMed')
    tabla['valoresy'] = tabla.pop('frecRel')
    del tabla['frec']
    del tabla['intCls']
    return tabla

datos = [2.0, 3.0, 0.3, 3.3, 1.3, 0.4,
         0.2, 6.0, 5.5, 6.5, 0.2, 2.3,
         1.5, 4.0, 5.9, 1.8, 4.7, 0.7,
         4.5, 0.3, 1.5, 0.5, 2.5, 5.0,
         1.0, 6.0, 5.6, 6.0, 1.2, 0.2]

tabla = obtenerTabla(datos, 0.1, 0.0, 7.0, 7)
imprimirTabla(tabla)
histograma.dibujar(establecerDatosHist(tabla))

datos  = [2.2, 4.1, 3.5, 4.5, 3.2, 3.7, 3.0, 2.6,
          3.4, 1.6, 3.1, 3.3, 3.8, 3.1, 4.7, 3.7,
          2.5, 4.3, 3.4, 3.6, 2.9, 3.3, 3.9, 3.1,
          3.3, 3.1, 3.7, 4.4, 3.2, 4.1, 1.9, 3.4,
          4.7, 3.8, 3.2, 2.6, 3.9, 3.0, 4.2, 3.5]

tabla = obtenerTabla(datos, 0.1, 1.5, 5.0, 7)
imprimirTabla(tabla)
histograma.dibujar(establecerDatosHist(tabla))
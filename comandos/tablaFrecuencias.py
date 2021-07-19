from redondeo import *

datos = [2.0, 3.0, 0.3, 3.3, 1.3, 0.4,
         0.2, 6.0, 5.5, 6.5, 0.2, 2.3,
         1.5, 4.0, 5.9, 1.8, 4.7, 0.7,
         4.5, 0.3, 1.5, 0.5, 2.5, 5.0,
         1.0, 6.0, 5.6, 6.0, 1.2, 0.2]

paso = 0.1
mínimo = 0.0
máximo = 7.0
numDivisiones = 7

"""
datos  = [2.2, 4.1, 3.5, 4.5, 3.2, 3.7, 3.0, 2.6,
          3.4, 1.6, 3.1, 3.3, 3.8, 3.1, 4.7, 3.7,
          2.5, 4.3, 3.4, 3.6, 2.9, 3.3, 3.9, 3.1,
          3.3, 3.1, 3.7, 4.4, 3.2, 4.1, 1.9, 3.4,
          4.7, 3.8, 3.2, 2.6, 3.9, 3.0, 4.2, 3.5]

paso = 0.1
mínimo = 1.5
máximo = 5.0
numDivisiones = 7
"""

div = (máximo-mínimo)/numDivisiones

strIntCls = "Int. Cls.     "
strPntMed = "Pnt. Med.    "
strFrec = "Frec.    "
strFrecRel = "Frec. Rel."
print(f'{strIntCls}{strPntMed}{strFrec}{strFrecRel}')
for i in range(numDivisiones):
    # Hacen los cálculos
    minCls = mínimo + div*i
    maxCls = mínimo + div*(i+1) - paso
    pntMed = redondear((minCls+maxCls)/2,2)
    frec = len([dato for dato in datos if minCls<=dato<=maxCls])
    frecRel = redondear(frec/len(datos), 3)

    # Hacen las impresiones
    intCls = f'{redondear(minCls, 1)}-{redondear(maxCls, 1)}'
    print(intCls, end="")
    espacios = len(strIntCls) - len(intCls) + len(str(pntMed))
    print('{:>{}}'.format(pntMed, espacios), end="")
    espacios = len(strPntMed) - len(str(pntMed)) + len(str(frec))
    print('{:>{}}'.format(frec, espacios), end="")
    espacios = len(strFrec) - len(str(frec)) + len(str(frecRel))
    print('{:>{}}'.format(frecRel, espacios ))
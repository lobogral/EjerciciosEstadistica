#!/usr/bin/env python
# -*- coding: latin-1 -*-

import re

cap = argv[1]
parte = argv[2]
ruta = 'capitulo-' + cap + '/parte-' + cap + '-' + parte + '.py'
programa = open(ruta, 'r', encoding='utf8')
texto = programa.readlines()
programa.close()

texto = "".join(texto)
texto = re.sub('C\(', 'binomial(', texto)
texto = re.sub('importar C,', 'importar binomial,', texto)
texto = re.sub('desde (.+) importar (.+) como (.+)', 'from \g<1> import \g<2> as \g<3>', texto)
texto = re.sub('desde (.+) importar (.+)', 'from \g<1> import \g<2>', texto)
texto = re.sub('escribir\(', 'print(', texto)
texto = re.sub('tama�o\(', 'len(', texto)
texto = re.sub('Fracci�n', 'Fraction', texto)
texto = re.sub('fracciones', 'fractions', texto)
texto = re.sub('Trozos', 'Piecewise', texto)
texto = re.sub('otroCaso', 'True', texto)
exec(texto)

#!/usr/bin/env python
# -*- coding: latin-1 -*-

import re

cap = argv[1]
parte = argv[2]
ruta = 'capitulo-' + cap + '/parte-' + cap + '-' + parte + '.py'
programa = open(ruta, 'r', encoding='utf8')
texto = programa.readlines()
programa.close()

"""
Traducciones
"""

" Funciones "
escribir = print
tamaño = len

" Variables "
otroCaso = True
Verdadero = True

" Palabras Clave"
texto = "".join(texto)
texto = re.sub('desde (.+) importar (.+) como (.+)', 'from \g<1> import \g<2> as \g<3>', texto)
texto = re.sub('desde (.+) importar (.+)', 'from \g<1> import \g<2>', texto)
texto = re.sub('\.pert\(', '.as_relational(', texto)
exec(texto)

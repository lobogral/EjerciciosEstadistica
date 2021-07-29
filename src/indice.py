#!/usr/bin/env python
# -*- coding: latin-1 -*-

import re

cap = argv[2]
parte = argv[3]
ruta = 'capitulo-' + cap + '/parte-' + cap + '-' + parte + '.py'
programa = open(ruta, 'r', encoding='utf8')
texto = programa.readlines()
programa.close()

texto = "".join(texto)
texto = re.sub('desde (.+) importar (.+)', 'from \g<1> import \g<2>', texto)
texto = re.sub('escribir\(', 'print(', texto)
texto = re.sub('tamaño\(', 'len(', texto)
exec(texto)

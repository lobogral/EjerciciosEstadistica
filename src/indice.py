import sys
import os

cap = sys.argv[1]
parte = sys.argv[2]
ruta = 'capitulo_' + cap + '/parte_' + cap + '_' + parte + '.py'
os.system("py " + ruta)

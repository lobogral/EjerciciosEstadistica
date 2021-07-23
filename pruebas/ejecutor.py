from sys import path
import re
import sys
import os

os.chdir('..')
if (not os.path.isdir('módulos')): 
    os.mkdir('módulos')
os.chdir('módulos')
if (not os.path.isdir('Redondeo')):
    os.system('git clone https://github.com/lobogral/Redondeo.git')
if (not os.path.isdir('ComandosEstadistica')):
    os.system('git clone https://github.com/lobogral/ComandosEstadistica.git')
os.chdir('../pruebas/')
path.append('../módulos/Redondeo/')
path.append('../módulos/ComandosEstadistica/')


path.append("../comandos/")
programaTxt = open(sys.argv[1], 'r', encoding='utf8')
texto = programaTxt.readlines()
programaTxt.close()

texto = "".join(texto)
texto = re.sub('desde (.+) importar (.+)', 'from \g<1> import \g<2>', texto)
texto = re.sub('escribir\(', 'print(', texto)
texto = re.sub('tamaño\(', 'len(', texto)
exec(texto)
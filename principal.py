import re
import sys

programaTxt = open(sys.argv[1], 'r', encoding='utf8')
texto = programaTxt.readlines()
programaTxt.close()

texto = "".join(texto)
texto = re.sub('desde (.+) importar (.+)', 'from \g<1> import \g<2>', texto)
texto = re.sub('from sistema', 'from sys', texto)
texto = re.sub('import ruta', 'import path', texto)
texto = re.sub('ruta.', 'path.', texto)
texto = re.sub('\.agregar', '.append', texto)
texto = re.sub('escribir\(', 'print(', texto)
texto = re.sub('tamaño\(', 'len(', texto)
exec(texto)

import sys

def tamaño(muestra):
    return len(muestra)

def escribir(*objects, sep=' ', end='\n', file=sys.stdout, flush=False):
    print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

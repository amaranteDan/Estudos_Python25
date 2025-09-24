"""
    Parametros passados por linha de comando

"""    
    
import sys

print(f"Numeros de parametros: {len(sys.argv)}")
for n, p in enumerate(sys.argv):
    print(f"Parametro {n} = {p}")    
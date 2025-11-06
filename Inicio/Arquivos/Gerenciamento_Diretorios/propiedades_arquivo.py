# Verifica a propriedade de um arquivo ou diretorio
import os   
import os.path
import time
import sys

nome = sys.argv[1] # Pega o nome do arquivo ou diretorio passado como argumento na linha de comando

print(f"Nome: {nome}")
print(f"Criado: {time.ctime(os.path.getctime(nome))}")  # Data de criacao
print(f"Tamanho: {os.path.getsize(nome)} bytes")  # Tamanho em bytes
print(f"Ultimo acesso: {time.ctime(os.path.getatime(nome))}")
print(f"Ultima modificacao: {time.ctime(os.path.getmtime(nome))}")
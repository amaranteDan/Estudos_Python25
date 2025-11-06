'''
Esta é uma aplicação simples para criar uma estrutura de diretórios e arquivos usando Python.

'''
import os

import time

# Imprime na tela o diretório atual de trabalho
print("Diretorio Atual",os.getcwd())

# Caminho dentro do home do usuário
caminho = os.path.expanduser("~/W/Z/V")

# Cria os diretorios recursivamente
os.makedirs(caminho, exist_ok=True)
time.sleep(100)
print(f"Diretorios {caminho} criados com sucesso!")

if os.path.exists(caminho):
    print(f"O diretório {caminho} existe.")
    
    os.rmdir(caminho)  # Remove o diretório (deve estar vazio)
    print(f"O diretório {caminho} foi removido.")
else:
    print(f"O diretório {caminho} não existe.")
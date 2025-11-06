'''
Programa para verificar se tem confirmação para apagar diretorios
'''

import os
import shutil

caminho = os.path.expanduser("~/W")

# Verifica se diretorio existe
if os.path.exists(caminho):
    confirmacao = input(f"Tem certeza que deseja apagar o diretório {caminho} e todo o seu conteúdo? (s/n): ")
    
    if confirmacao.lower() == 's':
        shutil.rmtree(caminho)  # Remove o diretório e todo o seu conteúdo
        print(f"O diretório {caminho} e todo o seu conteúdo foram removidos.")
    else:
        print("Operação cancelada pelo usuário.")
else:
    print(f"O diretório {caminho} não existe.")
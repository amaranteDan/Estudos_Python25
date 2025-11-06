'''
Este é um exemplo de programa que remove tudo recursivamente, com arquivos e subpastas

'''

import os
import shutil

caminho = os.path.expanduser("~/W")

if os.path.exists(caminho):
    shutil.rmtree(caminho)  # Remove o diretório e todo o seu conteúdo
    print(f"O diretório {caminho} e todo o seu conteúdo foram removidos.")
else:
    print(f"O diretório {caminho} não existe.")
    
    
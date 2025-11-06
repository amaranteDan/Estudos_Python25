'''
O progrma para remover um diretorio e todo o seu conteudo com passagem de arqgumentos:
O diretório a remover passado como argumento.

Usar a flag --force para apagar sem pedir confirmação.

Se não usar --force, o script pergunta antes.

'''

import os
import shutil
import argparse 

def remover_diretorios(caminho, force=False):
    if os.path.exists(caminho):
        if force:
            shutil.rmtree(caminho)
            print(f"O diretório {caminho} e todo o seu conteúdo foram removidos sem confirmação.")
        else:
            confirmacao = input(f"Tem certeza que deseja apagar o diretório {caminho} e todo o seu conteúdo? (s/n): ")
            if confirmacao.lower() == 's':
                shutil.rmtree(caminho)
                print(f"O diretório {caminho} e todo o seu conteúdo foram removidos.")
            else:
                print("Operação cancelada pelo usuário.")
    else:
        print(f"O diretório {caminho} não existe.")
        
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Remover diretório e todo o seu conteúdo com opção de confirmação.")
    parser.add_argument("caminho", help="Caminho do diretório a ser removido.")
    parser.add_argument("--force", action="store_true", help="Apagar sem pedir confirmação.")
    
    args = parser.parse_args()
    
    caminho = os.path.expanduser(args.caminho)
    
    remover_diretorios(args.caminho, args.force)       
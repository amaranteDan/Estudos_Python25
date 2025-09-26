'''
Contar linhas, palavras e caracteres em um arquivo de texto
Enunciado: Crie um programa que leia um arquivo de texto e conte o número de linhas, palavras e caracteres presentes no arquivo. O programa deve exibir essas informações na tela.
Cenário de uso: Útil para análise rápida de arquivos de texto, como logs ou documentos.

Como usar:
- python Exe_9.6.py txt
'''

import sys

def contar_conteudo(arquivo):
    try:
        with open(arquivo, 'r', encoding='utf-8') as arq:
            linhas = arq.readlines()
            num_linhas = len(linhas)
            num_palavras = sum(len(linha.split()) for linha in linhas)
            num_caracteres = sum(len(linha) for linha in linhas)

        print(f"Arquivo: {arquivo}")
        print(f"Número de linhas: {num_linhas}")
        print(f"Número de palavras: {num_palavras}")
        print(f"Número de caracteres: {num_caracteres}")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao processar o arquivo '{arquivo}': {e}")
        
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python Exe_9.6.py <nome_do_arquivo>")
        sys.exit(1)

    nome_arquivo = sys.argv[1]
    contar_conteudo(nome_arquivo)        
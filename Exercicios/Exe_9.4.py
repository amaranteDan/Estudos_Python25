'''
Crie um programa que receba o nome de dois arquivos como parametro da linha de comando e gere
um terceiro arquivo contendo a saida com as linhas do primeiro arquivo seguidas das linhas do segundo arquivo.
O nome do arquivo de saida pode ser passado como parametro na linha de comandos.
'''
import sys
import os

if len(sys.argv) != 4:
    print("Uso: python Exe_9.4.py <arquivo1> <arquivo2> <arquivo_saida>")
    sys.exit(1)
if not (os.path.exists(sys.argv[1]) and os.path.exists(sys.argv[2])):
    print("Erro: Um ou ambos os arquivos de entrada não existem.")
    sys.exit(1)
    
arquivo1 = sys.argv[1]
arquivo2 = sys.argv[2]
arquivo_saida = sys.argv[3]
try:
    with open(arquivo1, 'r', encoding='utf-8') as arq1, open(arquivo2, 'r', encoding='utf-8') as arq2, open(arquivo_saida, 'w', encoding='utf-8') as arq_saida:
        # Escreve as linhas do primeiro arquivo no arquivo de saída
        for linha in arq1:
            arq_saida.write(linha)
        # Escreve as linhas do segundo arquivo no arquivo de saída
        for linha in arq2:
            arq_saida.write(linha)
    print(f"Arquivo '{arquivo_saida}' criado com sucesso.")
except FileNotFoundError as e:
    print(f"Erro: {e}. Verifique se os arquivos existem.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")    

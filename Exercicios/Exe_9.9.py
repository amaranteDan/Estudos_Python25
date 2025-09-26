'''
Gerar Relatório de Tamanho de Arquivos
Enunciado: Crie um programa que receba uma lista de nomes de arquivos como argumentos da linha de comando e gere um relatório em um arquivo de saída (também passado como argumento) com o nome de cada arquivo e seu tamanho em bytes.
Cenário de uso: Útil para auditoria de arquivos em um diretório, como verificar o tamanho de backups ou logs.

Como usar:
- python3 Exe_9.9.py arquivo1 arquivo2 arquivo_saida resultado.txt

Erro na saída:
cat resultado.txt 
Relatório de Tamanho de Arquivos
==============================
Arquivo: arquivo1, Erro: Não encontrado
Arquivo: arquivo2, Erro: Não encontrado
Arquivo: arquivo_saida, Erro: Não encontrado

Resultado esperado:
cat relatorio.txt 
Relatório de Tamanho de Arquivos
==============================
Arquivo: arquivo1.txt, Tamanho: 12 bytes
Arquivo: arquivo2.txt, Tamanho: 37 bytes
Arquivo: arquivo_saida.txt, Tamanho: 147 bytes
'''

import sys
import os

def gerar_relatorio_tamanho():
    if len(sys.argv) < 3:
        print("Uso: python relatorio_tamanho.py <arquivo1> [arquivo2 ...] <arquivo_saida>")
        sys.exit(1)

    arquivos_entrada = sys.argv[1:-1]
    arquivo_saida = sys.argv[-1]

    try:
        with open(arquivo_saida, 'w', encoding='utf-8') as arq_saida:
            arq_saida.write("Relatório de Tamanho de Arquivos\n")
            arq_saida.write("=" * 30 + "\n")
            for arquivo in arquivos_entrada:
                try:
                    tamanho = os.path.getsize(arquivo)
                    arq_saida.write(f"Arquivo: {arquivo}, Tamanho: {tamanho} bytes\n")
                except FileNotFoundError:
                    arq_saida.write(f"Arquivo: {arquivo}, Erro: Não encontrado\n")
                except Exception as e:
                    arq_saida.write(f"Arquivo: {arquivo}, Erro: {e}\n")
        print(f"Relatório gerado em '{arquivo_saida}'.")
    except Exception as e:
        print(f"Erro ao criar arquivo de saída: {e}")

if __name__ == "__main__":
    gerar_relatorio_tamanho()
'''
Filtrar Linhas por Palavra-Chave
Enunciado: Crie um programa que receba como argumentos o nome de um arquivo de texto e uma palavra-chave, e gere um novo arquivo contendo apenas as linhas que contêm a palavra-chave. O nome do arquivo de saída deve ser um argumento adicional.
Cenário de uso: Útil para extrair linhas específicas de logs ou arquivos de dados com base em um termo, como filtrar erros em logs de servidores.
Como usar:
- python log.txt "ERROR" log_erros.txt  
'''
import sys

def filtrar_linhas():
    if len(sys.argv) != 4:
        print("Uso: python filtrar.py <arquivo_entrada> <palavra_chave> <arquivo_saida>")
        sys.exit(1)

    arquivo_entrada = sys.argv[1]
    palavra_chave = sys.argv[2]
    arquivo_saida = sys.argv[3]

    try:
        with open(arquivo_entrada, 'r', encoding='utf-8') as arq_entrada, \
             open(arquivo_saida, 'w', encoding='utf-8') as arq_saida:
            for linha in arq_entrada:
                if palavra_chave.lower() in linha.lower():
                    arq_saida.write(linha)
        print(f"Arquivo '{arquivo_saida}' criado com as linhas contendo '{palavra_chave}'.")
    except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo_entrada}' não encontrado.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    filtrar_linhas()
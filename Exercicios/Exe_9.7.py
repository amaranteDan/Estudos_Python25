'''
Substituir Texto em um Arquivo
Enunciado: Crie um programa que receba como argumentos da linha de comando: o nome de um arquivo de texto, uma palavra a ser substituída e a nova palavra. O programa deve criar um novo arquivo com o texto modificado, mantendo o original intacto.
Cenário de uso: Útil para automação de edição de arquivos de configuração, substituição de termos em documentos ou pré-processamento de dados.

Como usar:
- python Exe_9.7.py config.txt "localhost" "192.168.1.1" config_modificado.txt

'''

import sys

def substituir_texto():
    if len(sys.argv) != 5:
        print("Uso: python substituir.py <arquivo_entrada> <palavra_antiga> <palavra_nova> <arquivo_saida>")
        sys.exit(1)

    arquivo_entrada = sys.argv[1]
    palavra_antiga = sys.argv[2]
    palavra_nova = sys.argv[3]
    arquivo_saida = sys.argv[4]

    try:
        with open(arquivo_entrada, 'r', encoding='utf-8') as arq_entrada:
            conteudo = arq_entrada.read()
        
        # Realiza a substituição
        conteudo_modificado = conteudo.replace(palavra_antiga, palavra_nova)

        with open(arquivo_saida, 'w', encoding='utf-8') as arq_saida:
            arq_saida.write(conteudo_modificado)
        
        print(f"Arquivo '{arquivo_saida}' criado com as substituições.")
    except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo_entrada}' não encontrado.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    substituir_texto()
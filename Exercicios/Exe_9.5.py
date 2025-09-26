import sys

def concatenar_arquivos():
    if len(sys.argv) < 3:
        print("Uso: python Exe_9.5.py <arquivo1> <arquivo2> ... <arquivo_saida>")
        sys.exit(1)

    arquivos_entrada = sys.argv[1:-1]
    arquivo_saida = sys.argv[-1]
    arquivos_processados = 0

    try:
        with open(arquivo_saida, 'w', encoding='utf-8') as arq_saida:
            for arquivo in arquivos_entrada:
                try:
                    with open(arquivo, 'r', encoding='utf-8') as arq_entrada:
                        for linha in arq_entrada:
                            arq_saida.write(linha)
                        #rq_saida.write("\n")
                        arquivos_processados += 1
                except FileNotFoundError:
                    print(f"Erro: O arquivo '{arquivo}' não foi encontrado. Pulando este arquivo.")
                except Exception as e:
                    print(f"Ocorreu um erro ao ler o arquivo '{arquivo}': {e}. Pulando este arquivo.")
        if arquivos_processados == 0:
            print(f"Aviso: Nenhum arquivo de entrada foi processado. O arquivo '{arquivo_saida}' pode estar vazio.")
        else:
            print(f"Arquivo '{arquivo_saida}' criado com sucesso. {arquivos_processados} arquivo(s) processado(s).")
    except Exception as e:
        print(f"Ocorreu um erro ao criar o arquivo de saída '{arquivo_saida}': {e}")

if __name__ == "__main__":
    concatenar_arquivos() # Chama a função principal
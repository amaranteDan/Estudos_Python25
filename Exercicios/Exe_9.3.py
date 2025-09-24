'''
Enunciado: Criar um programa que leia os arquivos pares.txt e impares.txt, os junte e crie um novo chamado pares_impares.txt em ordem.
'''
try:
    
    numeros = []

    # ler os arquivos pares.txt
    with open("pares.txt") as pares:
        for linha in pares:
            # Converte a linha para inteiro, removendo espaços ou quebras de linha
            numeros.append(int(linha.strip()))
        
    # Ler os arquivos impares.txt
    with open("impares.txt") as impares:
        for linha in impares:
            # Converte a linha para inteiro, removendo espaços ou quebras de linha
            numeros.append(int(linha.strip()))
        
    # Ordenar as linhas
    numeros_ordenados = sorted(numeros)    

    # Escrever no arquivo pares_impares.txt
    with open("pares_impares.txt", "w") as pares_impares:
        for numeros in numeros_ordenados:
            pares_impares.write(f"{numeros}\n")   
except FileNotFoundError as e:
    print(f"Erro: {e}. Verifique se os arquivos pares.txt e impares.txt existem.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")                
        
"""
Geração de arquivos - Programa 9.3 - Verifica se um número é par ou ímpar e grava em arquivos diferentes
"""
with open ("impares.txt", "w") as impares:
    with open ("pares.txt", "w") as pares:
        for i in range(1, 1001):
            if i % 2 == 0:
                pares.write(f"{i}\n")
            else:
                impares.write(f"{i}\n")
                
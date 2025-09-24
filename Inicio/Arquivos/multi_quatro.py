"""
Programa Leitura e escrita usando multiplos de 4.
"""

with open ("multi_quatro.txt", "w") as multiplos4:
    with open ("pares.txt") as pares:
        for linha in pares.readlines():
            if int(linha) % 4 == 0:
                multiplos4.write(linha)
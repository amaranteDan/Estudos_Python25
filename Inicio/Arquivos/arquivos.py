"""
 O objetivo deste módulo é fornecer funções para manipulação de arquivos.
 Modo
    r - leitura
    w - escrita
    a - anexar mas preserva o que ja foi escrito
    b - binário
    + - atualização (leitura e escrita)   
"""

arquivo = open("telefones.csv", "r")
for linha in arquivo.readlines():
    print(linha.strip())
arquivo.close()


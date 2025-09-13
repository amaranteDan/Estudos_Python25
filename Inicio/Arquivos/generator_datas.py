import csv
import random

# Estados com DDD e regiões simplificados
dados_estados = [
    ("SP", "Sudeste", [11, 12, 13, 14, 15, 16, 17, 18, 19]),
    ("RJ", "Sudeste", [21, 22, 24]),
    ("MG", "Sudeste", [31, 32, 33, 34, 35, 37, 38]),
    ("ES", "Sudeste", [27, 28]),
    ("PR", "Sul", [41, 42, 43, 44, 45, 46]),
    ("SC", "Sul", [47, 48, 49]),
    ("RS", "Sul", [51, 53, 54, 55]),
    ("DF", "Centro-Oeste", [61]),
    ("GO", "Centro-Oeste", [62, 64]),
    ("MT", "Centro-Oeste", [65, 66]),
    ("MS", "Centro-Oeste", [67]),
    ("BA", "Nordeste", [71, 73, 74, 75, 77]),
    ("PE", "Nordeste", [81, 87]),
    ("CE", "Nordeste", [85, 88]),
    ("RN", "Nordeste", [84]),
    ("PB", "Nordeste", [83]),
    ("AL", "Nordeste", [82]),
    ("SE", "Nordeste", [79]),
    ("MA", "Nordeste", [98, 99]),
    ("PI", "Nordeste", [86, 89]),
    ("PA", "Norte", [91, 93, 94]),
    ("AM", "Norte", [92, 97]),
    ("AC", "Norte", [68]),
    ("RO", "Norte", [69]),
    ("RR", "Norte", [95]),
    ("AP", "Norte", [96]),
    ("TO", "Norte", [63]),
]

# Criar arquivo CSV
with open("telefones.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile, delimiter=";")
    writer.writerow(["numero", "regiao", "codigo_area", "estado"])

    for _ in range(100):
        estado, regiao, codigos = random.choice(dados_estados)
        ddd = random.choice(codigos)
        numero = f"{ddd}9{random.randint(10000000, 99999999)}"
        writer.writerow([numero, regiao, ddd, estado])

print("Arquivo telefones.csv gerado com sucesso!")

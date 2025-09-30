'''
Exercicio com listas - Percorrendo a lista diretamente com o for
'''

notas = [7, 7, 7, 4, 9]

soma = 0

for nota in notas:
    soma += nota
media = soma / len(notas)    
print(f"Média: { media:5.2f}")    
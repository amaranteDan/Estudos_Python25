'''
Media de notas de um aluno usando o for com indice para percorrer a lista
'''

notas = [7, 7, 7, 4, 9]

soma = 0

for n in range(len(notas)):
    soma += notas[n]
    
media = soma / len(notas)    
print(f"Média: { media:5.2f}")
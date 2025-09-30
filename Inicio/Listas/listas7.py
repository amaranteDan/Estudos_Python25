'''
Gostaria de ver outra forma pythonica de resolver o exercicio de media?
Agora vamos usar Usando `statistics.mean`. Quer ver como fica?

'''

import statistics

notas = [7, 7, 7, 4, 9]

media = statistics.mean(notas)


print(f"Média: { media:5.2f}")
'''
Usando list comprehension (com `sum`)
Ainda podemos melhorar mais o código, com list comprehension. Sabe o que é e como usar?
Vamos ver como fica?

👉 Todas dão o mesmo resultado, mas cada estilo serve para situações diferentes:

* **while** → quando você precisa de mais controle do índice.
* **for** → quando só quer percorrer os elementos.
* **sum/mean** → mais limpo e direto.
* **list comprehension** → quando quer transformar ou filtrar elementos antes de somar.

👉 Quer saber quais são as funções built-in do Python? Dá uma olhada [aqui](https://docs.python.org/3/library/functions.html).
Mas como nos gostamos da linha de codigo, vamos importar o modulo builtin?  😁

import builtins

# Lista tudo que está no namespace built-in
print(dir(builtins))

ou você pode percorrer como aprendemos com o for.

for nome in dir(builtins):
    if callable(getattr(builtins, nome)):
        print(nome)
'''

notas = [7, 7, 7, 4, 9]

media = sum([nota for nota in notas]) / len(notas)
print(f"Média: { media:5.2f}")
## Ruff Tutorial

`https://docs.astral.sh/ruff/tutorial/`

## Textual 

`https://textual.textualize.io/tutorial/`

## uv Tutorial

`https://docs.astral.sh/uv/getting-started/`

## FastApi

`https://fastapi.tiangolo.com/`

## Books online

`https://automatetheboringstuff.com/`

## Polars Dataframe

`https://docs.pola.rs/user-guide/getting-started/`

## Brython - Script language for the web

`https://brython.info/`

## Removendo arquivos do rastreamento do git

`git rm --cached arquivos.txt`
`git rm --cached testes.txt`

## Depois comitar
`git commit -m "Remove arquivos.txt e testes.txt do rastreamento"`

## Exercicios com lista:

Esse seu exercício calcula a média de uma lista de notas. Ele está certinho, mas podemos escrever de várias formas diferentes em Python, algumas mais simples e outras mais "pitônicas".

Vou te mostrar algumas variações:

---

### 🔹 1. Usando `for` com índice

```python
notas = [6, 7, 8, 5, 9]

soma = 0
for i in range(len(notas)):
    soma += notas[i]

media = soma / len(notas)
print(f"Média: {media:5.2f}")
```

---

### 🔹 2. Usando `for` direto sobre a lista

```python
notas = [6, 7, 8, 5, 9]

soma = 0
for nota in notas:
    soma += nota

media = soma / len(notas)
print(f"Média: {media:5.2f}")
```

---

### 🔹 3. Usando a função `sum()`

```python
notas = [6, 7, 8, 5, 9]

media = sum(notas) / len(notas)
print(f"Média: {media:5.2f}")
```

---

### 🔹 4. Usando `statistics.mean`

```python
import statistics

notas = [6, 7, 8, 5, 9]

media = statistics.mean(notas)
print(f"Média: {media:5.2f}")
```

---

### 🔹 5. Usando list comprehension (com `sum`)

```python
notas = [6, 7, 8, 5, 9]

media = sum([nota for nota in notas]) / len(notas)
print(f"Média: {media:5.2f}")
```

---

👉 Todas dão o mesmo resultado, mas cada estilo serve para situações diferentes:

* **while** → quando você precisa de mais controle do índice.
* **for** → quando só quer percorrer os elementos.
* **sum/mean** → mais limpo e direto.

Quer que eu mostre também uma versão **orientada a objetos** (com uma classe `Aluno` que guarda notas e calcula a média)?

Perfeito 🚀! Vamos transformar esse exercício em um exemplo **orientado a objetos**. Assim você já treina conceitos de **POO** em Python.

---

## 🔹 Exemplo 1 — Classe simples `Aluno`

```python
class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas
    
    def calcular_media(self):
        return sum(self.notas) / len(self.notas)
    

# Exemplo de uso
aluno1 = Aluno("Daniel", [6, 7, 8, 5, 9])
print(f"Média do {aluno1.nome}: {aluno1.calcular_media():5.2f}")
```

---

## 🔹 Exemplo 2 — Com validação de notas

```python
class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        # Garante que todas as notas estão entre 0 e 10
        self.notas = [n for n in notas if 0 <= n <= 10]
    
    def calcular_media(self):
        return sum(self.notas) / len(self.notas) if self.notas else 0
    
    def aprovado(self):
        return self.calcular_media() >= 7


# Exemplo de uso
aluno1 = Aluno("Maria", [6, 7, 8, 5, 9])
print(f"Média da {aluno1.nome}: {aluno1.calcular_media():5.2f}")
print("Situação:", "Aprovado" if aluno1.aprovado() else "Reprovado")
```

---

## 🔹 Exemplo 3 — Classe com múltiplos alunos

```python
class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas
    
    def calcular_media(self):
        return sum(self.notas) / len(self.notas)
    
    def __str__(self):
        return f"{self.nome} - Média: {self.calcular_media():.2f}"


class Turma:
    def __init__(self):
        self.alunos = []
    
    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
    
    def medias_turma(self):
        for aluno in self.alunos:
            print(aluno)


# Exemplo de uso
turma = Turma()
turma.adicionar_aluno(Aluno("Ana", [10, 8, 9]))
turma.adicionar_aluno(Aluno("Carlos", [6, 5, 7, 8]))
turma.adicionar_aluno(Aluno("Beatriz", [9, 9, 10]))

turma.medias_turma()
```

Saída:

```
Ana - Média: 9.00
Carlos - Média: 6.50
Beatriz - Média: 9.33
```

---

Não existe um emoji oficial só para **debug**, mas dá pra usar alguns que combinam bem com o contexto de “depuração”, “analisar”, “caçar bug” 🐛🔍.

Aqui estão alguns que a galera costuma usar:

* 🐛 → bug (clássico pra marcar erro/bug)
* 🔍 → lupa (investigando algo)
* 🐞 → joaninha (bug de software também)
* 🛠️ → ferramentas (arrumando algo)
* 📊 → logs, análise
* 📝 → anotações de debug
* 🧪 → testes
* 🚧 → em desenvolvimento

Exemplo de log com emoji:

```text
🐛 DEBUG: variável x = 42
🔍 TRACE: entrou na função processar_dados()
```

👉 Quer que eu te monte um **padrão de logs com emojis** (tipo INFO, DEBUG, ERROR, WARNING cada um com seu emoji)?


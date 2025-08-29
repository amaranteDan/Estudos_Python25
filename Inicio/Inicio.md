````markdown
# 📚 Sumário

- [📌 Regras para Nomear Variáveis em Python](#-regras-para-nomear-variáveis-em-python)
- [📌 Strings em Python](#-strings-em-python)
- [📌 Números em Python](#-números-em-python)
  - [📝 Tabela de Números](#-tabela-de-números)
  - [🔄 Conversões](#-conversões)
  - [⚡ Exemplo prático](#-exemplo-prático)
- [🧘 Zen do Python](#-zen-do-python)

---

# 📌 Regras para Nomear Variáveis em Python

✅ **Podem começar** com letra ou underscore (`_`), mas **não** com número.  
Exemplo: `greeting_message`  

✅ **Use sempre letras minúsculas** para nomes de variáveis.  

❌ **Não utilize palavras reservadas** da linguagem.  

---

## 🔎 Como ver as palavras reservadas em Python
```python
import keyword
print(keyword.kwlist)
````

---

# 📌 Strings em Python

Strings são uma série de caracteres.
Exemplos: `"This is a string"` ou `"Python is my favorite language"`

```python
name = "python"

print(f'{name.title()}')  # Maiúscula no começo
print(name.upper())       # Tudo em maiúscula
print(name.lower())       # Tudo em minúscula
```

📌 O **ponto (`.`)** após a variável indica que você está acessando um **método**.
Exemplo: `name.title()` → o método `title()` atua na variável `name`.

> Todo método é seguido de parênteses, pois pode receber informações adicionais.

---

# 📌 Números em Python

## 📝 Tabela de Números

| Tipo                     | Descrição                                     | Exemplo de valor                    | Exemplo de uso em Python |
| ------------------------ | --------------------------------------------- | ----------------------------------- | ------------------------ |
| **`int`**                | Número inteiro (positivo, negativo, zero)     | `10`, `-7`, `0`                     | `a = 10`                 |
| **`float`**              | Número decimal (ponto flutuante)              | `3.14`, `-0.5`, `2.0`               | `x = 3.14`               |
| **`complex`**            | Número complexo (real + imaginário)           | `2+3j`, `-1j`                       | `c = 2+3j`               |
| **Notação científica**   | Forma compacta de grandes ou pequenos números | `1.5e3` (=1500.0), `2e-4` (=0.0002) | `n = 1.5e3`              |
| **Divisão inteira `//`** | Resultado inteiro da divisão                  | `9 // 2 = 4`                        | `resultado = 9 // 2`     |
| **Módulo `%`**           | Resto da divisão                              | `9 % 2 = 1`                         | `resto = 9 % 2`          |
| **Potência `**`**        | Exponenciação                                 | `2 ** 3 = 8`                        | `pot = 2 ** 3`           |

---

## 🔄 Conversões

```python
int(3.99)     # 3
float(7)      # 7.0
complex(5)    # (5+0j)
```

---

## ⚡ Exemplo prático

```python
# Inteiros
a = 10
b = -7

# Float
pi = 3.14159

# Complexo
c = 2 + 3j

# Operações
print("Soma:", a + pi)          # 13.14159
print("Divisão inteira:", 9 // 2)  # 4
print("Potência:", 2 ** 5)      # 32
print("Complexo real:", c.real) # 2.0
print("Complexo imag:", c.imag) # 3.0
```

---

# 🧘 Zen do Python

A filosofia da comunidade Python está contida no **“Zen de Python”** de Tim Peters.

```python
import this
print(this)
```

```

---

Em **Python**, as palavras reservadas (keywords) são aquelas que **já têm significado especial na linguagem** e **não podem ser usadas como nomes de variáveis, funções ou classes**.

Para **ver a lista completa das palavras reservadas** no seu Python, você pode usar o módulo `keyword`:

```python
import keyword

# Lista de todas as palavras reservadas
print(keyword.kwlist)

# Quantas palavras reservadas existem
print(len(keyword.kwlist))
```

🔎 Exemplo de saída (pode variar de acordo com a versão do Python):

```python
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
 'try', 'while', 'with', 'yield']
```

---

😃
Em **Python**, as palavras reservadas (keywords) são aquelas que **já têm significado especial na linguagem** e **não podem ser usadas como nomes de variáveis, funções ou classes**.

Para **ver a lista completa das palavras reservadas** no seu Python, você pode usar o módulo `keyword`:

```python
import keyword

# Lista de todas as palavras reservadas
print(keyword.kwlist)

# Quantas palavras reservadas existem
print(len(keyword.kwlist))
```

🔎 Exemplo de saída (pode variar de acordo com a versão do Python):

```python
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
 'try', 'while', 'with', 'yield']
```

---


🚀 Vamos explicar direitinho o que fazem as funções **`str()`**, **`int()`** e **`float()`** no Python, com exemplos práticos.

---

# 📌 1. `str()`

👉 Converte um valor em **string** (texto).

### Exemplos:

```python
# Número para string
x = 10
print(str(x))        # "10"
print(type(str(x)))  # <class 'str'>

# Booleano para string
flag = True
print(str(flag))     # "True"

# Lista para string
lista = [1, 2, 3]
print(str(lista))    # "[1, 2, 3]"
```

---

# 📌 2. `int()`

👉 Converte um valor para **inteiro** (número sem casas decimais).
⚠️ Se tentar converter algo inválido (ex.: `"abc"`), gera erro.

### Exemplos:

```python
# Float para inteiro (corta a parte decimal)
print(int(3.99))   # 3

# String numérica para inteiro
print(int("42"))   # 42

# Booleano para inteiro
print(int(True))   # 1
print(int(False))  # 0
```

---

# 📌 3. `float()`

👉 Converte um valor para **número de ponto flutuante** (com casas decimais).

### Exemplos:

```python
# Inteiro para float
print(float(7))     # 7.0

# String numérica para float
print(float("3.14"))  # 3.14

# Booleano para float
print(float(True))   # 1.0
print(float(False))  # 0.0
```

---

# 📌 Comparação prática entre as três

```python
n = 5

print(str(n))   # "5"   (texto)
print(int("10"))   # 10   (inteiro)
print(float("3.5")) # 3.5 (decimal)
```

---

Perfeito 😃 vamos montar uma **tabelinha comparativa** lado a lado mostrando como `str()`, `int()` e `float()` se comportam com os mesmos valores.

---

# 📌 Comparação entre `str()`, `int()` e `float()`

| Valor de entrada  | `str()` (texto) | `int()` (inteiro)     | `float()` (decimal) |
| ----------------- | --------------- | --------------------- | ------------------- |
| `10`              | `"10"`          | `10`                  | `10.0`              |
| `3.99`            | `"3.99"`        | `3`                   | `3.99`              |
| `"42"` (string)   | `"42"`          | `42`                  | `42.0`              |
| `"3.14"` (string) | `"3.14"`        | ❌ Erro (`ValueError`) | `3.14`              |
| `True`            | `"True"`        | `1`                   | `1.0`               |
| `False`           | `"False"`       | `0`                   | `0.0`               |

---

## ⚡ Exemplos em código

```python
# Exemplo com número inteiro
n = 10
print(str(n))   # "10"
print(int(n))   # 10
print(float(n)) # 10.0

# Exemplo com float
f = 3.99
print(str(f))   # "3.99"
print(int(f))   # 3
print(float(f)) # 3.99

# Exemplo com string
s = "42"
print(str(s))   # "42"
print(int(s))   # 42
print(float(s)) # 42.0

# Exemplo com booleano
print(str(True))   # "True"
print(int(True))   # 1
print(float(True)) # 1.0
```

---






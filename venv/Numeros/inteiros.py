
# Exemplos de números inteiros em Python
a = 10       # inteiro positivo
b = -7       # inteiro negativo
c = 0        # zero
print(type(a))  # <class 'int'>

# Exemplos de números de ponto flutuante em Python
x = 3.14
y = -0.5
z = 2.0
print(type(x))  # <class 'float'>

# Exemplos de números complexos em Python
c1 = 2 + 3j
c2 = -1j
print(c1.real)  # Parte real -> 2.0
print(c1.imag)  # Parte imaginária -> 3.0


# Notação científica

n1 = 1.5e3   # 1500.0
n2 = 2e-4    # 0.0002
print(n1, n2)

# Operações básicas com números

soma = 5 + 3       # 8
sub = 10 - 4       # 6
mult = 7 * 6       # 42
div = 8 / 2        # 4.0
div_int = 9 // 2   # 4 (divisão inteira)
mod = 9 % 2        # 1 (resto da divisão)
pot = 2 ** 3       # 8 (potência)
print(soma, sub, mult, div, div_int, mod, pot)

# Converter entre tipos

a = int(3.99)     # 3
b = float(7)      # 7.0
c = complex(5)    # (5+0j)
print(a, b, c)
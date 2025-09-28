notas = [6,7,8,5,9]

soma = 0
x = 0

while x < 5:
    soma = soma + notas[x]
    x += 1
print(f"Media: {soma / x:5.2f}")
    
    
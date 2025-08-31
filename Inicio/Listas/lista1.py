"""A Ideia destes exercícios é praticar o uso de listas em Python."""

# Exercício 1: Crie uma lista com os números de 1 a 10 e imprima cada número multiplicado por 2.
numeros = list(range(1, 11))
for numero in numeros:
    print(f'{numero * 2}')

    
bikes = ['trek', 'cannondale', 'redline', 'specialized']
for i in range(1):
    #print(bikes[i].title())
    for bike in bikes[:3]:
     #   print(bike.title())   
        for char in bikes[0]:
      #      print(char.upper()) 
            
            for i, char in enumerate(bikes[0]):
                print(f"Posição {i} : {char.upper()}")
    
    
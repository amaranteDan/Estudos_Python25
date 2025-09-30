'''
Bom, chegou o momento de aprendermos a usar listas com POO. 
Imagine que você precisa criar um sistema para gerenciar as notas dos alunos de uma escola. Nesse sistema, vamos armazenar a nota do aluno Daniel apenas e vamos evoluindo.

'''
'''
Criando a minha classe Aluno

'''


class Aluno:
    '''
    Classe para representar um aluno com suas notas
    '''
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas =  notas # Inicializa uma lista vazia para armazenar as notas

    
    def calcular_media(self):
        '''Calcula a média das notas do aluno'''
        if len(self.notas) == 0:
            return 0  # Evita divisão por zero
        return sum(self.notas) / len(self.notas)  # Calcula a média das notas
    
    
# Agora vou instanciar a classe Aluno e adicionar notas    
aluno1 = Aluno("Daniel", [7, 7, 7, 4, 9])

'''E vamos ver o resultado, claro como sempre fazemos com a ajuda do nosso amigo 🐞'''
 
print(f"Aluno: {aluno1.nome}, sua Média é: {aluno1.calcular_media():5.2f}")
'''
Mais um exemplo de listas com POO, agora com validação das notas

'''

class Aluno:
    '''
    Classe para representar um aluno e validar as notas
    '''
    
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = [n for n in notas if 0 <= n <= 10]  # Valida as notas entre 0 e 10
        
    def calcular_media(self):
        return sum(self.notas) / len(self.notas) if self.notas else 0  # Evita divisão por zero 
    
    def aprovado(self):
        return self.calcular_media() >= 7  # Considera aprovado se a média for 6 ou mais  
    
    
aluno1 = Aluno("Daniel", [7, 7, 7, 4, 9])  # Inclui notas inválidas para teste
print(f"\n Aluno: {aluno1.nome}, Média: {aluno1.calcular_media():5.2f}, Aprovado: {'Sim' if aluno1.aprovado() else 'Não'}")


aluno2 = Aluno("Ana", [6, 5, 8, 7, 10])  # Inclui notas inválidas para teste
#print("Situação:", "Aprovado" if aluno2.aprovado() else "Reprovado")   
print(f"\n Aluno: {aluno2.nome}, Média: {aluno2.calcular_media():5.2f}, Aprovado: {'Sim' if aluno2.aprovado() else 'Não'}")
  

aluno3 = Aluno("Rosangela", [7, 8, 7, 9, 8, 9])  # Inclui notas inválidas para teste
#print("Situação:", "Aprovado" if aluno3.aprovado() else "Reprovado") 
print(f"\n Aluno: {aluno3.nome}, Média: {aluno3.calcular_media():5.2f}, Aprovado: {'Sim' if aluno3.aprovado() else 'Não'}")

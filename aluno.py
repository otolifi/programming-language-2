class Aluno:
    def __init__(self):
        self.nome = None
        self.tempo_sem_dormir = 0
    
    def estudar(self,horas):
        self.tempo_sem_dormir += horas
    
    def dormir(self,horas):
        self.tempo_sem_dormir -= horas


aluno1 = Aluno()
aluno1.nome = "Luizinho" 
aluno1.estudar(3)
aluno1.dormir(2)
aluno1.estudar(4)
aluno1.dormir(2)
print('O aluno', aluno1.nome, 'está a', aluno1.tempo_sem_dormir, 'horas sem dormir')

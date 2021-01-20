class Funcionario():
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def aumentar_salario(self,aumento):
        self.salario += aumento

f = Funcionario('ze',2000)
f.aumentar_salario(50)
print(f.salario)
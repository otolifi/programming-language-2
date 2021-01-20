class Pessoa:
    def __init__(self, nome, fone, email):
        self.nome = nome
        self.fone = fone
        self.email = email
        self.emprego = None
        self.dependentes = None
    
    def calcular_salario(self):
        self.emprego.salario += self.emprego.bonus * self.dependentes

class Emprego:
    def __init__(self, cargo, area, salario, bonus):
        self.cargo = cargo
        self.area = area
        self.salario = salario
        self.bonus = bonus


gerente = Emprego('gerente','engenharia',20000,1000)
severino = Pessoa('severino','909090090','sev@erin.com')
severino.emprego = gerente
severino.dependentes = 3
severino.calcular_salario()
print(severino.emprego.salario)
    
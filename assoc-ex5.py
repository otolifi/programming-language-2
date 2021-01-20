class Paciente:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

class Medico:
    def __init__(self, nome, crm, especializacao):
        self.nome = nome
        self.crm = crm
        self.especializacao = especializacao

class Exame:
    def __init__(self, medico, paciente, descricao, resultado):
        self.medico = medico
        self.paciente = paciente
        self.descricao = descricao
        self.resultado = resultado

    def imprimir_exame(self):
        print("Paciente: ", self.paciente.nome)
        print("Medico: ", self.medico.nome)
        print("CRM: ", self.medico.crm)
        print("Descrição: ", self.descricao)
        print("Resultado: ", self.resultado)


paciente = Paciente('Marcelo Silva', '033444555-22', 26)
medico = Medico('Ana Beatriz', 333431, 'Clínico Geral')
exame01 = Exame(medico, paciente, 'COVID-19', 'Negativo')  
exame01.imprimir_exame()						
# Deve exibir relatório com todos os dados do exame (inclusive os dados do médico e paciente)

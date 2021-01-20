'''Crie uma hierarquia de classes para representar os diferentes tipos de
funcionários de um escritório que tem os seguintes cargos: gerente, assistente
e vendedor.
Escreva uma classe base abstrata chamada Funcionario que declara um método
abstrato calcular_salario()
Essa classe também deve definir os seguintes atributos: nome, matricula
e salario_base.
Essa classe abstrata deverá ser herdada pelas outras classes que são:
Gerente, Assistente e Vendedor.
Em cada classe filha deve-se sobrescrever o método calcular_salario().
Este método deve calcular e retornar o salário de cada funcionário,
da seguinte forma:
O gerente recebe duas vezes o salário_base.
O assistente recebe o salário_base.
O vendedor recebe o salário_base mais uma comissão de 10%.
Implemente um programa principal que cria um objeto de cada tipo
(gerente, assistente e vendedor) e os armazena em uma lista
Percorra essa lista e imprima o salário de cada funcionário.'''

from abc import ABC, abstractmethod


class Funcionario(ABC):
    nome = ""
    matricula = ""
    salario = 2000
    salario_base = 2000

    @abstractmethod
    def calcular_salario(self):
        pass

class Gerente(Funcionario):
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
    
    def calcular_salario(self):
        self.salario = 2 * self.salario_base
        return self.salario

class Assistente(Funcionario):
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
    
    def calcular_salario(self):
        self.salario = self.salario_base
        return self.salario

class Vendedor(Funcionario):
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
    
    def calcular_salario(self):
        self.salario = 1.1 * self.salario_base
        return self.salario

gerente = Gerente("Gerente", "6660999")
assistente = Assistente("Assistente", "9099900")
vendedor = Vendedor("Vendedor", "190909909")

funcas = [gerente, assistente, vendedor]


for func in funcas:
    print(f"Nome: {func.nome} - Salário: {func.calcular_salario()}")

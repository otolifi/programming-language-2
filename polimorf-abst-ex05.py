'''Um banco trabalha com três tipos de contas:
conta corrente comum
conta corrente com limite
conta poupança
Em todos os casos é necessário guardar o número da conta,
o nome do correntista e o saldo.
Para a conta poupança é necessário guardar o dia do aniversário da conta
(quando são creditados os juros).
Já para a conta com limite é necessário guardar o valor do limite.
As operações possíveis são: depósito, saque e impressão de saldo.
Essas operações devem ser definidas numa classe abstrata denominada Conta.
A operação de depósito e saldo são iguais para os três tipos de conta.
A operação de saque só é diferente na conta com limite,
pois esta admite que o saldo fique negativo até o limite estabelecido.
Nas demais contas o saque não pode ser realizado
se não houver saldo suficiente.
Implemente a hierarquia de classes definida acima.
'''

from abc import ABC, abstractmethod


class Conta(ABC):
    numero = 0
    correntista = None
    saldo = 0
    limite = 0




class ContaCorrenteComum(Conta):
    def __init__(self, numero, correntista):
        self.numero = numero
        self.correntista = correntista

    def deposito(self, valor):
        super().deposito(valor)

    def saque(self, valor):
        super().saque(valor)

    def imprime_saldo(self):
        super().imprime_saldo()


class ContaPoupanca(Conta):
    def __init__(self, numero, correntista, aniversario):
        self.numero = numero
        self.correntista = correntista
        self.aniversario = aniversario

    def deposito(self, valor):
        super().deposito(valor)

    def saque(self, valor):
        super().saque(valor)

    def imprime_saldo(self):
        super().imprime_saldo()


class ContaCorrenteLimite(Conta):
    def __init__(self, numero, correntista, limite):
        self.numero = numero
        self.correntista = correntista
        self.limite = limite

    def deposito(self, valor):
        super().deposito(valor)

    def saque(self, valor):
        super().saque(valor)

    def imprime_saldo(self):
        super().imprime_saldo()

conta4 = Conta()

print(conta4)



'''
Implemente a classe Copo com dois atributos PRIVADOS:
    capacidade
    quantidade
Implemente um construtor que inicialize os atributos.
Implemente um conjunto de métodos get para cada atributo
    get_capacidade
    get_quantidade
Implemente os métodos:
    encher: aumenta 100 unidades na quantidade do copo.
    esvaziar: diminui 100 unidades na quantidade do copo.
Atenção: A quantidade no copo nunca pode ser maior que sua capacidade
ou menor que zero.
'''


# { IMPLEMENTE SEU CÓDIGO AQUI

class Copo:
    def __init__(self, capacidade, quantidadae):
        self.__capacidade = capacidade
        self.__quantidade = quantidadae

    def get_capacidade(self):
        return self.__capacidade

    def get_quantidade(self):
        return self.__quantidade

    def encher(self):
        if self.__quantidade + 100 <= self.__capacidade:
            self.__quantidade += 100

    def esvaziar(self):
        if self.__quantidade - 100 >= 0:
            self.__quantidade -= 100

# }


copo = Copo(400, 200)

copo.encher()
print("Quantidade:", copo.get_quantidade())    # Quantidade: 300
copo.encher()
print("Quantidade:", copo.get_quantidade())    # Quantidade: 400
copo.encher()
print("Quantidade:", copo.get_quantidade())    # Quantidade: 400

copo.esvaziar()
print("Quantidade:", copo.get_quantidade())    # Quantidade: 300
copo.esvaziar()
print("Quantidade:", copo.get_quantidade())    # Quantidade: 200
copo.esvaziar()
print("Quantidade:", copo.get_quantidade())    # Quantidade: 100
copo.esvaziar()
print("Quantidade:", copo.get_quantidade())    # Quantidade: 0
copo.esvaziar()
print("Quantidade:", copo.get_quantidade())    # Quantidade: 0
copo.esvaziar()

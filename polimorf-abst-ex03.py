from abc import ABC, abstractmethod


class Veiculo(ABC):

    @abstractmethod
    def limpar(self):
        pass

    @abstractmethod
    def consertar(self):
        pass


class Bicicleta(Veiculo):
    def __init__(self):
        pass

    def limpar(self):
        print("Bicicleta foi limpo")

    def consertar(self):
        print("Bicicleta foi consertada")


class Automovel(Veiculo):
    def __init__(self):
        pass

    def limpar(self):
        print("Automóvel foi limpo")

    def consertar(self):
        print("Automóvel foi consertado")

    def trocar_oleo(self):
        print("O óleo foi trocado")







bike = Bicicleta()
carro = Automovel()

bike.limpar()
bike.consertar()

carro.limpar()
carro.consertar()
carro.trocar_oleo()

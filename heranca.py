class Veiculo:
    def __init__(self, marca, modelo, rodas):
        self.marca = marca
        self.modelo = modelo
        self.rodas = rodas
        self.__velocidade = 0

    def acelerar(self, valor):
        self.__velocidade += valor

    def frear(self, valor):
        self.__velocidade -= valor

    def get_velocidade(self):
        return self.__velocidade


class Carro(Veiculo):
    def __init__(self, marca, modelo, rodas, potencia):
        super().__init__(marca, modelo, rodas)
        self.potencia = potencia

    def imprimir_informacoes(self):
        print("Carro:")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Rodas: {self.rodas}")
        print(f"Potencia: {self.potencia}")


class Moto(Veiculo):
    def __init__(self, marca, modelo, rodas, partida_eletrica):
        super().__init__(marca, modelo, rodas)
        self.partida_eletrica = partida_eletrica

    def imprimir_informacoes(self):
        print("Moto:")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Rodas: {self.rodas}")
        print(f"Partida Elétrica: {self.partida_eletrica}")


class Bicicleta(Veiculo):
    def __init__(self, marca, modelo, rodas, marchas, bagageiro):
        super().__init__(marca, modelo, rodas)
        self.marchas = marchas
        self.bagageiro = bagageiro

    def imprimir_informacoes(self):
        print("Bicicleta:")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Rodas: {self.rodas}")
        print(f"Marchas: {self.marchas}")
        print(f"Bagageiro: {self.bagageiro}")

carro = Carro("Ford", "Ka", 4, 85.0)
moto = Moto("Honda", "Biz", 2, True)
bike = Bicicleta("Caloi", "Elite", 2, 18, True)

carro.acelerar(30)
carro.frear(10)
moto.acelerar(100)
moto.frear(20)
bike.acelerar(20)
bike.frear(5)

carro.imprimir_informacoes()   # imprime os valores de todos os atributos do carro
bike.imprimir_informacoes()    # imprime os valores de todos os atributos da bicicleta
moto.imprimir_informacoes()    # imprime os valores de todos os atributos da moto

# testar a velocidade atual
print("Velocidade atual do Carro:", carro.get_velocidade())       # 20
print("Velocidade atual da Moto:", moto.get_velocidade())         # 80
print("Velocidade atual da Bicicleta:", bike.get_velocidade())    # 15

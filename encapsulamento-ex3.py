class CarroCorrida:
    def __init__(self, numero, piloto, vel_max):
        self.__nnumero = numero
        self.__piloto = piloto
        self.__vel_max = vel_max
        self.__vel_atual = 0
        self.__ligado = False
    
    def ligar(self):
        self.__ligado = True

    def desligar(self):
        self.__ligado = False

    def acelerar(self, acel):
        if (self.__ligado == True and self.__vel_atual < self.__vel_max):
            if (self.__vel_atual + acel < self.__vel_max):
                self.__vel_atual += acel
            else:
                self.__vel_atual = self.__vel_max     
    
    def frear(self):
        self.__vel_atual = 0

    def get_velocidade_atual(self):
        return self.__vel_atual


carro = CarroCorrida(1, "Paulo", 150)
carro.acelerar(20)
print(carro.get_velocidade_atual())         # imprime 0, porque o carro está desligado
carro.ligar()
carro.acelerar(20)                          
print(carro.get_velocidade_atual())         # imprime 20
carro.acelerar(80)
print(carro.get_velocidade_atual())         # imprime 100
carro.acelerar(70)
print(carro.get_velocidade_atual())         # imprime 150, não ultrapassar a vel. max.
carro.frear()
print(carro.get_velocidade_atual())         # imprime 0

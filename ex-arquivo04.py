import pickle

class Conta:
    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo


conta1 = Conta(100, "Jose", 1000.00)
conta2 = Conta(101, "Maria", 2000.01)
conta3 = Conta(102, "Kiko", 150.55)

lista = [conta1, conta2, conta3]

print(lista)


arq = open("contas.bin", "wb")
pickle.dump(lista, arq)
arq.close()


arq = open("contas.bin", "rb")
lista = pickle.load(arq)

for el in lista:
    print(f"Conta: {el.numero}, Titular: {el.titular}, Saldo: {el.saldo}")


arq.close()
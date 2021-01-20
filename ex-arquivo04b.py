import pickle

arq = open("contas.bin", "rb")
lista = pickle.load(arq)

for el in lista:
    print(el.titular)


arq.close()
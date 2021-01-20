def pega_numeros(arquivo, lista):
    arq = open(arquivo, 'r')
    for linha in arq:
        lista.append(int(linha))
    arq.close()


lista = []

pega_numeros('pares.txt', lista)
pega_numeros('impares.txt', lista)

lista.sort()

arq = open('todos.txt','w')
for el in lista:
    arq.write(str(el) + '\n')
arq.close()

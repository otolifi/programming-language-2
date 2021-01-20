class Produto:
    def __init__(self, descricao, valor):
        self.descricao = descricao
        self.valor = valor


class Carrinho:
    def __init__(self, cliente):
        self.cliente = cliente
        self.produtos = []

    def adicionar_produto(self, item):
        self.produtos.append(item)

    def listar_produto(self):
        for produto in self.produtos:
            print(produto.descricao, ' - ', produto.valor)

    def calcular_total(self):
        i = 0
        for produto in self.produtos:
            i += 1
        return i

class Cliente:
    def __init__(self, nome):
        self.nome = nome


cliente1 = Cliente('Fulano')
prod1 = Produto('Banana', 5)
prod2 = Produto('Café', 12)
prod3 = Produto('Coca-Cola', 3)

carrinho1 = Carrinho(cliente1)
carrinho1.adicionar_produto(prod1)
carrinho1.adicionar_produto(prod2)
carrinho1.adicionar_produto(prod3)
carrinho1.listar_produto()
print("Total: ", carrinho1.calcular_total())
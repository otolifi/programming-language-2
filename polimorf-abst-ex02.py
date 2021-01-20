class Produto:
    def __init__(self, nome, preco, descricao):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao
    
    def exibir_descricao(self):
        print(self.descricao)
        

class Mouse(Produto):
    def __init__(self, nome, preco, descricao, tipo):
        super().__init__(nome, preco, descricao)
        self.tipo = tipo
    
    def exibir_descricao(self):
        print(self.descricao)
        print(self.tipo)


class Livro(Produto):
    def __init__(self, nome, preco, descricao, autor):
        super().__init__(nome, preco, descricao)
        self.autor = autor
    
    def exibir_descricao(self):
        print(self.descricao)
        print(self.autor)


mouse1 = Mouse("Logitreco",99.99,'Bluetooth','Sem Fio')
mouse2 = Mouse("Multitazer",19.99,'Receptor','Sem Fio')
mouse3 = Mouse("Microploft",199.99,'Silencioso','USB')
livro1 = Livro("Dom Casmurro",4.99,"Sobre Bentinho e Capitu","Machadovski")
livro2 = Livro("Os Lusíadas",9.99,"Sonetos 2 quartetos e 2 sextetos","Camões")

carrinho = [mouse1, mouse2, mouse3, livro1, livro2]

for item in carrinho:
    item.exibir_descricao()
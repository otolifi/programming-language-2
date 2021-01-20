class Livro:
    def __init__(self, titulo, autor, preco):
        self.titulo = titulo
        self.autor = autor
        self.preco = preco
    
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.preco = None
    
    def exibir_dados(self):
        print("Dados do livro: ")
        print("Titulo: ", self.titulo)
        print("Autor: ", self.autor)
        print("Preco: ", self.preco)


livro1 = Livro("Biblia", "JEsus", 10)
livro1.exibir_dados()
livro1.preco = 21
livro1.exibir_dados()
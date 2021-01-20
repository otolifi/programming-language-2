class Pessoa:
    def __init__(self, nome):
        self.nome = nome


class Livro:
    def __init__(self, titulo, paginas, autor):
        self.titulo = titulo
        self.paginas = paginas
        self.autor = autor

    def exibir_dados(self):
        print("Titulo: ", self.titulo)
        print("Paginas: ", self.paginas)
        print("Autor: ", self.autor.nome)


pessoa1 = Pessoa('JK Rowland')
livro1 = Livro('Harry Porta', 123, pessoa1)
livro1.exibir_dados()
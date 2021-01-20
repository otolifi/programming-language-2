class Filme:
    def __init__(self):
        self.__titulo = ""
        self.__genero = ""
    
    def get_titulo(self):
        return self.__titulo
    
    def get_genero(self):
        return self.__genero
    
    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_genero(self, genero):
        self.__genero = genero


lista_filmes = []

filme1 = Filme()
filme1.set_titulo("Mad Max")
filme1.set_genero("Ação")
lista_filmes.append(filme1)

filme2 = Filme()
filme2.set_titulo("Alladin")
filme2.set_genero("Desenho")
lista_filmes.append(filme2)

filme3 = Filme()
filme3.set_titulo("A Hora do Espanto")
filme3.set_genero("Terror")
lista_filmes.append(filme3)


print("Relatório de Filmes:")
for filme in lista_filmes:
    print("Título: {}, Gênero: {}".format(filme.get_titulo(), filme.get_genero()))

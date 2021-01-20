class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def emitir_som(self):
        print('...')


class Cachorro(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def emitir_som(self):
        print('Auau')


class Gato(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def emitir_som(self):
        print('Miau')


class Cavalo(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def emitir_som(self):
        print('Hayou')


class Veterinario:
    def __init__(self):
        pass
    
    def examinar(self, animal):
        animal.emitir_som()




dog = Cachorro("Rex", 3)
horse = Cavalo("Horse", 6)
cat = Gato("Tina", 1)

print(dog.nome)
print(horse.nome)
print(cat.nome)

dog.emitir_som()          # exibe o som do cachorro
horse.emitir_som()        # exibe o som do cavalo
cat.emitir_som()          # exibe o som do gato

vet = Veterinario()
vet.examinar(dog)         # exibe o som do cachorro 
vet.examinar(horse)       # exibe o som do cavalo 
vet.examinar(cat)         # exibe o som do gato

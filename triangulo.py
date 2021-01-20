class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def calcular_perimetro(self):
        return self.a+self.b+self.c
    
    def maior_lado(self):
        return max([self.a,self.b,self.c])

t = Triangulo(1,2,3)
print(t.calcular_perimetro())
print(t.maior_lado())
class Televisao:
    def __init__(self):
        self.canal = 0
        self.volume = 0
    
    def alterar_canal(self, canal):
        self.canal = canal
    
    def aumentar_volume(self):
        self.volume += 1
    
    def diminuir_volume(self):
        self.volume -= 1

tv = Televisao()
tv.alterar_canal(5)
tv.aumentar_volume()
tv.aumentar_volume()
tv.aumentar_volume()
tv.diminuir_volume()
print('A tv está no canal:', tv.canal)			# imprime 5
print('A tv está no volume:', tv.volume)			# imprime 2

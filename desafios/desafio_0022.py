'''
Crie a classe ControleRemoto, onde simularemos o funcionamento de um controle remoto simples(canal, volume, liga/desliga).
'''
from rich import print
from rich.panel import Panel
from rich.align import Align

texto = Align.center(f'[red]A tv está desligada[/red]')
print(Panel(texto, title=f'[ TV ]', title_align='center', width=40))

print(Panel(f'CANAL = 1 2 3 4 5\nVOLUME = ▮▮▮▯', title=f'[ TV ]', title_align='center', width=40))




tela_volume = '▮▯▯▯'

while True:
    volume = input('Volume: ') 
    if volume == '+':
        tela_volume[0] = '▮'
        tela_volume[:-1]
    elif volume == '0':
        break   
print(tela_volume)



'''
class ControleRemoto:

    def __init__(self,ligar):
        self.ligar = ligar
    
    def tela(self):
        if self.ligar == '@':
            print
'''
'''
Crie a classe ControleRemoto, onde simularemos o funcionamento de um controle remoto simples(canal, volume, liga/desliga).
'''
from rich import print
from rich.panel import Panel
from rich.align import Align

texto = Align.center(f'[red]A tv está desligada[/red]')
print(Panel(texto, title=f'[ TV ]', title_align='center', width=40))

print(Panel(f'CANAL = 1 2 3 4 5\nVOLUME = ▮▮▮▯', title=f'[ TV ]', title_align='center', width=40))

canais = [1,2,3,4,5]

for i in range(len(canais)):
    print(i+1,end=' ')

def select_canal(canal=int):
    if canal in canais:
        for i in range(len(canais)):
            if canal == i:
                print(f'[yellow on white]{i}[/yellow on white]',end=' ')

select_canal(3)



botao = ''
while True:
    botao = input('Canal: ')
    if botao == '>':
        for i in canais:
            if i == 1:
                print(f'[yellow on white]{i}[/yellow on white]',end=' ')
    print(canais)









#----------------------------------------------------------------------------------------------------------------
#VOLUME
'''
volume_nivel = 1
MAX_VOLUME = 5


tela_volume = '▮' * volume_nivel + '▯' * (MAX_VOLUME - volume_nivel)
print(f'Volume: {tela_volume}')

while True:
    volume = input('Volume: ')
    if volume_nivel < MAX_VOLUME:
        if volume == '+':
            tela_volume = '▮' + tela_volume
            tela_volume = tela_volume[:-1]
        elif volume == '-':
            tela_volume = tela_volume + '▯'
            tela_volume = tela_volume[1:]
        elif volume == '0':
            break   
    print(tela_volume)

#----------------------------------------------------------------------------------------------------------------


class ControleRemoto:

    def __init__(self,ligar):
        self.ligar = ligar
    
    def tela(self):
        if self.ligar == '@':
            print
'''
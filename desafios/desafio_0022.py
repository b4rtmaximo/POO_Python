'''
Crie a classe ControleRemoto, onde simularemos o funcionamento de um controle remoto simples(canal, volume, liga/desliga).
'''
from rich import print
from rich.panel import Panel
from rich.align import Align


class ControleRemoto:

    def __init__(self):
        self.ligar = ' '
    
    def tela(self,botao):
        self.ligar = botao
        if self.ligar == '#':
    
            tela_off = Align.center(f'[red]A tv está desligada[/red]') 
            
            print(Panel(tela_off, title=f'[ TV ]', title_align='center', width=40))
        
        elif self.ligar == '@':
             
             print(Panel(f'[green]CANAL[/green] = 1 2 3 4 5\n[green]VOLUME[/green] = ▮▮▮▯', title=f'[ TV ]', title_align='center', width=40)) 

    
    def select_canal(self, canal=int):
        canais = [1,2,3,4,5]
        if canal in canais:
            for i in canais:
                if i == canal:
                    print(f' [yellow on white]{i}[/yellow on white] ',end='')
                else:
                    print(f' {i} ', end='')
            print()
            
    def select_volume(self):
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
        



c1 = ControleRemoto()

tela_off = Align.center(f'[red]A tv está desligada[/red]') 
print(Panel(tela_off, title=f'[ TV ]', title_align='center', width=40))
while True:
    botao = input()
    if botao == '#':
        c1.tela(botao)
    elif botao == '@':
        c1.tela(botao)
        c1.select_volume()
        c1.select_canal()
    else:
        break





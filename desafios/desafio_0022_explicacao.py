from rich import print
from rich.panel import Panel
from rich.align import Align

class Controle_Remoto:
    #atributos de classe
    canal_min: int = 1
    canal_max: int = 5
    vol_min: int = 1
    vol_max: int = 6

    def __init__(self, canal = 1, volume = 2):
        self.canal_atual: int = canal
        self.vol_atual: int = volume
        self.ligado: bool = False

    def on_off(self):
        self.ligado = not self.ligado



    def canal_mais(self):
        if self.ligado:
            if self.canal_atual == Controle_Remoto.canal_max:
                self.canal_atual = Controle_Remoto.canal_min
            else:
                self.canal_atual += 1

    def canal_menos(self):
        if self.ligado:
            if self.canal_atual == Controle_Remoto.canal_min:
                self.canal_atual = Controle_Remoto.canal_max
            else:
                self.canal_atual -= 1

    def vol_mais(self):
        if self.ligado:
            if self.vol_atual != Controle_Remoto.vol_max:
                self.vol_atual += 1

    def vol_menos(self):
        if self.ligado:
            if self.vol_atual != Controle_Remoto.vol_min:
                self.vol_atual -= 1



    def mostrarTV(self):

        conteudo = ''

        if not self.ligado:
            conteudo = f'[red]          TV OFF[/]'
        else:
            conteudo = f'[blue]Canal = [/]'

            for canal in range(Controle_Remoto.canal_min, Controle_Remoto.canal_max + 1):
                if canal == self.canal_atual:
                    conteudo += f' [black on yellow] {canal} [/] '
                else:
                    conteudo += f' {canal} '

            conteudo += f' \nVolume = '
            for volume in range(Controle_Remoto.vol_min, Controle_Remoto.vol_max + 1):
                if volume <= self.vol_atual:
                    conteudo += '[black on cyan] [/]'    
                else:
                    conteudo += '[black on white] [/]'

        tv = Panel(conteudo, title = 'TV', width=30)
        print(tv)

c = Controle_Remoto()

while True:
    c.mostrarTV()
    comando = str(input(f' < CH >  - VOL + '))
    match comando:
        case '0':
            break
        case '@':
            c.on_off()
        case '>':
            c.canal_mais()
        case '<':
            c.canal_menos()
        case '-':
            c.vol_menos()
        case '+':
            c.vol_mais()
    print('\n' * 10)
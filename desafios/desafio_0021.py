'''
Crie uma classe chamada Caneta, que simule o funcionamento de uma escrita colorida, podendo escrever frases na cor relativa.
'''

from rich import print

class Caneta:

    def __init__(self,cor):
        self.cor = cor

    def destampar(self,destampar=True):
        self.destampar = destampar


    def quebrar_linha(self, numero):
        self.numero = numero
        for i in range(self.numero):
            print()

    def escrever(self,texto):
        if self.destampar == True:
            if self.cor == 'verde':
                print(f'[green]{texto}[/green]')
            elif self.cor == 'vermelho':
                print(f'[red]{texto}[/red]')
            elif self.cor == 'azul':
                print(f'[blue]{texto}[/blue]')
            else:
                print(f'Sorry! Não temos a cor {self.cor}..')
        else:
            print(f'🚫 A caneta está tampada!')

        
c1 = Caneta('vermelho')
c2 = Caneta('azul')
c1.destampar()
c1.escrever('Olá')
c1.quebrar_linha(4)
c2.escrever('Olá')
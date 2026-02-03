'''
Crie uma classe Gamer, onde podemos cadastrar nome, nick e jogos favoritos de uma pessoa. Crie também um método que permita mostrar a ficha desse gamer.
'''
from rich import print
from rich.panel import Panel

class Gamer:

    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.lista = []
    
    def listar(self, title):
        self.title = title
        self.lista.append(title)
        self.lista.sort()
    

    def fav_games(self):
        print(Panel(f'{self.lista}', title='Ficha do Jogador', style='yellow',width=40))
        for i in self.lista:
            print(f'🕹️, {i}')

G1 = Gamer('Caroline Máximo', 'CarolXP')
G1.listar('Super Mario')
G1.listar('Resident Evil')
G1.listar('Castlevania')
G1.fav_games()
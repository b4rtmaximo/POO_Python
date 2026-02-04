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
        return self.lista
    
    def exibir(self):
        games_format = []
        for i in self.lista:
            games_format.append(f'🕹️, {i}')

        return '\n'.join(games_format) 

    def fav_games(self):
        print(Panel(f'{self.exibir()}', title= f'{self.nome} / {self.nick}', style='bold white',width=38))



G1 = Gamer('Roberto Marinho', 'BobXP')
G1.listar('Super Mario')
G1.listar('Resident Evil')
G1.listar('Castlevania')
G1.fav_games()
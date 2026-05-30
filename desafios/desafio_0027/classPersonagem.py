from abc import ABC, abstractmethod
import random
from rich import print

class Personagem(ABC):

    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = []

    def atacar(self, alvo, forca = 10):
        if self.vida > 0 and alvo.vida > 0:
            golpe = self.golpes[random.randrange(0, len(self.golpes))]
            print(f'{self.nome}({self.vida}) [red]atacou[/] {alvo.nome}({alvo.vida}) com o um {golpe} de força {forca}.')
            alvo.receber_dano(forca)
        else:
            print(f'{self.nome} não pode atacar {alvo.nome}.')

    def receber_dano(self, dano):
        fator = random.randint(0, dano)
        self.vida -= fator
        if self.vida <= 0:
            self.vida = 0
            print(f'[blue]{self.nome}[\] não resistiu ao ataque e desmaiou!')
        else:
            print(f'[blue]{self.nome}[/] recebeu [red]{fator} pts[/] de dano!')
    
    @abstractmethod
    def curar(self):
        pass

#_____________________________________________________________

class Guerreiro(Personagem):

    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        
        self.golpes = ["Ataque com espada", "Soco forte", "Chute 300"]
    
    def curar(self):
        fator = random.randint(0, 20)
        self.vida += fator
        print(f'[blue]{self.nome}[/] usou uma atadura e recuperou [green]{fator} pts[/] de vida.')


class Mago(Personagem):

    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Bola de Fogo', 'Raio', 'Dardos Mágicos']

    def curar(self):
        fator = random.randint(0, 20)
        self.vida += fator
        print(f'[blue]{self.nome}[/] usou uma magia de cura e recuperou [green]{fator} pts[/] de vida.')



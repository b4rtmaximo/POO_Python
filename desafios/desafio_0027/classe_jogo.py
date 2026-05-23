from abc import ABC, abstractmethod
import random

class Personagem(ABC):

    def __init__(self, nome, vida, golpes):
        self.nome = nome
        self.vida = vida
        self.golpes = golpes

    def atacar(alvo, força):
        pass

    def receber_dano(dano):
        pass
        
    @abstractmethod
    def curar():
        pass


class Guerreiro(Personagem):

    def __init__(self, nome, vida, golpes):
        super().__init__(nome, vida, golpes)
        vida = 2000
        golpes = ["Espada de Fogo", "Soco de Hércules", "Empurrão"]

    def curar():
        pass

class Mago(Personagem):

    def __init__(self, nome, vida, golpes):
        super().__init__(nome, vida, golpes)
        self.golpes = golpes
        golpes = ["Bola de Fogo", "Mísseis Mágicos", "Orbe Cromática"]
    
    def atacar(alvo, força):
        random.choice(golpes)


    def curar():
        pass

p1 = Guerreiro("Kratos")
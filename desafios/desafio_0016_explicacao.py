from rich import print
from rich import inspect

class Funcionario:

    # atributos de classe
    empresa = 'Curso em Vídeo'

    def __init__(self, nome, setor, cargo):
        # atributos de instância
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self) -> str:
        return f':handshake: Olá, sou {self.nome} e sou {self.cargo} do setor {self.setor} da empresa {Funcionario.empresa}.'
        # ou {self.__class__.empresa}


#Funcionario.empresa = 'Hostnet'

c1 = Funcionario('Maria', 'Administração', 'Diretora')
print(c1.__dict__)
print(c1.apresentacao())
#inspect(c1, methods=True)

c2 = Funcionario('Pedro', 'TI', 'Programador')
print(c2.apresentacao())
        
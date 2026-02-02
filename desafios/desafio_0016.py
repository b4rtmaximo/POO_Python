'''
Crie uma classe Funcionario, onde podemos cadastrar nome, setor e cargo. Crie também um método que permita ao funcionário se apresentar.
'''

class Funcionario:

    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentar(self):
        return f'Olá! Me chamo {self.nome} e sou {self.cargo} do setor de {self.setor}.'
    
f1 = Funcionario('Mario', 'RH', 'Psicólogo')
print(f1.apresentar())
class Pessoa: #Superclasse
    def __init__(self, nome = "", idade = 0):
        self.nome = nome
        self.idade = idade
    
    def fazer_niver(self):
        self.idade += 1
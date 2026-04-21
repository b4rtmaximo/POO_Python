from abc import ABC, abstractmethod

class Pessoa(ABC): #Superclasse, Mãe, Raiz, Classe Abstrata
    def __init__(self, nome = "", idade = 0):
        self.nome = nome
        self.idade = idade
    
    def fazer_niver(self):
        self.idade += 1

    @abstractmethod #obriga as classes filhas a terem esse método, mas elas podem modificar para cada situação
    def estudar(self):
        pass

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f'{self.nome} - Status: Matriculado')

    def estudar(self):
        print(f'{self.nome} está estudando {self.curso} na turma {self.turma}')
    


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f'{self.nome} iniciou uma aula.')

    def estudar(self):
        print(f'{self.nome} é especialista em {self.especialidade} no {self.nivel}')


class Funcionario(Pessoa):
    def __init__(self,nome,idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor
    
    def bater_ponto(self):
        print(f'{self.nome} bateu o ponto!')

    def estudar(self):
        print(f'{self.nome} se especializa para a área de {self.setor}')
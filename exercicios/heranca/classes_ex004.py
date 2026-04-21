

class Pessoa: #Superclasse
    def __init__(self, nome = "", idade = 0):
        self.nome = nome
        self.idade = idade
    
    def fazer_niver(self):
        self.idade += 1


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f'{self.nome} - Status: Matriculado')


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f'{self.nome} iniciou uma aula.')


class Funcionario(Pessoa):
    def __init__(self,nome,idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor
    
    def bater_ponto(self):
        print(f'{self.nome} bateu o ponto!')

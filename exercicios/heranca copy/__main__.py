from rich import print, inspect
from aluno import Aluno
from professor import Professor
from funcionario import Funcionario


a1 = Aluno('José', 17, "Informática", "T01")
print(a1.__dict__)
a1.fazer_matricula()
inspect(a1, methods=True)

p1 = Professor('Samuel', 37, 'Biologia', 'Mestrado')
p1.dar_aula()
inspect(p1, methods=True)
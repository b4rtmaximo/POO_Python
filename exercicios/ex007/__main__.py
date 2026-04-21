from rich import print, inspect
from classes import Pessoa, Aluno, Professor, Funcionario

def main():
    a1 = Aluno('José', 17, "Informática", "T01")
    print(a1.__dict__)
    a1.fazer_matricula()
    #inspect(a1, methods=True)

    p1 = Professor('Samuel', 37, 'Biologia', 'Mestrado')
    p1.fazer_niver()
    p1.dar_aula()
    #inspect(p1, methods=True)

    f1 = Funcionario("Cláudia", 27, "Secretária", "Secretaria")
    f1.fazer_niver()
    f1.bater_ponto()

    #x = Pessoa("Gustavo", 48)
    #x.fazer_niver()
    #inspect(x, methods=True)

    a1.estudar()
    p1.estudar()
    f1.estudar()

if __name__ == "__main__":
    main()
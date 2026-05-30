from rich import inspect

from classPersonagem import *




def main():
    guerreiro = Guerreiro("Aquiles",100)
    wizard = Mago("Gandalf", 100)
    inspect(guerreiro, methods=True)
    
    guerreiro.receber_dano(40)
    guerreiro.atacar(wizard, 30)
    wizard.curar()
    wizard.atacar(guerreiro, 23)




if __name__ == "__main__":
    main()
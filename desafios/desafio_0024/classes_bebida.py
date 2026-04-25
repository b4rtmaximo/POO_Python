from abc import ABC, abstractmethod

class Bebida(ABC):

    def __init__(self):
        pass   
    
    @abstractmethod
    def preparar(self):
        print(f"-- Iniciando o preparo... --\n1 - Preparar água a 100 graus Celsius.")


class Cafe(Bebida):

    def __init__(self):
        pass

    def preparar(self):
        super().preparar() 
        print(f"2 - Passando água pressurizada pelo pó de café moído." \
        "\n3 - Servindo em xícara pequena\n-- Bebida pronta. --")


class Cha(Bebida):

    def __init__(self):
        pass

    def preparar(self):
        super().preparar()
        print(f'2 - Mergulhando o sachê de ervas na água.\n3 - Servindo na caneca de porcelana com limão.\n-- Bebida pronta. --')
    

class Leite(Bebida):

    def __init__(self):
        pass

    def preparar(self):
        super().preparar()
        print(f"2 - Passando vapor pressurizado pelo leite.\n3 - Servindo na caneca grande, já com café.\n-- Bebida pronta. --")



cafe = Cafe()
cafe.preparar()   

cha = Cha()
cha.preparar()

milk = Leite()
milk.preparar()
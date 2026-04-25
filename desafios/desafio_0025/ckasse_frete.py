from abc import ABC, abstractmethod

class Transporte(ABC):

    def __init__(self,distancia = 0, frete = 0):
        self.distancia = distancia
        self.frete = frete

    @abstractmethod
    def calc_frete(self):
        pass

class Moto(Transporte):

    def __init__(self, distancia=0, frete=0):
        super().__init__(distancia, frete)

    def calc_frete(self):
        fator = 0.5
        self.frete = fator * self.distancia 
        print(f'Frete = R$ {self.frete}') 


class Caminhao(Transporte):

    def __init__(self, distancia=0, frete=0):
        super().__init__(distancia, frete)

    def calc_frete(self):
        fator = 1.5
        
        if self.distancia < 50:
            print(f'A distância de {self.distancia} Km não atende ao mínimo necessário.')
        else:
            self.frete = self.distancia * fator
            print(f'Frete = R$ {self.frete}') 
        

class Drone(Transporte):

    def __init__(self, distancia=0, frete=0):
        super().__init__(distancia, frete)

    def calc_frete(self):
        fator = 9.5
        
        if self.distancia > 10:
            print(f'A distância de {self.distancia} Km não atende ao máximo permitido')
        else:
            self.frete = self.distancia * fator
            print(f'Frete = R$ {self.frete}')         



frete1 = Moto(10)
frete1.calc_frete()

frete2 = Caminhao(30)
frete2.calc_frete()

frete3 = Drone(11)
frete3.calc_frete()
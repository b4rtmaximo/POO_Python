# Diagrama de classes de polígonos

from abc import ABC, abstractmethod
from math import pi

class Poligono(ABC):

    def __init__(self, qtd_lados):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Quadrado(Poligono):

    def __init__(self, lado=0):
        super().__init__(4)
        self.lado = lado

    def perimetro(self):
        perimetro = self.qtd_lados * self.lado
        print(f'O perímetro do quadrado é {perimetro} m')
    
    def area(self):
        area = self.lado * self.lado
        print(f'A área do quadrado é de {area} m²')


class Circulo(Poligono):

    def __init__(self, raio):
        super().__init__(0)
        self.raio = raio

    def perimetro(self):
        perimetro = 2 * pi * self.raio
        print(f'O perímetro do círculo é {perimetro:.2f} m')
    
    def area(self):
        area = pi * self.raio ** 2
        print(f'A área do círculo é de {area:.2f} m²')



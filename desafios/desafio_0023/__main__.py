from classes_poligono import Poligono, Quadrado, Circulo


def main():
    q1 = Quadrado(10)
    q1.perimetro()
    q1.area()

    c1 = Circulo(3)
    c1.area()
    c1.perimetro()

if __name__ == '__main__':
    main()
'''
Crie uma classe Churrasco, onde seja possivel informar quantas pessoas vão participar e mostrar quanto de carne deve ser comprado, o custo total do churrasco e o preço por pessoa.

CONSIDERE:
Consumo padrão: 400g por pessoa
Preço: R$82,40/Kg
'''
from rich import print
from rich.panel import Panel

class Churrasco:

    def __init__(self, nome, quant):
        self.nome = nome
        self.quant = quant        
    
    def custos(self):
        titulo = f'{self.nome}: {self.quant} pessoas'
        total_kg = self.quant * 0.4
        total_valor = total_kg * 82.4
        valor_unit = total_valor / self.quant

        texto = f'Recomendo comprar {total_kg} Kg de carne\nO custo total será de R${total_valor:.2f}\nCada pessoa terá que pagar R${valor_unit:.2f}'

        etiqueta = Panel(f'[yellow]{texto}[/]', title=f'{titulo}', style='white',width=40)

        return etiqueta


churras = Churrasco('Encontro Terceirão', 20)
print(churras.custos())
'''
Crie a classe Produto, onde podemos cadastrar nome e o preço. Crie também um método que mostra uma etiqueta de preço do produto.
'''
from rich import print
from rich.panel import Panel

class Produto:

    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def etiqueta(self):
        etiqueta = Panel(f'[white]{self.valor}[/]', title=f'{self.nome}', style='yellow',width=16, height=4)
        
        return etiqueta
    
p1 = Produto('iMAC', 'R$ 10.000,00')
print(p1.etiqueta())
from rich import print
from rich.panel import Panel

class Churrasco:
    #atributos de classe
    consumo_padrao = 0.4 
    preco_kg = 82.4

    def __init__(self, titulo, quant):
        self.titulo =  titulo
        self.participantes = quant

    def __str__(self):
        return f'Esse é {self.titulo} com {self.participantes} participantes'
    
    def calcular_qtd_carne(self) -> float:
        return self.participantes * Churrasco.consumo_padrao

    def calcular_custo_total(self) -> float:
        return self.calcular_qtd_carne() * Churrasco.preco_kg

    def calcular_custo_individual(self) -> float:
        return self.calcular_custo_total() / self.participantes

    def analisar(self):
        conteudo = f'Analisando [green]{self.titulo}[/] com [blue] {self.participantes} convidadados [/]'
        conteudo += f'\nCada participante comerá {Churrasco.consumo_padrao} Kg e cada quilo custa R$ {Churrasco.preco_kg:,.2f}'
        conteudo += f'\nRecomendo comprar {self.calcular_qtd_carne():,.3f} Kg de carne'
        conteudo += f'\nO custo total será de R$ {self.calcular_custo_total():,.2f}'
        conteudo += f'\nCada pessoa pagará R$ {self.calcular_custo_individual():,.2f}'

        painel = Panel(conteudo, title=self.titulo)
        print(painel)


c1 = Churrasco("Churras dos Amigos", 15)
c1.analisar()
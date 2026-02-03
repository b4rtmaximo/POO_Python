'''
Crie uma classe Livro, que vai simular a passagem de páginas de um livro, considerando também se o usuário chagou ao fim da leitura.
'''

from rich import print
from time import sleep

class Livro:

    def __init__(self, titulo, total):
        self.titulo = titulo
        self.total = total
        self.lido = 0 
        

    def passar_paginas(self, quantidade):
        print(f'Você esta lendo [blue]{self.titulo}[/] que tem [red]{self.total}[/] páginas.')
        if self.lido >= self.total:
            print('O livro já foi completamente lido!')
            return
        
        pagina_inicial = self.lido + 1
        pagina_final = min(self.lido + quantidade, self.total)
        
        for pagina in range(pagina_inicial, pagina_final + 1):
            print(f'Pág({pagina}) --> ', end='')
            sleep(0.5)
        
        self.lido = pagina_final
        
        if self.lido < self.total:
            print(f'Você parou na Página {pagina_final}')
        else:
            print('[red]Parabéns! Você terminou o livro![/]')


livro1 = Livro('100 Anos de Solidão', 20)
livro1.passar_paginas(10)
livro1.passar_paginas(11)
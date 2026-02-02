'''
Crie uma classe Livro, que vai simular a passagem de páginas de um livro, considerando também se o usuário chagou ao fim da leitura.
'''

'''
Crie uma classe Churrasco, onde seja possivel informar quantas pessoas vão participar e mostrar quanto de carne deve ser comprado, o custo total do churrasco e o preço por pessoa.

CONSIDERE:
Consumo padrão: 400g por pessoa
Preço: R$82,40/Kg
'''
from rich import print
from time import sleep

class Livro:

    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas 

    def passar_paginas(self, lido):
        self.lido = lido
        paginas = 1


        while paginas <= self.lido:
            print(f'Pág({paginas}) --> ',end='')
            sleep(0.5)
            paginas += 1
        print(f'Você parou na Página {paginas}')


livro = Livro('100 Anos de Solidão', 10)
print(livro.passar_paginas(5))
print(livro.passar_paginas(4))

from rich import print
from rich.panel import Panel

caixa = Panel('Esse aqui é um painel de exemplo')
print(caixa)

caixa_2 = Panel('[white]Esse aqui é um painel de exemplo[/] :+1:', title='Mensagem', style='yellow',width=40)
print(caixa_2)
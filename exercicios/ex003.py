from rich import inspect

class ContaBancaria:
    '''
    Docstring for ContaBancaria:
    Cria uma conta bancária e permite fazer saques e depósitos 
    '''
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f'Conta {self.id} criada com sucesso! Saldo atual de R$ {self.saldo:,.2f}')

    def __str__(self):
        return f'A conta n° {self.id} de {self.titular} possui R$ {self.saldo:,.2f} de saldo'

    def deposito(self, valor):
        self.saldo += valor
        print(f'Depósito de R$ {valor:,.2f} autorizado na conta {self.id}')

    def saque(self, valor):
        if valor > self.saldo:
            print(f'Saque NEGADO de R$ {valor:,.2f} na conta {self.id}: SALDO INSUFUCIENTE')
        else:
            self.saldo -= valor
            print(f'Saque de R$ {valor:,.2f} autorizado na conta {self.id}')
        
    

c1 = ContaBancaria(112, 'Gustavo', 3000)
c1.deposito(500)
c1.saque(20000)
print(c1)

inspect(c1)
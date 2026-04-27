from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel

class Funcionario(ABC):

    def __init__(self, nome, sal_bruto, salario=0, sal_min=1612, inss=7.5):
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.salario = salario
        self.sal_min = sal_min
        self.inss = inss

    @abstractmethod
    def cal_salario(self):
        pass
  
    def analisar_sal(self):
        media = self.salario / self.sal_min
        caixa_2 = Panel (f'O salário de [blue]{self.nome}[/] ({__class__.__name__}) é de [green]{self.salario}[/] e corresponde a [yellow]{media:.2f}[/] salários mínimos.', title='Análise de Salário', style='white',width=50)
        print(caixa_2)


class Horista(Funcionario):

    def __init__(self, nome, horas_trabalhadas, valor_hora, sal_min=1612, inss=7.5,sal_bruto=0, salario=0, ):
        super().__init__(nome, sal_bruto, salario, sal_min, inss)
        self.valor_hora = valor_hora
        self.horas_trabalhadas = horas_trabalhadas
        
    def cal_salario(self):
        self.sal_bruto = (self.horas_trabalhadas * self.valor_hora)*30
        self.salario = self.sal_bruto - (self.sal_bruto * (self.inss / 100))
        return self.salario
    
    def analisar_sal(self):
        return super().analisar_sal()


class Mensalista(Funcionario):

    def __init__(self, nome, sal_bruto, salario=0, sal_min=1612, inss=7.5):
        super().__init__(nome, sal_bruto, salario, sal_min, inss)

    def cal_salario(self):
        self.salario = self.sal_bruto - (self.sal_bruto*(self.inss/100))
        return self.salario
    
    def analisar_sal(self):
        return super().analisar_sal()
    


    
f1 = Horista("Maria", horas_trabalhadas=8, valor_hora=15)
f1.cal_salario()
f1.analisar_sal()

f2 = Mensalista("Tania", 4000)
f2.cal_salario()
f2.analisar_sal()
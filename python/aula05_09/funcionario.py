class Funcionario:
    contador = 1000
    BONIFICACAO = 0.15
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        self.id = Funcionario.contador
        Funcionario.contador+1

    def calcular_bonificacao(self):
        return self.salario*Funcionario.BONIFICACAO
    
    def mostrar_detalhes(self):
        print(f'id: {self.id}')
        print(f'nome: {self.nome}')
        print(f'salario: {self.salario}')
        b = self.calcular_bonificacao()
        print(f'Bonificação: {b}')
        sb = self.salario + b
        print(f'Salario + Bonificacao: {sb}')

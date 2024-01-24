
# Exercício – Calculadora Polimórfica
# Objetivo: Desenvolver uma calculadora que suporta várias operações matemáticas básicas, como adição, subtração,
# multiplicação e divisão, utilizando polimorfismo por sobrecarga. O sistema deve ser capaz de realizar essas operações
# em diferentes tipos de números (inteiros, decimais) e em diferentes números de argumentos.
# -----------------------

# Classes
# Objetos
# Métodos
# Herança
# Polimorfismo
# Encapsulamento
# Interfaces e Classes Abstratas
# Tratamento de Exceção (try-except e raise)
# Modificadores de visibilidade (private, protected, public)


from abc import ABC, abstractmethod
class Calculadora(ABC):
    def __init__(self, nome):
       self.__nome = nome

    @abstractmethod
    def calcular(self, a: float, b: float):
        pass

    @property
    def nome(self):
        return self.__nome

class Soma(Calculadora):
    def calcular(self, a: float, b: float) -> str:
        return f'A soma de {a} + {b} é {a + b}'
    
class Subtracao(Calculadora):
    def calcular(self, a: float, b: float) -> str:
        return f'A Subtração de {a} - {b} é {a - b}'

class Mutiplicacao(Calculadora):
    def calcular(self, a: float, b: float) -> str:
        return f'A mutiplicação de {a} * {b} é {a * b}'
    
class Divisao(Calculadora):

    def verificaValor(self, a, b) :
         if a == '' or b == '':
                raise TypeError

    def calcular(self, a: float, b: float) -> str:
        # para tratamento de erro 
        try:
            self.verificaValor(a, b)
            retorno = a / b
           
        except ZeroDivisionError:
            print('Operação não pode ser concluida, pois o divisor é "0"')
        except TypeError:
            print('Operação invalida')
        else:
            print(f'A divisão de {a} / {b} é { retorno}')
        finally:
            print('Fim da operação')


# link de estudo : https://docs.python.org/3/library/exceptions.html
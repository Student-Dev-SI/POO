# Objetivo: Desenvolver uma aplicação que permita o gerenciamento de diferentes animais, suas características e comportamentos.

# Requisitos:

# 1. Classe Animal:
# - Atributos:
# - `nome`: Representa o nome do animal (por exemplo, "Rex").
# - `tipo`: Define a classificação do animal (como "Mamífero", "Réptil", etc.).
# - `som`: Descreve o som característico que o animal faz (como "Latido", "Miado", etc.).
# - Construtor:
# - Inicializa os atributos `nome`, `tipo`, e `som`.

# - Métodos:
# - `setSom(String som)`: Permite alterar o som do animal.
# - `fazerSom()`: Imprime a ação de o animal fazer o seu som característico.
# - `alimentar()`: Imprime a ação de alimentar o animal.
# - `dormir()`: Imprime a ação do animal dormindo.
# - `mostrarInfo()`: Imprime as informações do animal.


class Animal:
    # set  atribuir valor
    # get pegar valor
    # conceito de encapsulamento
    # construtor 
    def __init__(self, nome, tipo, som):
        self.nome = nome
        self.tipo = tipo
        self.som = som

    def setSom(self, som):
        self.som = som
    
    def getSom(self):
        return self.som
    
    def setNome(self, nome):
        self.nome = nome
    
    def getNome(self):
        return self.nome
    
    def setTipo(self, tipo):
        self.tipo = tipo
    
    def getTipo(self):
        return self.tipo
    
    def fazerSom(self):
         return print(f'O animal {self.nome} faz o som {self.som}!')
    
    def mostrarInfo(self):
        print(f'nome: {self.nome}')
        print(f'tipo: {self.tipo}')
        print(f'som: {self.som}')
    
# tres animais fora da classe
def main():
    animal1 = Animal("Rodolpho", "porco", "roinc")
    animal2 = Animal("Bento", "gato", "mia")
    animal3 = Animal("Bob", "cao", "late")

    # chamando o animal que queremos e o que será reproduzido
    print(animal1.getSom())

    # para mudar o som 
    animal1.setSom("rooooooooc")
    print(animal1.getSom())

    # exibe
    animal2.fazerSom()
    
    animal3.mostrarInfo()

# __ = é uma variavél que vai receber um valor então no python ele recebe esse __
# inicializar 
# if __name__=="__main__":
    # main()
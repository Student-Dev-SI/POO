# Objetivo: criar e manipular uma classe Carro que represente as características e comportamentos básicos de um carro.

# Parte 1: Declaração da Classe e Atributos
# 1. Crie uma classe chamada Carro.
# 2. Declare os seguintes atributos privados:
# - `marca`: String que armazena a marca do carro.
# - `modelo`: String que armazena o modelo do carro.
# - `ano`: Inteiro que armazena o ano do carro.
# - `ligado`: Booleano que indica se o carro está ligado ou desligado (verdadeiro ou falso).

# Parte 2: Construtor
# 1. Crie um construtor que aceite os parâmetros `marca`, `modelo` e `ano`.
# - Inicialize os atributos com os valores fornecidos.
# - Inicialize o atributo `ligado` como `false`, já que o carro começa desligado.

# Parte 3: Métodos
# 1. Crie um método `ligar` sem parâmetros:
# - Atribua o valor verdadeiro ao atributo `ligado`.
# - Mostre a mensagem "Carro ligado!".
# 2. Crie um método `desligar` sem parâmetros:
# - Atribua o valor falso ao atributo `ligado`.
# - Mostre a mensagem "Carro desligado!".
# 3. Crie um método `mostrarInfo` sem parâmetros:
# - Mostre as informações do carro, incluindo a marca, o modelo, o ano e se está ligado ou não.

# Parte 4: Main
# Crie um método main para demonstrar a classe:
# - Instancie um objeto da classe Carro com os valores "Ford", "Fiesta", 2020.
# - Chame o método `mostrarInfo` para mostrar as informações iniciais do carro.
# - Chame o método `ligar` para ligar o carro e depois chame `mostrarInfo` novamente.
# - Chame o método `desligar` para desligar o carro e depois chame `mostrarInfo` mais uma vez.

class Carro:
    #construtor
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ligado = False

    def setMarca(self, marca):
        self.marca = marca
    
    def getMarca(self):
        return self.marca

    def setModelo(self, modelo):
        self.modelo = modelo

    def setAno(self, ano):
        self.ano = ano
    
    def getAno(self):
        return self.ano
    
    def getModelo(self):
        self.modelo

    def ligar(self):
        self.ligado = True
        print('Carro ligado!')
    
    def desligar(self):
        self.ligado = False
        print('Carro desligado!')

    def mostrarInfo(self):
        print(f'marca: {self.marca}')
        print(f'modelo: {self.modelo}')
        print(f'Ano: {self.ano}')
        print(f'ligado: {self.ligado}')

def main():
    carro1 = Carro("Volkswagen", "Gol", "2019")
    carro2 = Carro("Hyundai", "H20", "2017")
    carro3 = Carro("Chevrolet", "Onix", "2020")
    carro4 = Carro("Fiat Mobi", "4", "2018")
    carro5 = Carro("Ford", "Fiesta", "2020")

    print(f'mostra a marca: {carro1.getMarca()}')

    print(f'*******ligar o  {carro2.getMarca()} *********')
    carro2.ligar()

    print(f'*******ligar o {carro3.getMarca()} *********')
    carro3.ligar()
    print(f'*******desligar o {carro3.getMarca()} *********')
    carro3.desligar()
    
   
    print(f'*******Mostar informação do carro {carro2.getMarca()} *********')
    carro2.mostrarInfo()

    print(f'*******Mostar informação do carro {carro5.getMarca()}*********')
    carro5.mostrarInfo()

# inicializar 
if __name__=="__main__":
    main()
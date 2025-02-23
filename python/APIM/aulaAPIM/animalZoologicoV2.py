class DadosVazios(Exception):
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem

    def __str__(self) -> str:
        return f"O Campo: {self.mensagem} não é permitido valor vazio!"

class Animal:
    def __init__(self, nome: str, especie: str, idade: int) -> None:

        if nome == "":
            raise DadosVazios(f"nome")
        
        elif especie == "":
            raise DadosVazios(f"especie")
        
        elif idade == "":
            raise DadosVazios(f"idade")

        else:
            self.nome = nome
            self.especie = especie
            self.idade = idade
            # atributo de classe 
            Zoologico.capacidade
            # Zoologico.animais.append(self)
            Zoologico.adicionar_animal(self)

    # representação dos atributos
    def __repr__(self) -> str:
        return f"{self.nome}, {self.especie}, {self.idade}"


class Zoologico:
    capacidade = 5
    animais = []
    
    def adicionar_animal(self) -> None:
        print(self)
        # if len(self) < self.capacidade:
        #     self.append(self.animais)
        # else:
        #     print("limite excedido!")

    def mostrar_animais(self) -> None:
        for animal in self.animais:
            print(animal)

        print(f"capacidade : {self.capacidade}")

# listaAnimal = Zoologico()

# animal1 = Animal('Leao', 'mamifero', 25)
# animal2 = Animal('Tigre', 'mamifero', 15)
# animal3 = Animal('Vaca', 'mamifero', 20)
# animal4 = Animal('Golfinho', 'mamifero', 30)
# animal5 = Animal('Golfinho', 'mamifero', 30)
# animal6 = Animal('Golfinho', 'mamifero', 30)
# para erro 
# animal4 = Animal("nome", "", 30)

# listaAnimal.mostrar_animais()

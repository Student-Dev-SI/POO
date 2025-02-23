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

    # representação dos atributos
    def __repr__(self) -> str:
        return f"{self.nome}, {self.especie}, {self.idade}"


class Zoologico:
    def __init__(self, capacidade: int) -> None:
        self.capacidade = capacidade
        self.animais = []

    def adicionar_animal(self, animal: Animal) -> None:
        if len(self.animais) < self.capacidade:
            self.animais.append(animal)
        else:
            print("limite excedido!")

    def mostrar_animais(self) -> None:
        for animal in self.animais:
            print(animal)

        print(f"capacidade : {self.capacidade}")


animal1 = Animal('Leao', 'mamifero', 25)
animal2 = Animal('Tigre', 'mamifero', 15)
animal3 = Animal('Vaca', 'mamifero', 20)
animal4 = Animal('Golfinho', 'mamifero', 30)
# para erro 
# animal4 = Animal("nome", "", 30)


listaAnimal = Zoologico(5)

listaAnimal.adicionar_animal(animal1)
listaAnimal.adicionar_animal(animal2)
listaAnimal.adicionar_animal(animal3)
listaAnimal.adicionar_animal(animal4)

listaAnimal.mostrar_animais()

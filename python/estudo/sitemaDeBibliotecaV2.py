# Objetivo: Criar um sistema simplificado de biblioteca que permita gerenciar livros e usuários. O
# sistema deve ser capaz de realizar empréstimos, devoluções e rastrear o status dos livros.

# Parte 1: Definir Classes
# 1. Classe Livro:
# - Atributos: título, autor, ISBN, status (emprestado ou disponível).
# - Métodos: emprestar, devolver.
# 2. Classe Usuário:
# - Atributos: nome, ID, livros_emprestados (lista de livros).
# - Métodos: emprestar_livro, devolver_livro.

# Parte 2: Implementar Métodos

# 1. Implemente os métodos de empréstimo e devolução na classe Livro.
# 2. Implemente os métodos para emprestar e devolver livros na classe Usuário, ajustando o status
# dos livros emprestados.


class Livro:
    def __init__(self, titulo: str, autor: str, ISBN: int) -> None:
        self.titulo = titulo
        self.autor = autor
        self.ISBN = ISBN
        self.status = "Disponível"

    def emprestar(self) -> None:
        self.status = "Reservado"

    def devolucao(self) -> None:
        self.status = "Disponível"
        pass

    def __repr__(self) -> str:
        return f"{self.titulo}, {self.autor}, {self.ISBN}, {self.status}"

class Usuario:
    def __init__(self, nome: str, ID: int) -> None:
        self.nome = nome
        self.ID = ID
        self.livros_emprestados = []

    def retirar_livro(self, livro: Livro, nomeInserido: str) -> None:

        self.verificaDados(nomeInserido)
        if livro.status == "Disponível":
            self.livros_emprestados.append(livro)
            livro.emprestar()
            print("Livro Adicionado")
        else:
            print("Livro não está disponivél para reserva")

    def devolver_livro(self, livro: Livro, nomeInserido: str) -> None:
         
        self.verificaDados(nomeInserido)
        if livro in self.livros_emprestados:
            self.livros_emprestados.remove(livro)
            livro.devolucao()
            print("Livro Removido da lista")
        else:
            print("Livro não está na lista de empréstimos")


    def verificaDados(self, nomeInserido: str):
        if nomeInserido.lower() == self.nome:
            print("Usuario encontrado")
        else:
            print("Usuario Não encontrado")


livro1 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1)
livro2 = Livro("Romeu E Julieta", "William Shakespeare", 2)
livro3 = Livro("Dom Quixote De La mancha", "Miguel de Cervantes", 3)
livro4 = Livro("Orgulho E Preconceito", "Jane Austen", 4)

u1 = Usuario("Roberto", 1)
u2 = Usuario("Joao", 2)
u3 = Usuario("Maria", 3)
u4 = Usuario("Bernardo", 4)

u1.retirar_livro(livro1, input('Insira seu nome cadastrado na base'))
u1.retirar_livro(livro2, input('Insira seu nome cadastrado na base'))

u3.retirar_livro(livro4, input('Insira seu nome cadastrado na base'))
u4.retirar_livro(livro3, input('Insira seu nome cadastrado na base'))

# u1.livros_emprestados
# u1.devolver_livro(livro2, 'Maria')


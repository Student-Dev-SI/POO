class Usuario:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    def fazerReserva(self, livro):
        livro.reservar()

    def fazerDevolucao(self, livro):
        livro.devolver()
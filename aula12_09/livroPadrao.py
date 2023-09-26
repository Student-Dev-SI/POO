from livro import Livro, Status
from datetime import datetime, timedelta

class LivroPadrao(Livro):
    def __init__(self, titulo, autor, isbn):
        super().__init__(titulo, autor, isbn)
        self.dataDeDevolucao = None

    def reservar(self):
        if self.status == Status.DISPONIVEL:
            self.dataDeDevolucao = datetime.now() + timedelta(days=7)
            self.status = Status.DISPONIVEL
            return 'Livro resevado'
        else:
            return "Livro indisponivel"
        
    def __str__(self):
        return f"{self.titulo},{self.autor}, {self.isbn}, {self.dataDeDevolucao}"    


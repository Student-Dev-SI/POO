from abc import ABC, abstractmethod
from enum import Enum

class Status(Enum):
    DISPONIVEL = "disponivel"
    INDISPONIVEL = "indisponivel"

class Tema(Enum):
    FISICA = 'fisica'
    QUIMICA = 'quimica'

class Livro(ABC):
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.titulo = isbn
        self.status = "Disponivel"
        
    @abstractmethod
    def reservar(self):
        raise NotImplementedError("O método deve ser implementado nas sub")
    
    def devolver(self):
        self.status = "Disponivel"
        return self.status 
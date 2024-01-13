
from datetime import datetime 


class Participante:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.ingressosComprados = []
      
    def setNome(self, nome):
        self.nome = nome
    
    def getNome(self):
        return self.nome
    
    def setEmail(self, email):
        self.email = email
    
    def getEmail(self):
        return self.email
    
    def mostrarIngressos(self):
        return self.ingressosComprados
    
    

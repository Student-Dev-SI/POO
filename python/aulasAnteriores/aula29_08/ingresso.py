
from datetime import datetime 

class Ingresso:
    def __init__(self, participante, evento):
        self.status = True
        self.evento = evento
        self.dataCompra = datetime.now()
        self.participante = participante
        
    def getDataCompra(self):
        return self.dataCompra
    
    def setStatusIngressos(self, status):
        self.status = status
    
    def getStatusIngressos(self):
        return self.status
    
    def getParticipante(self):
        return self.participante

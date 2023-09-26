class Evento:
    def __init__(self, nomeEvento, localEvento, dataEvento, capacidadeEvento) :
        self.nomeEvento = nomeEvento
        self.localEvento = localEvento
        self.dataEvento = dataEvento
        self.capacidadeEvento = capacidadeEvento
        self.inscritosEvento = []

    def mostraInfoEvento(self):
        print(f'nome: {self.nomeEvento} | local: {self.localEvento} | data: {self.dataEvento}')

    def cancelarEvento(self):
        pass

    def incluirEventos(self):
        pass

    def setNomeEvento(self, nomeEvento):
        self.nomeEvento = nomeEvento

    def getNomeEvento(self):
        return self.nomeEvento
    
    def setLocalEvento(self, localEvento):
        self.localEvento = localEvento

    def getLocalEvento(self):
        return self.localEvento
    
    def setDataEvento(self, dataEvento):
        self.dataEvento = dataEvento

    def getDataEvento(self):
        return self.dataEvento
    
    def setCapacidadeEvento(self, capacidadeEvento):
        self.capacidadeEvento = capacidadeEvento

    def getCapacidadeEvento(self):
        return self.capacidadeEvento
    

    


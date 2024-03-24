# link: https://classroom.google.com/c/NjE2NDE5MDI5MTY0/m/NTg5NDI0MjAyNjU1/details

class Evento:
   def __init__(self, nomeEvento: str, localEvento: str, dataEvento: str, capacidadeEvento: int, inscritosEvento: str) -> None:
      self.nomeEvento = nomeEvento
      self.localEvento = localEvento
      self.dataEvento = dataEvento
      self.capacidadeEvento = capacidadeEvento
      self.inscritosEvento = inscritosEvento      
      self.eventos = []
      pass
   
   def getEventos(self):
      pass
   
   def mostraInfoEvento(self):
      pass
   
   def cancelarEvento(self):
      pass
   
   def incluirInscrito(self):
      self.inscritosEvento = []
      pass
   

class Ingresso:
   def __init__(self, participante: str, evento: str, dataCompra: str, statusIngresso: bool) -> None:
      pass


class Participante:
   def __init__(self, nome: str, email: str, ingressosComprados) -> None:
      pass
   
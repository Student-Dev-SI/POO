class Animal:
    def __init__(self, nome: str, tipo: str, som: str) -> None:
        self.nome = nome
        self.tipo = tipo
        self.som = som

    def setSom(self, novoSom: str) -> str:
        self.som = novoSom
        return f' o novo som do animal {self.nome} é {novoSom}'
    
    @property
    def getSom(self) -> str:
        return f' o som do animal é { self.som }'
    
    def setAlimento(self, comida: str) -> str:
        self.comida = comida
        return self.comida
       
    @property
    def getAlimento(self ) -> str:
        return f' A comida favorita é { self.comida}'
    
    def setDormir(self, sono: str) -> str:
        self.sono = sono
        return self.sono
    
    @property
    def getDormir(self ) -> str:
        return f' A comida favorita é { self.sono }'
    
    def mostrarInfo(self) -> str:
        print(f'nome: {self.nome}')
        print(f'tipo: {self.tipo}')
        print(f'som: {self.som}')
        print(f'comida: {self.comida}')
        print(f'sono: {self.sono}')


a1 = Animal('Rex', 'Mamifero', 'Latido')
a1.setAlimento('come o que caça')
a1.setDormir('12 Horas de sono')
a1.mostrarInfo()
# a1 = setDormir('12 Horas de sono')
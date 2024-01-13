class LivroReferencia(Livro):
    def __init__(self, titulo, autor, isbn, tema):
        super().__init__(titulo, autor, isbn)
        self.tema = tema


    def reservar(self):
        return "Livro referencia não pode ser"
    
    def __str__(self):
        return f"{self.titulo},{self.autor}, {self.isbn}, {self.tema}"
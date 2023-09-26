from livro import Livro
from usuario import Usuario
from livroPadrao import LivroPadrao
from livroReferencia import LivroReferencia, Tema
from arquivo import Arquivo

livro1 = LivroPadrao('X','XXX', 123)
livro2 = LivroReferencia('X','XXX', 123, Tema.Fisica)
print(str(Livro))

usuario1 = Usuario(170, "mario")
usuario1.fazerReserva(livro1)
usuario1.fazerReserva(livro2)
usuario1.fazerDevolucao(livro1)
livrosTXT = Arquivo('livro.txt')
livrosTXT.gravar(str(livro1))
livrosTXT.gravar(str(livro2))
print('***Metodo ler()')
print(livrosTXT.ler())
print('***Método LerLinha***')
print(livrosTXT.lerLinha())
print(livrosTXT.lerLinhas())
from evento import Evento
from ingresso import Ingresso
from participante import Participante

def main():
    evento1 = Evento("Show do Alcione", "Morumbi", "05-09-2023 23:00", 1000)
    evento2 = Evento("Show do Beyonce", "Morumbi", "25-09-2023 23:00", 2000)
    evento3 = Evento("Show do Zéca Pagodinho", "Morumbi", "28-09-2023 23:00", 3000)

    participante = Participante("João", "joao@gmail.com")
    participante = Participante("Maria", "maria@gmail.com")

    if __name__== "__main__":
        main()
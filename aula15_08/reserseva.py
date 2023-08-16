
import time

salas = { "sala A":"disponível","sala B":"disponível","sala C":"disponível","sala D":"disponível", "sala E":"disponível"}
# sala = str()
while True:
    print('****Menu de opçöes*****')
    print('1 - Listar salas disponíveis: ')
    print('2 - Reservar uma sala')
    print('3 - Cancelar reserva de uma sala')
    print('4 - Sair')
    opcao = int(input('Selecione a opção desejada: '))
    if opcao == 1:
        #visualizar salas e verifica se estao disponivéis
        for k,v in salas.items():
            print(k,v)
    elif opcao == 2:
        #reserva uma sala
 
        salaSelecionada = input("Escolha a sala desejada: ")
      
        # for salaIndividual in salas:
        #     sala = salaIndividual
        #     if (salaSelecionada == sala):
        #         salas[salaSelecionada] = "indisponível"
        #         print("Salas agendadas com sucesso!")

        # outra forma de fazer 
        if salaSelecionada in salas:
            salas[salaSelecionada] = "indisponível"
            print("Salas agendadas com sucesso!")
        else:
            print("Sala inválido ou não encontrado")
        
    elif opcao == 3:
        #excluir a reserva

        salaSelecionada = input("Escolha a sala que desejada retirar da reserva: ")

        if salaSelecionada in salas:
            salas[salaSelecionada] = "disponivel"
            print("Salas exckuida com sucesso!")
        else:
            print("Sala inválido ou não encontrado")
      
    elif opcao == 4:
        #finalizar programa
        resposta = input("Deseja Finalizar s/n: ")
        if(resposta.lower() != "n" or resposta.lower() != "nao" or resposta.lower() != "não"): 
            break
        else:
            continue
    else:
        print('opcao invalida')
        time.sleep(3)
        continue
import random


jogador = ""
computador = ""
escolhas = ["pedra", "papel", "tesoura"]
vjogador = 0
vcomputador = 0
empates = 0
 

while True:
    print("Jogo Jokenpô")
    print("\n")
    print("Opções")
    print("Pedra")
    print("Papel")
    print("Tesoura")
    print("\n")
    jogador = input("Digite sua opção: ")
    computador = random.choice(escolhas)
    print(jogador, computador)

    if jogador == computador:
        print('empate!')
        empates +=1

    elif (jogador=='pedra' and computador=='tesoura') or (jogador=='pedra' and computador=='papel') or (jogador=='tesoura' and computador=='papel'):
        print('O jogador ganhou a partida!')
        vjogador +=1
    else:
        print('Você perdeu!')
        vcomputador +=1

    print('Placar')
    print(f'Jogador: {vjogador}')
    print(f'computador: {vcomputador}')
    print(f'Empate: {empates}')
    resposta = input("Deseja continuar s/n")
    if resposta == "n":
        break

import time;

tarefas = {}
id = 0
while True:
    print('****Gerenciador de tarefas****')
    print('1 - Criar tarefa')
    print('2 - Visualizar tarefa')
    print('3 - Excluir tarefa')
    print('4 - Sair')
    print('**************')
    opcao = int(input('Entre com a opção desejada: '))
    if opcao == 1:
        #incluir tarefa
        descricao = input('entre com a tarefa: ')
        tarefas [id] = descricao
        id+=1
    elif opcao == 2:
        #visualizar tarefa
        print("***lista de tarefas***")
        for k, v in tarefas.items():
            print(k,v)
    elif opcao == 3:
        #excluir tarefa
        idExclusao = int(input("Entre com id da tarefa a ser excluída:"))
        if idExclusao in tarefas:
            del tarefas[idExclusao]
        else:
            print("id inválido ou não encontrado")
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
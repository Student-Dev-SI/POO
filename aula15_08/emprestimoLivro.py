import time;

emprestimoLivros = {'livro':str(), 'titulo':str(), 'nome': str()}
id = 0
while True:
    print('****Gerenciador de tarefas****')
    print('1 - Criar tarefa')
    print('2 - Visualizar tarefa')
    print('3 - Excluir tarefa')
    print('4 - Excluir tarefa')
    print('5 - Sair')
    print('**************')
    opcao = int(input('Entre com a opção desejada: '))
    if opcao == 1:
        #incluir livro
        livro = input('entre com a tarefa: ')
        # emprestimoLivros.append(livro)
        # print(dict(emprestimoLivros))
        # print(emprestimoLivros)
        # print(emprestimoLivros [livro])

        # if livro in emprestimoLivros:
        #     emprestimoLivros[livro] = livro
        #     print(emprestimoLivros)
        print(emprestimoLivros[livro].append(livro))
            
        id+=1
    elif opcao == 2:
        #visualizar/listar livro
        print("***lista de tarefas***")
        
        for l, t, n in emprestimoLivros.items():
            print(l,t, n),
    elif opcao == 3:
        #emprestar livro
        idExclusao = int(input("Entre com id da tarefa a ser excluída:"))
        if idExclusao in tarefas:
            del tarefas[idExclusao]
        else:
            print("id inválido ou não encontrado")
    elif opcao == 4:
        # ver emprestimo de  livro
        idExclusao = int(input("Entre com id da tarefa a ser excluída:"))
        if idExclusao in tarefas:
            del tarefas[idExclusao]
        else:
            print("id inválido ou não encontrado")
    elif opcao == 5:
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
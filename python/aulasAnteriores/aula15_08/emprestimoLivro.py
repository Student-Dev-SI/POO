# Descrição: Você está desenvolvendo um sistema simples de gerenciamento para uma biblioteca. O sistema permite que os
# usuários realizem as seguintes ações:

# 1. Adicionar livro: O usuário pode adicionar um novo livro à lista de livros da biblioteca, fornecendo o título do livro.
# 2. Listar livros: O usuário pode listar todos os livros disponíveis na biblioteca.
# 3. Emprestar livro: O usuário pode emprestar um livro, fornecendo o título do livro e o nome do leitor. Se o livro já estiver
# emprestado, uma mensagem de erro será exibida.
# 4. Ver empréstimos: O usuário pode visualizar todos os empréstimos ativos, mostrando o título do livro e o nome do leitor que
# o emprestou.
# 5. Sair: O usuário pode sair do sistema.

# O código fornecido representa uma implementação desse sistema. Seu trabalho é entender o código e adicionar as seguintes
# funcionalidades:

# 1. Validação de empréstimo: Antes de emprestar um livro, verifique se o livro existe na lista de livros. Se o livro não existir ou
# já estiver emprestado, exiba uma mensagem de erro.
# 2. Devolução de livro: Adicione uma opção para permitir que os leitores devolvam livros emprestados. Quando um livro é
# devolvido, ele deve ser removido da lista de empréstimos.
# 3. Pesquisar livro: Adicione uma opção para permitir que os usuários pesquisem por um livro específico na lista de livros.
# 4. Salvar e carregar dados: Implemente funcionalidades para salvar e carregar os dados da biblioteca em um arquivo, de
# modo que as informações de livros e empréstimos sejam mantidas entre as execuções do programa.

import time;

livros = {}
emprestimo = []
id = 0
while True:
    print('****Gerenciador de emprestimo****')
    print('1 - Adicionar livro')
    print('2 - Listar livros')
    print('3 - Emprestar livro')
    print('4 - Ver empréstimos')
    print('5 - Sair')
    print('**************')
    opcao = int(input('Entre com a opção desejada: '))
    if opcao == 1:
        #incluir livro
        nomeDoLivro = input('Qual o nome do Livro: ')     
        livros [id] = nomeDoLivro        
        id+=1
    elif opcao == 2:
        #visualizar/listar livro
        print("***lista Os Livros***")
        
        for id, livro in livros.items():
            print(id, livro),
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
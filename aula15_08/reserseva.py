
salas = { "sala A":"disponivel","sala B":"disponivel","sala C":"disponivel","sala D":"disponivel", "sala E":"disponivel"}

print('1 - Listar salas disponíveis: ')
print('2 - Reservar uma sala')
print('3 - Cancelar reserva de uma sala')
print('4 - Sair')
opcao = int(input('Selecione a opção desejada:'))
if opcao == 1:
   for k,v in salas.items():
       print(k,v)
elif == 2:
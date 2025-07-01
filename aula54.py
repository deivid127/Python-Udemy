"""
Faça uma lista de comprar com listas
O usuário deve ter a possibiliadade de
inserir, apahar e listas valores da sua lista
Não permita que o programa quebre com
erro de índices inexistentes na lista
"""
import os


lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        os.system('cls')

        if len(lista) == 0:
            print('Não há nada para deletar.')

        for i, valor in enumerate(lista):
            print(i, valor)

        if len(lista) >= 1:
            indice_str = input('Escolha um índice para apagar: ')
        try: 
            indice = int(indice_str)
            del lista[indice]
        
        except:
            print('Não foi possível apagar esse índice.')
    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('Não há nada para listar.')

        for i, valor in enumerate(lista):
            print(i, valor)
        


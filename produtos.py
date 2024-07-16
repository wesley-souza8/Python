import os

produtos = []

while True:
    escolha = input('Selecione uma opção\n[i]nserir, [a]pagar, [l]istar ou [s]air: ')

    while len(escolha) > 1:
        print('Insira somente a primeira letra da opção desejada.')
        escolha = input('Selecione uma opção\n[i]nserir, [a]pagar ou [l]istar: ')

    while escolha.lower() not in ('i','a','l','s'):
        print('Opção desejada inválida')
        escolha = input('Selecione uma opção\n[i]nserir, [a]pagar ou [l]istar: ')

    if escolha.lower() == "a":
        os.system('cls')
        if len(produtos) == 0:
            print('Não há produtos a serem apagados')
        else:
            for indice, nome in enumerate(produtos):
                print(indice, nome)
            try:
                apagar = int(input('dígite o índice do produto a ser apagado: '))
                produtos.pop(apagar)
            except ValueError:
                print('Insira um valor inteiro para realizar o apagamrnto do produto')
            except:
                print('O Indice informado não existe')
    elif escolha.lower() == "i":
        os.system('cls')
        novo = input('Digite o nome do produto a ser inserido: ')
        produtos.append(novo)
    elif escolha.lower() == "l":
        os.system('cls')
        if len(produtos) == 0:
            print('Não há produtos a serem listados')
        else:
            for indice, nome in enumerate(produtos):
                print(indice, nome)
    else:
        os.system('cls')
        print('Você está saindo da consulta')
        break
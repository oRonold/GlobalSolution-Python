from funcoes import cadastro_doador_e_doacao, cadastro_donatario, lista_de_alimentos_doacao

def menu():
    print('Bem vindo ao menu de cadastro e doações de alimentos para as regiões da capital de São Paulo!')
    print('Siga as instruções abaixo\n')

    print('1 - Cadastro e doação de alimentos')
    print('2 - Cadastro de donatário(necessita de assistencia de doações)')
    print('3 - Criar lista de alimentos para doar')

    opcao_escolhida = int(input('Digite a opção desejada: '))

    if opcao_escolhida == 1:
        cadastro_doador_e_doacao()

    elif opcao_escolhida == 2:
        cadastro_donatario()

    elif opcao_escolhida == 3:
        lista_de_alimentos_doacao()

    else:
        print('Opção invalida')

menu()
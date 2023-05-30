def cadastro_doador_e_doacao():
    print('Bem-vindo a sessão de cadastro temporario de doadores!')
    print('Por favor preencha os campos abaixo\n')

    nome_doador = input('Digite seu nome completo: ')
    data_nascimento = int(input('Digite a sua data de nascimento: '))
    cpf = input('Digite seu CPF: ')
    regiao = input('Digite sua regiao em que voce mora em São Paulo: \n')
    print(f'Parabens {nome_doador} o seu cadastro foi finalizado! Segue as informações abaixo: \n')
    print(f'Data de nascimento: {data_nascimento}')
    print(f'CPF: {cpf}')
    print(f'Região cadastrada: {regiao}')
    print('Cadastro finalizado! A seguir voce podera continuar para a doação ou sair, caso escolha sair o cadastro precisara ser feito novamente, pois ele é temporario')
    sim_nao = input('Voce deseja continuar para a doação?(s/n) ')
    if sim_nao == 'n':
        print('Sessão cadastro encerrado, seleciona a opção 1 para criar um novo cadastro temporário')
        exit()
    else:
        print('A seguir voce')
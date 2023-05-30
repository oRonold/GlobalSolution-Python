def cadastro_doador_e_doacao():
    print('Bem-vindo a sessão de cadastro temporario de doadores de São Paulo!')
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
    elif sim_nao == 's':
        print('A seguir voce podera realizar a sua doação para a ONG mais proxima da sua região\n')
        alimento = input('Qual alimento voce quer doar? ')
        qtd = float(input('Qual a quantidade em KG? '))
        regiao_doacao = input('Digite em qual região voce quer que a sua doação seja redirecionada em São Paulo:(norte/sul/leste/oeste) ')
        if regiao_doacao == 'sul':
            print('Perfeito, a sua doação sera direcionada para o galpão da Cruz Vermelha Brasileira')
        elif regiao_doacao == 'oeste':
            print('Excelente, a sua doação sera direcionada para o depósito da FUSSP(Fundo Social de São Paulo)')
        elif regiao_doacao == 'leste':
            print('Ótimo, a sua doação será direcionada para a Associação Fenix, na zona leste')
        elif regiao_doacao == 'norte':
            print('Excelente, a sua doação será direcionada para o Banco de Alimentos localizado na zona Norte')
        
        transporte = input('Agora o transporte do alimento, a sua preferencia é ')

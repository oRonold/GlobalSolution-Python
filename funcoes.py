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
            print('Ótimo, a sua doação será direcionada para a ONG Palavra Viva, na zona leste')
        elif regiao_doacao == 'norte':
            print('Excelente, a sua doação será direcionada para o Banco de Alimentos localizado na zona Norte')
        
        print('A seguir conversaremos sobre o transporte do alimento')
        print('No caso da transportadora ser selecionada, a Instituição selecionada precisara ser contatada, uma taxa será cobrada para o transporte')
        transporte = input('O transporte do alimento será realizado pela sua pessoa ou por uma transportadora?(por mim/transportadora')
        if transporte == 'por mim':
            if regiao_doacao == 'sul':
                print('O galpão da cruz vermelha se localiza na: Av. Moreira Guimarães, 699, Indianópolis')
        elif transporte == 'por mim':
            if regiao_doacao == 'oeste':
                print('O depósito da FUSSP se localiza na: Av. Marechal Mario Guedes, 301, no Jaguaré')
        elif transporte == 'por mim':
            if regiao_doacao == 'leste':
                print('O depósito da ONG Palavra Viva se localiza na: Rua Dr. Camilo Haddad, 186 Altos - Parque São Lucas')
        elif transporte == 'por mim':
            if regiao_doacao == 'norte':
                print('O depósito da ONG Banco de Alimentos Rua Sobral Júnior, 264 - Vila Maria Alta')
        elif transporte == 'por mim':
            if regiao_doacao == 'transportadora':
                print('Por favor, digite seu endereço:\n')
                logradouro = input('Logradouro: ')
                numero = int(input('Digite o seu numero: '))
                cep = input('Digite seu CEP: ')
                bairro = input('Digite seu bairro: ')

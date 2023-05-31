from xml.etree.ElementTree import SubElement


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
        
        
        print('A seguir conversaremos sobre o transporte do alimento')
        print('No caso da transportadora ser selecionada, a Instituição selecionada precisara ser contatada, uma taxa será cobrada para o transporte')
        
        #if transporte == 'eu':
        regiao_doacao = input('Digite em qual região voce quer que a sua doação seja redirecionada em São Paulo:(norte/sul/leste/oeste) ')

        if regiao_doacao == 'sul':
            transporte = input('O transporte do alimento será realizado pela sua pessoa ou por uma transportadora?(eu/transportadora) ')
            if transporte == 'eu':
                print('A Instituição da sua região se chama Cruz Vermelha de São Paulo')
                print('Se localiza na: Av. Moreira Guimarães, 699 - Indianópolis')
        elif regiao_doacao == 'oeste':
            transporte = input('O transporte do alimento será realizado pela sua pessoa ou por uma transportadora?(eu/transportadora) ')
            if transporte == 'eu':
                print('Excelente, a sua doação sera direcionada para o depósito da FUSSP(Fundo Social de São Paulo)')
                print('Se localiza na: Av. Marechal Mario Guedes, 301, no Jaguaré')
        elif regiao_doacao == 'leste':
            transporte = input('O transporte do alimento será realizado pela sua pessoa ou por uma transportadora?(eu/transportadora) ')
            if transporte == 'eu':
                print('Ótimo, a sua doação será direcionada para a ONG Palavra Viva, na zona leste')
                print('Se localiza na: Rua Dr. Camilo Haddad, 186 Altos - Parque São Lucas')
        elif regiao_doacao == 'norte':
            transporte = input('O transporte do alimento será realizado pela sua pessoa ou por uma transportadora?(eu/transportadora) ')
            if transporte == 'eu':
                print('Excelente, a sua doação será direcionada para o Banco de Alimentos localizado na zona Norte')
                print('Se localiza na: Rua Sobral Júnior, 264 - Vila Maria ') 

        if regiao_doacao == 'transportadora':
            print('Por favor, digite seu endereço:\n')
            logradouro = input('Logradouro: ')
            numero = int(input('Digite o seu numero: '))
            cep = input('Digite seu CEP: ')
            bairro = input('Digite seu bairro: ')
            print('Endereço cadastro, resumo da operação:\n')
            print(f'Logradouro: {logradouro}')
            print(f'Numero: {numero}')
            print(f'CEP: {cep} ')
            print(f'bairro {bairro}')
            print('Perfeito! Resumo das informações cadastradas:\n')
            print(f'Logradouro: {logradouro}')
            print(f'Numero da residencia: {numero}')
            print(f'CEP: {cep}')
            print(f'Bairro: {bairro}')

def cadastro_donatario():
    print('Bem vindo a sessão de cadastro de donatário')
    print('Por favor preencha os campos abaixo:\n')
    nome = input('Digite seu nome: ')
    cpf = input('Digite seu CPF: ')
    data_nascimento = input('Digite sua data de nascimento: ')
    logradouro = input('Digite seu logradouro: ')
    numero = input('Digite o numero da sua casa: ')
    bairro = input('Digite seu bairro: ')
    print('Cadastro finalizado')
    print('A seguir voce irá informar sua renda para identificarmos o seu nivel de prioridade\n')
    print('--------NIVEIS DE PRIORIDADE--------')
    print('Existem três niveis de prioridade:')
    print('Nível 1: A de menor prioridade das tres')
    print('Nível 2: A de prioridade média')
    print('Nível 3: A de maior prioridade')
    renda_bruta = float(input('Digite sua renda bruta somada de todos os moradores: '))
    qtd_pessoas_familia = int(input('Digite quantas pessoas moram na sua casa: '))
    prioridade = renda_bruta/qtd_pessoas_familia
    if prioridade == 1320:
        print('O seu nível de prioridade é nivel 2')
    elif prioridade < 1320:
        print('O seu nível de prioridade é nivel 3')
    elif prioridade > 1320:
        print('O seu nível de prioridade é nivel 1')

cadastro_doador_e_doacao()
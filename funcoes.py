from xml.etree.ElementTree import SubElement


def cadastro_doador():
    print('Bem-vindo a sessão de cadastro temporario de doadores de São Paulo!')
    print('Por favor preencha os campos abaixo:\n')

    nome_doador = input('Digite seu nome completo: ').title()
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
        doacao()

def doacao():
    print('')
    print('Bem vindo a sessão de doações de alimentos!')
    print('Por favor, siga os campos abaixo:\n')
    alimento = input('Qual alimento voce quer doar? ')
    qtd = float(input('Qual a quantidade em KG? '))
    
    
    print('A seguir conversaremos sobre o transporte do alimento')
    regiao_doacao = input('Digite em qual região voce quer que a sua doação seja redirecionada em São Paulo:(norte/sul/leste/oeste) ')
    if regiao_doacao == 'sul':
        transporte = input('O transporte do alimento será realizado pela sua pessoa ou por uma transportadora?(1 - eu / 2 - transportadora) ')
        if transporte == '1':
            print('A Instituição da sua região se chama Cruz Vermelha de São Paulo')
            print('Se localiza na: Av. Moreira Guimarães, 699 - Indianópolis')
        
        elif transporte == '2':
            print('Por favor, digite seu endereço:\n')
            logradouro = input('Logradouro: ')
            numero = int(input('Digite o seu numero: '))
            cep = input('Digite seu CEP: ')
            print('Otimo, seus dados serão enviados para a instituição Cruz Vermelha de São Paulo, que se localiza na zona sul')
            print('Assim que o transporte estiver a caminho, voce sera notificado\n')
            print('Endereço cadastro, resumo da operação:')
            print(f'Logradouro: {logradouro}')
            print(f'Numero: {numero}')
            print(f'CEP: {cep} ')
    elif regiao_doacao == 'oeste':
        transporte = input('O transporte do alimento será realizado pela sua pessoa ou por uma transportadora? Digite o número(1 - eu / 2 - transportadora) ')
        if transporte == '1':
            print('Excelente, a sua doação sera direcionada para o depósito da FUSSP(Fundo Social de São Paulo)')
            print('Se localiza na: Av. Marechal Mario Guedes, 301, no Jaguaré')
        
        elif transporte == '2':
            print('Por favor, digite seu endereço:\n')
            logradouro = input('Logradouro: ')
            numero = int(input('Digite o seu numero: '))
            cep = input('Digite seu CEP: ')
            print('Otimo, seus dados serão passados para a instituição FUSSP(Fundo Social de São Paulo), localizado na zona oeste')
            print('Assim que o transporte estiver a caminho, voce sera notificado\n')
            print('Endereço cadastro, resumo da operação:')
            print(f'Logradouro: {logradouro}')
            print(f'Numero: {numero}')
            print(f'CEP: {cep} ')
    elif regiao_doacao == 'leste':
        transporte = input('O transporte do alimento será realizado pela sua pessoa ou por uma transportadora? Digite o número(1 - eu / 2 - transportadora) ')
        if transporte == '1':
            print('Ótimo, a sua doação será direcionada para a ONG Palavra Viva, na zona leste')
            print('Se localiza na: Rua Dr. Camilo Haddad, 186 Altos - Parque São Lucas')
        
        elif transporte == '2':
            print('Por favor, digite seu endereço:\n')
            logradouro = input('Logradouro: ')
            numero = int(input('Digite o seu numero: '))
            cep = input('Digite seu CEP: ')
            print('Otimo, os seus dados serão enviados para a instituição Palavra Viva, localizada na zona leste')
            print('Assim que o transporte estiver a caminho, voce sera notificado\n')
            print('Endereço cadastro, resumo da operação:')
            print(f'Logradouro: {logradouro}')
            print(f'Numero: {numero}')
            print(f'CEP: {cep} ')
    elif regiao_doacao == 'norte':
        transporte = input('O transporte do alimento será realizado pela sua pessoa ou por uma transportadora? Digite o número(1 - eu / 2 - transportadora) ')
        if transporte == '1':
            print('Excelente, a sua doação será direcionada para o Banco de Alimentos localizado na zona Norte')
            print('Se localiza na: Rua Sobral Júnior, 264 - Vila Maria ')
        
        elif transporte == '2':
            print('Por favor, digite seu endereço:\n')
            logradouro = input('Logradouro: ')
            numero = int(input('Digite o seu numero: '))
            cep = input('Digite seu CEP: ')
            print('Os seus dados serão enviados para a instituição Banco de Alimentos, localizado na Zona Norte')
            print('Assim que o transporte estiver a caminho, voce sera notificado\n')
            print('Endereço cadastro, resumo da operação:')
            print(f'Logradouro: {logradouro}')
            print(f'Numero: {numero}')
            print(f'CEP: {cep} ')

def cadastro_donatario():
    print('Bem vindo a sessão de cadastro de donatário')
    print('Por favor preencha os campos abaixo:\n')
    nome = input('Digite seu nome completo: ').title()
    cpf = input('Digite seu CPF: ')
    data_nascimento = input('Digite sua data de nascimento: ')
    logradouro = input('Digite seu logradouro: ')
    numero = input('Digite o numero da sua casa: ')
    bairro = input('Digite seu bairro: ')
    print('Cadastro finalizado')
    print('A seguir voce irá informar sua renda para identificarmos o seu nivel de prioridade\n')
    print('--------NIVEIS DE PRIORIDADE--------')
    print('Existem três niveis de prioridade:')
    print('Nível 1: A que precisa de mais assistencia')
    print('Nível 2: A que precisa de assistencia nivel moderada')
    renda_bruta = float(input('Digite sua renda bruta somada de todos os moradores: '))
    qtd_pessoas_familia = int(input('Digite quantas pessoas moram na sua casa: '))
    prioridade = renda_bruta/qtd_pessoas_familia
    print(f'Renda per capita da familia: {prioridade}')
    if prioridade == 1320:
        print('O seu nível de prioridade é nivel 2')
    elif prioridade < 1320:
        print('O seu nível de prioridade é nivel 1')
    elif prioridade > 1320:
        print('Você não possui os direitos para receber doação')
    

def lista_de_alimentos_doacao():
    print('Caso voce queira criar uma lista de alimentos a ser doado, siga os passos:')

    lista = []
    while True:
        print('Por favor, digite os alimentos desejados para serem doados:\n')
        alimento = input('Digite um alimento ou digite sair para finalizar: ').title()
        if alimento.lower() == 'sair':
            print('Alimentos adicionados:')
            for alimento in lista:
                print(alimento)
            print('Lista criada e finalizada')
            print('Muito obrigado pela sua gentileza e bondade!.')
            break

        lista.append(alimento)
        for alimento in lista:
            print(alimento)
           
    return lista
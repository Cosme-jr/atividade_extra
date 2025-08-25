while True:
    try:
        senha = input('Digite a senha (ou "sair" para encerrar): ')
        if senha.lower() == "sair":
            print('Encerrando o programa.')
            break

        if len(senha) < 8:
            raise Exception('Senha muito curta. Deve ter pelo menos 8 caracteres.')

        tem_numero = False
        for char in senha:
            if char.isdigit():
                tem_numero = True
                break
        if not tem_numero:
            raise Exception('Senha deve conter pelo menos um número.')
        print('Senha forte!')

    except Exception as e:
        print(f'Erro: {e} Tente novamente.')
        




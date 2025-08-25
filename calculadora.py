while True:
    try:
        num = float(input('Digite um número: '))
        num2 = float(input('Digite outro número: '))
        operacao = input('Digite a operação (+, -, *, /) ou "sair" para encerrar: ')

        if operacao == '+':
            resultado = num + num2
        elif operacao == '-':
            resultado = num - num2
        elif operacao == '*':
            resultado = num * num2
        elif operacao == '/':
            resultado = num / num2
        elif operacao == 'sair':
            print('Encerrando a calculadora.')
            break
        else:
            print('Operação inválida.')

            raise Exception()

        print(f'Resultado: {resultado}')

    except ValueError:
        print('Digite um número válido.')

    except ZeroDivisionError:
        print('Erro: Divisão por zero não é permitida.')
    except Exception:
        print('Você deve digitar apenas operações válidas (+, -, *, /)')
    finally:
        print('Fim da operação.')
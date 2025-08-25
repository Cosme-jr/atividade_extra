notas = []

while True:
    try:
        entrada = input('Digite a nota do aluno de 0 a 10 (ou -1 para sair): ')
        if entrada.lower() == 'fim':
            break
        nota = float(entrada)
        if nota < 0 or nota > 10:
            raise Exception()
        notas.append(nota)

    except ValueError:
        print('Entrada inválida. Digite um número.')

    except Exception:
        print('Erro inesperado. Tente novamente.')

if notas:
    media = sum(notas) / len(notas)
    print(f'A média das notas é: {media:.2f}')
else:
    print('Nenhuma nota válida foi digitada.')

par= 0
impa = 0
while True:
    try:
        entrada = input('Digite um número (ou fim para sair): ')
        if entrada.lower() == 'fim':
            break
        numero = int(entrada)
        
        if numero % 2 == 0:
            par += 1
        else:
            impa += 1
            if numero < 0:
                raise ValueError('Número negativo não é permitido.')
    except ValueError:
        print('Entrada inválida. Digite um número inteiro.')

print(f'Números pares: {par}')
print(f'Números ímpares: {impa}')
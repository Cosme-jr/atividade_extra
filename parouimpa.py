par= 0
impa = 0
while True:
    try:
        entrada = input('Digite um número (ou -1 para sair): ')
        if entrada.lower() == 'fim':
            break
        numero = int(entrada)
        
        if numero % 2 == 0:
            par += 1
        else:
            impa += 1
            raise Exception('Número ímpar detectado.')

            
    except ValueError:
        print('Entrada inválida. Digite um número inteiro.')

print(f'Números pares: {par}')
print(f'Números ímpares: {impa}')
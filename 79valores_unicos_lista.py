valores = []
while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    continuar = input('Deseja continuar? [S/N] ').upper()[0].strip()
    if continuar in 'Nn':
        break
print('-=' * 30)
valores.sort()
print(f'Voçê digitou os valores {valores}')

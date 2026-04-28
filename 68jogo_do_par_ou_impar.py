from random import randint
cont = 0
resultado = ''
print('=-'*15)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-'*15)
while True:
    jogador = int(input('Digite um valor: '))
    pi = ' '
    while pi not in 'PI':
        pi = str(input('Par ou Impar? [P/I] ')).upper().strip()[0]
    computador = randint(1, 10)
    total = computador + jogador
    print('-' * 30)
    print(f'Voçê jogou {jogador} e o computador jogou {computador}. Total de {total} - ', end=' ')
    if total % 2 == 0:
       resultado = 'PAR'
    else:
       resultado = 'IMPAR'
    print(resultado)
    print('-' * 30)
    if pi == 'P' and resultado == 'PAR' or pi == 'I' and resultado == 'IMPAR':
        print('Voçê VENCEU!')
        print('Vamos jogar novamente!...')
        print('=-' * 15)
        cont += 1
    else:
        print('Voçe PERDEU!')
        print('=-' * 15)
        print(f'GAME OVER! Voçê venceu {cont} vez(es).')
        break

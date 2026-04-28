while True:
    valor = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if valor < 0:
        break
    for n in range(1, 11):
        print(f'{valor} x {n} = {valor*n}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO, Volte Sempre!')


cont1 = cont2 = cont3 = 0
while True:
    print('-' * 25)
    print('CADASTRE UMA PESSOA')
    print('-' * 25)
    idade = int(input('Idade: '))
    if idade >= 18:
        cont1 += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [F/M] ')).upper().strip()[0]
    print('-' * 25)
    if sexo == 'M':
        cont2 += 1
    if sexo == 'F' and idade < 20:
        cont3 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {cont1}')
print(f'Ao todo temos {cont2} homens cadastrados ')
print(f'E temos {cont3} mulher(es) com menos de 20 anos')



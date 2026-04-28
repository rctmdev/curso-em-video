print('=' * 30)
print('{:^30}'.format('SEU BANCO'))
print('=' * 30)
tot50 = tot20 = tot10 = tot1 = 0
rest50 = rest20 = rest10 = 0
valor = int(input('Que valor voçê quer sacar? R$ '))
while True:
    tot50 = valor // 50
    rest50 = valor % 50
    if tot50 != 0:
        print(f'Total de {tot50} cédula(s) de R$ 50,00')
    if rest50 != 0:
        tot20 = rest50 // 20
        rest20 = valor % 20
        if tot20 != 0:
            print(f'Total de {tot20} cédula(s) de R$ 20,00')
    if rest20 != 0:
        tot10 = rest20 // 10
        rest10 = valor % 10
        if tot10 != 0:
            print(f'Total de {tot10} cédula(s) de R$ 10,00')
    if rest10 != 0:
        tot1 = rest10 // 1
        print(f'Total de {tot1} cédula(s) de R$ 1,00')
    break
print('=' * 30)
print('Volte sempre ao SEU BANCO! Tenha um bom dia!')


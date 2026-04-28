teste = list()
teste.append('Ricardo')
teste.append(43)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(galera)
print('=-'*20)

turma = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in turma:
    print(f'{p[0]} tem {p[1]} anos de idade.')
print('=-'*20)

gal = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    gal.append(dado[:])
    dado.clear()

for p in gal:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')

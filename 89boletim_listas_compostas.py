lista = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-='*30)
print(f'{'N°.':<4}{'NOME':<10}{'MÉDIA':>8}')
print('-'*30)
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 30)
    n = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if n == 999:
        print('FINALIZANDO...')
        break
    if n <= len(lista) - 1:
        print(f'Notas de {lista[n][0]} são {lista[n][1]}')
print('<<< Volte sempre >>>')







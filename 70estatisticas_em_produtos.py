soma = totmil = menor = cont = 0
barato = ''
print('-' * 30)
print(f'{'LOJA SUPER BARATÃO':^30}')
print('-' * 30)
while True:
    nome = str(input('Nome do produto: '))
    preço = float(input('Valor do produto: R$ '))
    cont += 1
    soma += preço
    if preço >= 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = nome
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print('{:-^30}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R$ {soma:.2f}')
print(f'Temos {totmil} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}')

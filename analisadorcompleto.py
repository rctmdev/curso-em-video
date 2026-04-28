media = 0
ihmv = 0
cont = 0
nhmv = ''
for p in range (1, 5):
    print('----- {}° PESSOA -----'.format(p))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper()
    media = media + idade
    if sexo == 'M':
        if p == 1:
            ihmv = idade
            nhmv = nome
        else:
            if idade > ihmv:
                ihmv = idade
                nhmv = nome
    if sexo == 'F' and idade < 20:
        cont = cont + 1
print('A média de idade do grupo é de {:.1f} anos'.format(media/4))
print('O homem mais velho tem {} anos e se chama {}.'.format(ihmv,nhmv))
print('Ao todo são {} mulheres com menos de 20 anos'.format(cont))


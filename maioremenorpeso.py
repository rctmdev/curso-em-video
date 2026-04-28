numeros = []
for c in range(1,6):
    peso = float(input('Peso da {}° pessoa: '.format(c)))
    numeros.append(peso)
    maior = max(numeros)
    menor = min(numeros)
print('O maior peso lido foi de {}.'.format(maior))
print('O menor peso lido foi de {}.'.format(menor))



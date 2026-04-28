soma = 0
cont = 0
for c in range (1, 7):
    n = int(input('Digite o {}° valor: '.format(c)))
    if n % 2 == 0: 
        cont = cont + 1
        soma = soma + n
print('A soma dos {} números pares é {}'.format(cont, soma))

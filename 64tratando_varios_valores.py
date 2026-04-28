num = cont = soma = 0
while num != 999:
    num = int(input('Digite o número [999 para parar]: '))
    if num != 999:
        cont += 1
        soma += num
print('Voçê digitou {} números e a soma entre eles foi {}'.format(cont, soma))

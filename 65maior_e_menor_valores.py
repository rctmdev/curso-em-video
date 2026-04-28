continuar = 'S'
maior = menor = cont = soma = 0
while continuar in 'S':
    numero = int(input('Digite um número: '))
    cont += 1
    soma += numero
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if numero == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
print('Voçê digitou {} números e a média foi {}'.format(cont, soma / cont))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))


print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
n1 = 0
n2 = 1
cont = 3
termos = int(input('Quantos termos voçê quer mostrar? '))
print('~'*30)
print('{} -> {} -> '.format(n1, n2), end='')
while cont <= termos:
    n3 = n1 + n2
    print('{} ->'.format(n3), end=' ')
    cont = cont + 1
    n1 = n2
    n2 = n3
print('FIM')
print('~'*30)

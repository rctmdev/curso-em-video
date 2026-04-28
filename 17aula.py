num = [2, 5, 9, 1]
num [2] = 3
print(num)
num.append(7)
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
num.insert(2, 0)
print(num)
num.pop()
print(num)
num.remove(0)
print(num)
print(f'Essa lista tem {len(num)} elementos')

print('-='*30)

valores = list()
for cont in range(0, 3):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

print('-='*30)

a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(a)
print(b)
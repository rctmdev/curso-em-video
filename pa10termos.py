print('='*32)
print('      10 TERMOS DE UMA PA')
print('='*32)
pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))
for c in range (pt, pt + 10 * r, r):
    print(c,'->', end=' ')
print('ACABOU')    
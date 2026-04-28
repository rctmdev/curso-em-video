times = ('Palmeiras', 'São Paulo', 'Corinthians', 'Bahia', 'Fluminense',
         'Athletico-PR', 'Bragantino', 'Grêmio', 'Chapecoense', 'Mirassol',
         'Flamengo', 'Coritiba', 'Santos', 'Botafogo', 'Vitória', 'Remo',
         'Atlético-MG', 'Internacional', 'Cruzeiro', 'Vasco da Gama')
print('=-' * 20)
print(f'Lista de times do Brasileirão: {times}')
print('=-' * 20)
print(f'Os 5 primeiros são: {times[0:5]}')
print('=-' * 20)
print(f'Os 4 últimos são: {times[-4:]}')
print('=-' * 20)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('=-' * 20)
print(f'O Chapecoense está na {times.index('Chapecoense')+1}° posição')
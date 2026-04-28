d = dict()
d['nome'] = str(input('Nome: '))
d['media'] = float(input(f'Média de {d["nome"]}: '))
if d['media'] >= 7:
    d['situacao'] = 'Aprovado'
elif 5 <= d['media'] < 7:
    d['situacao'] = 'Recuperação'
else:
    d['situacao'] = 'Reprovado'
print('-='*20)
for k, v in d.items():
    print(f'  - {k} é igual a {v}')


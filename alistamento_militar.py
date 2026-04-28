from datetime import date
aa = date.today().year
an = int(input('Ano de nascimento: '))
i = aa - an 
if i < 18: 
    print('''Quem nasceu em {} tem {} anos em {}.
Ainda falta(m) {} ano(s) para o alistamento militar. 
Seu alistamento será em {}'''.format(an, i, aa, 18-i, (18-i)+2025))
elif i > 18:
    print('''Quem nasceu em {} tem {} anos em {}.
Você já deveria ter se alistado há {} anos.
Seu alistamento foi em {}.'''.format(an, i, aa, i-18, 2025-(i-18)))
else: 
    print('''Quem nasceu em {} tem 18 anos em {}.
Você tem que se alistar IMEDIATAMENTE!'''.format(an, aa))


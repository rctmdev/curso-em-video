an = int(input('Ano de nascimento: '))
i = 2025 - an 
if i < 18: 
    print('''Quem nasceu em {} tem {} anos em 2025.
Ainda falta(m) {} ano(s) para o alistamento militar. 
Seu alistamento será em {}'''.format(an, i, 18-i, (18-i)+2025))
elif i > 18:
    print('''Quem nasceu em {} tem {} anos em 2025.
Você já deveria ter se alistado há {} anos.
Seu alistamento foi em {}.'''.format(an, i, i-18, 2025-(i-18)))
else: 
    print('''Quem nasceu em {} tem 18 anos em 2025.
Você tem que se alistar IMEDIATAMENTE!'''.format(an))


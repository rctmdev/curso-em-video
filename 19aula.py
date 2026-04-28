pessoas = {'nome': 'Ricardo', 'sexo': 'M', 'idade': 43}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print('-='*20)
for k in pessoas.keys():
    print(k)
for v in pessoas.values():
    print(v)
for k,v in pessoas.items():
    print(f'{k} = {v}')
print('-='*20)
dicionario = {'nome': 'Ricardo', 'sexo': 'M', 'idade': 43}
del dicionario['sexo']
dicionario['nome'] = 'Gustavo'
dicionario['peso'] = 79
for k, v in dicionario.items():
    print(f'{k} = {v}')
print('-='*20)
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])
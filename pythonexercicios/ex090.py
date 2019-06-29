d = {'Nome': input('Nome: ')}
d['Média'] = float(input(f'Média de {d["Nome"]}: ').strip())
if d['Média'] < 5:
    d['Situação'] = 'Reprovado'
elif d['Média'] < 7:
    d['Situação'] = 'Recuperação'
else:
    d['Situação'] = 'Aprovado'
print('-='*30)
for k, v in d.items():
    print(f'    - {k} é igual a {v}')

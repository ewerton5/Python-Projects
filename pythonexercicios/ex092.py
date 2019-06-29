from datetime import date
d = {'nome': input('Nome: ').strip()}
a = int(input('Ano de nascimento: ').strip())
d['idade'] = date.today().year - a
ctps = int(input('Carteira de Trabalho (0 não tem): ').strip())
if ctps != 0:
    d['ctps'] = ctps
    d['contratação'] = int(input('Ano de contratação: ').strip())
    d['salário'] = float(input('Salário: '))
    d['aposentadoria'] = d['contratação'] + 35 - a
print('-='*30)
for k, v in d.items():
    print(f'{k} tem o valor {v}')

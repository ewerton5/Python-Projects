from datetime import date
a = int(input('Ano de nascimento: '))
i = date.today().year - a
print(f'O atleta tem {i} anos.\nClassificação: ', end='')
if i < 10:
    print('MIRIM')
elif i < 15:
    print('INFANTIL')
elif i < 20:
    print('JUNIOR')
elif i < 26:
    print('SÊNIOR')
else:
    print('MASTER')

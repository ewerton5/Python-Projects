from datetime import date
a = int(input('Ano de nascimento: '))
i = date.today().year - a
print(f'Quem nasceu em {a} tem {i} em {date.today().year}.')
if i < 18:
    print(f'Ainda faltam {18-i} anos para o alistamento.'
          f'\nSeu alistamento será em {a+18}')
elif i == 18:
    print(f'Você tem que se alistar IMEDIATAMENTE!')
else:
    print(f'Você já deveria ter se alistado à {i-18} anos.'
          f'\nSeu alistamento foi em {a+18}.')

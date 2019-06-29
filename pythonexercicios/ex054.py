from datetime import date
s= 0
for c in range(1, 8):
    a = int(input(f'Em que ano a {c}° pessoa nasceu? '))
    if date.today().year - a > 21:
        s += 1
print(f'{7-s} pessoas ainda não atingiram a maioridade.'
      f'\n{s} pessoas já são maiores.')

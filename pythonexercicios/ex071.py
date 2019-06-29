print('\033[33m-=-'*21)
print('-=-'*8+'\033[34m   Banco CEV   '+'\033[33m-=-\033[m'*8)
print('\033[33m-=-\033[m'*21)
n = int(input('\033[36mQue valor você quer sacar? R$').strip())
c50 = n//50
c20 = (n % 50)//20
c10 = ((n % 50) % 20)//10
c5 = (((n % 50) % 20) % 10)//5
c = (((n % 50) % 20) % 10) % 5
if c50 != 0:
    print(f'\033[31mTotal de {c50} cédulas de R$50')
if c20 != 0:
    print(f'\033[31mTotal de {c20} cédulas de R$20')
if c10 != 0:
    print(f'\033[31mTotal de {c10} cédulas de R$10')
if c5 != 0:
    print(f'\033[31mTotal de {c5} cédulas de R$5')
if c != 0:
    print(f'\033[31mTotal de {c} cédulas de R$1')
print('\033[33m-=-\033[m'*21)
print('\033[35mVolte sempre ao BANCO CEV! Tenha um bom dia!')

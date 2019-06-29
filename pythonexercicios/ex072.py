n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
     'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    x = int(input('Digite um número entre 0 e 20: ').strip())
    while x < 0 or x > 20:
        x = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {n[x]}')
    c = input('Quer continuar? [S/N] ').strip().upper()[0]
    if c == 'N':
        break

print('\033[33m-=-'*21)
print('-=-'*6+'\033[34m Sequência  de  Fibonacci  '+'\033[33m-=-\033[m'*6)
print('\033[33m-=-\033[m'*21)
a, b = 0, 1
n = int(input('Quantos elementos você quer ver? ').strip())
while n != 0:
    print(a, end=' → ')
    a, b = b, a + b
    n -= 1
print('ACABOU')

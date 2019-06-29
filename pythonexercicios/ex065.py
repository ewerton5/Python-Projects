c = 'SIM'
s = t = 0
while c in 'SIMQUERO':
    n = int(input('Digite um número: '))
    c = input('Quar continuar? ').upper().strip()
    s += n
    t += 1
    if t == 1:
        me = ma = n
    else:
        if n > ma:
            ma = n
        if n < me:
            me = n
print(f'Você digitou {t} números e a média foi {s/t:.2f}'
      f'\nO maior valor foi {ma} e o menor foi {me}')

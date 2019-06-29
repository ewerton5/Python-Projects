s = n = c = 0
while n != 999:
    c += 1
    s += n
    n = int(input('Digite um número(para parar digite 999): '))
print(f'Você digitou {c-1} números e a soma entre eles foi {s}.')

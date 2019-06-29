print('\033[33m-=-'*20)
print('\033[34mAnaisador de Triângulos')
print('\033[33m-=-\033[m'*20)
s1 = float(input('\033[32mPrimeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1+s2 > s3 and s1+s3 > s2 and s2+s3 > s1:
    print('\033[mOs segmentos acima \033[34mPODEM FORMAR\033[m triângulo ', end='')
    if s1 == s2 == s3:
        print('equilátero!')
    elif s1 != s2 != s3 != s1:
        print('escaleno!')
    else:
        print('isósceles!')
else:
    print('\033[mOs segmentos acima \033[31mNÃO PODEM FORMAR\033[m triângulo!')

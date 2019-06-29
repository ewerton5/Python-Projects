n = int(input('\033[35mDiga um número qualquer:\033[m '))
if n % 2 == 0:
    print(f'O número {n} é \033[34mPAR')
else:
    print(f'O número {n} é \033[34mÍMPAR')

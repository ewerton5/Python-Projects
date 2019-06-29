from time import sleep
n1 = int(input('Digite um número: ').strip())
n2 = int(input('Digite um número: ').strip())
o = 0
while o != 5:
    print('Selecione uma opção do menu:'
          '\n   [1] Somar'
          '\n   [2] Multiplicar'
          '\n   [3] Maior'
          '\n   [4] Novos números'
          '\n   [5] Sair do programa')
    o = int(input('>>>>> Qual sua opção? ').strip())
    if o == 1:
        print(f'A soma entre {n1} e {n2} vale {n1 + n2}')
    elif o == 2:
        print(f'O produto de {n1} e {n2} vale {n1 * n2}')
    elif o == 3:
        print(f'O maior valor entre {n1} e {n2} é {max(n1, n2)}')
    elif o == 4:
        n1 = int(input('Digite um número: ').strip())
        n2 = int(input('Digite um número: ').strip())
    elif o == 5:
        print('Finalizando...')
    else:
        print('Opção inválida, tente novamente.')
    print('=-='*10)
    sleep(1)
print('Fim do programa! Volte sempre!')

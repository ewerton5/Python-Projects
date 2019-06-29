# Ewerton Vieira de Silles
# 01/05/2019
#
# Programa que exibe um menu de uma calculadora que realiza as operacoes de multiplicacao; divisao;
# mmc e mdc entre dois numeros; e todos os numeros primos ate um determinado limite

# Funcao - calcula o produto de uma multiplicacao somando um fator a ele mesmo tantas vezes quanto vale o outro fator

def multiplicar(fator1, fator2):
    multiplicador = fator1
    if fator2 == 0:
        multiplicador = 0
    else:
        for cont in range(1, fator2):
            multiplicador += fator1
    return multiplicador

# Funcao - calcula o quociente e o resto de uma divisao subtraindo o divisor do dividendo tantas vezes quanto possivel

def dividir(dividendo, divisor):
    resto = dividendo
    if dividendo < divisor:
        quociente = 0
    else:
        resto -= divisor
        quociente, resto = dividir(resto, divisor)
        quociente += 1
    return quociente, resto

# Funcao - calcula o MMC entre dois numeros testando se os numeros posteriores ao maior sao divisiveis por ambos

def mmc(numero1, numero2):
    if (numero1 > numero2):
        maior = numero1
    else:
        maior = numero2
    while True:
        if (maior % numero1 == 0 and maior % numero2 == 0):
            return maior
        else:
            maior += 1

# Funcao - calcula o MDC entre dois numeros testando se ambos sao divisiveis pelos numeros anteriores ao menor

def mdc(numero1, numero2):
    if (numero1 < numero2):
        menor = numero1
    else:
        menor = numero2
    while True:
        if (numero1 % menor == 0 and numero2 % menor == 0):
            return menor
        else:
            menor -= 1

# Funcao - verifica quantos divisores tem cada numero e exibe todos os primos(numeros que so tem dois divisores) ate um determinado limite

def primos(limite):
    primos = '2'
    for numero in range(3, limite + 1):
        totaldivisores = 0
        for divisor in range(1, numero + 1):
            if (numero % divisor == 0):
                totaldivisores += 1
        if (totaldivisores == 2):
            primos += ', ' + str(numero)
    return primos


# Funcao - imprime o menu principal do programa com seis opcoes

def menu():
    print('=-=-=-= Calculadora =-=-=-='
          '\nSelecione uma opção do menu:'
          '\n   [1] Multiplicar'
          '\n   [2] Dividir'
          '\n   [3] M.M.C.'
          '\n   [4] M.D.C.'
          '\n   [5] Primos'
          '\n   [6] Sair do programa')


######## Programa principal ########

def main():
    menu()
    opcao = int(input('Qual sua opção? ').strip())
    while (opcao < 1 or opcao > 6):
        print('Opção inválida!')
        opcao = int(input('Qual sua opção? ').strip())
    if (opcao == 1):
        fator1 = int(input('Entre com o primeiro fator (número inteiro maior ou igual a zero): '))
        while (fator1 < 0):
            fator1 = int(input('Valor inválido! Por favor, entre com um número inteiro maior ou igual a zero: '))
        fator2 = int(input('Entre com o segundo fator (número inteiro maior ou igual a zero): '))
        while (fator2 < 0):
            fator2 = int(input('Valor inválido! Por favor, entre com um número maior ou igual a zero: '))
        produto = multiplicar(fator1, fator2)
        print('=-=' * 10)
        print('O produto de', fator1, 'e', fator2, 'vale', produto)
    elif (opcao == 2):
        dividendo = int(input('Entre com o dividendo (número inteiro maior ou igual a zero): '))
        while (dividendo < 0):
            dividendo = int(input('Valor inválido! Por favor, entre com um número maior ou igual a zero: '))
        divisor = int(input('Entre com o divisor (número inteiro maior que zero): '))
        while (divisor <= 0):
            divisor = int(input('Valor inválido! Por favor, entre com um número maior que zero: '))
        quociente, resto = dividir(dividendo, divisor)
        print('=-=' * 10)
        print('A divisão', str(dividendo) + '/' + str(divisor), 'tem quociente igual a', quociente, 'e resto igual a', resto)
    elif (opcao == 3):
        numero1 = int(input('Entre com um número inteiro maior que zero: '))
        while (numero1 <= 0):
            numero1 = int(input('Valor inválido! Por favor, entre com um número maior que zero: '))
        numero2 = int(input('Entre com outro número inteiro maior que zero: '))
        while (numero2 <= 0):
            numero2 = int(input('Valor inválido! Por favor, entre com um número maior que zero: '))
        mmcnumero = mmc(numero1, numero2)
        print('=-=' * 10)
        print('O M.M.C. entre', numero1, 'e', numero2, 'vale', mmcnumero)
    elif (opcao == 4):
        numero1 = int(input('Entre com um número inteiro maior que zero: '))
        while (numero1 <= 0):
            numero1 = int(input('Valor inválido! Por favor, entre com um número maior que zero: '))
        numero2 = int(input('Entre com outro número inteiro maior que zero: '))
        while (numero2 <= 0):
            numero2 = int(input('Valor inválido! Por favor, entre com um número maior que zero: '))
        mdcnumero = mdc(numero1, numero2)
        print('=-=' * 10)
        print('O M.D.C. entre', numero1, 'e', numero2, 'vale', mdcnumero)
    elif (opcao == 5):
        limite = int(input('Entre com o limite (número inteiro maior que 1): '))
        while (limite < 2):
            limite = int(input('Valor inválido! Por favor, entre com um número maior que 1: '))
        if (limite == 2):
            print('=-=' * 10)
            print('2 é o primeiro número primo.')
        else:
            primoslimite = primos(limite)
            print('=-=' * 10)
            print('Os números primos até', limite, 'são:', primoslimite + '.')
    print('=-=' * 10)
    if (opcao != 6):
        main()


##### Inicializacao do programa

main()

##### Termino do programa

print('Fim do programa! Volte sempre!')

# Ewerton Vieira
# aula 11 de abril
#
# programa monstra um menu

valor1 = int(input('Digite um valor inteiro: '))
valor2 = int(input('Digite outro valor inteiro: '))
print('\033[33m-=-'*10)
print('\033[36mEscolha uma opção:\n'
      '[1] soma\n'
      '[2] subtração\n'
      '[3] multiplicação\n'
      '[4] divisão')
print('\033[33m-=-'*10)
opcao = int(input('\033[mSua opção: '))
while opcao < 1 or opcao > 4:
	print('\033[31mOpção inválida!\033[m')
	opcao = int(input('\033[mSua opção: '))
if opcao == 1:
	print(valor1+valor2)
if opcao == 2:
	print(valor1-valor2)
if opcao == 3:
	print(valor1*valor2)
if opcao == 4:
	print(valor1/valor2)
